import json
from vosk import Model, KaldiRecognizer, SetLogLevel

def read_audio_chunk(process, chunk_size, sample_rate, queue):
    results = []
    SetLogLevel(0)
    model = Model(lang="en-us")
    rec = KaldiRecognizer(model, sample_rate)
    rec.SetWords(True)

    while True:
        output_chunk = process.stdout.read(chunk_size)
        if not output_chunk:
            break
        if rec.AcceptWaveform(output_chunk):
          part_result = json.loads(rec.Result())
          results.append(part_result)
    part_result = json.loads(rec.FinalResult())
    results.append(part_result)

    queue.put(results)
    return