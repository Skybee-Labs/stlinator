import subprocess

def extract_audio(input_file, sample_rate):
    ffmpeg_cmd = ['ffmpeg', 
                  '-loglevel', 'quiet', 
                  '-i', input_file, 
                  '-acodec', 'pcm_s16le', 
                  '-ar', str(sample_rate), 
                  '-ac', '1', 
                  '-f', 'wav', 
                  '-']

    try:
        process1 = subprocess.Popen(ffmpeg_cmd, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
        return process1
    except subprocess.CalledProcessError as e:
        print('Error occurred during audio extraction:')
        print(e.output.decode())

