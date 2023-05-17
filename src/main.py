#!/usr/bin/env python3

import threading
import sys
from ffmpeg_audio_extractor import extract_audio
from read_audio_chunk import read_audio_chunk
import Word as custom_Word
from queue import Queue

def lambda_handler(event, context):
    queue = Queue()
    chunk_size = 4000
    sample_rate = 16000

    ffmpeg_process = extract_audio(event["input_file"], sample_rate)

    audio_thread = threading.Thread(target=read_audio_chunk, args=(ffmpeg_process, chunk_size, sample_rate, queue))
    audio_thread.start()

    ffmpeg_process.wait()

    audio_thread.join()

    list_of_words = []
    results = queue.get()
    for sentence in results:
        if len(sentence) == 1:
            # sometimes there are bugs in recognition 
            # and it returns an empty dictionary
            # {'text': ''}
            continue
        for obj in sentence['result']:
            w = custom_Word.Word(obj)  # create custom Word object
            list_of_words.append(w)  # and add it to list


    for word in list_of_words:
        print(word.to_string())

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

