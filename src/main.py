#!/usr/bin/env python3

import threading
import json
import sys
from ffmpeg_audio_extractor import extract_audio
from read_audio_chunk import read_audio_chunk
from queue import Queue


def lambda_handler(event, context):
    queue = Queue()
    chunk_size = 4000
    sample_rate = 16000

    ffmpeg_process = extract_audio(event["input_file"], sample_rate)

    audio_thread = threading.Thread(target=read_audio_chunk, args=(
        ffmpeg_process, chunk_size, sample_rate, queue))
    audio_thread.start()

    ffmpeg_process.wait()

    audio_thread.join()

    results = queue.get()

    file_full_text_string = ' '.join(obj['text'] for obj in results)

    output_dict = {'fullTextString': file_full_text_string, 'results': []}
    for sentence in results:
        if len(sentence) == 1:
            continue
        for obj in sentence['result']:
            output_dict['results'].append(obj)

    with open('output.json', 'w') as file:
        json.dump(output_dict, file)

    return "success"


def main():
    event = {
        "input_file": sys.argv[1]
    }
    context = None
    response = lambda_handler(event, context)
    print(response)


if __name__ == "__main__":
    main()
