import soundfile as sf
import librosa
import numpy as np
import os
from pydub import AudioSegment

from moviepy.editor import VideoFileClip
def get_audio(video_path):

    audio = AudioSegment.from_file(video_path)
    audio_path = "./temp_audio.wave" 
    audio.export(audio_path, format='wav')
    sound, sr = librosa.load(audio_path)

    os.remove(audio_path)
    return (sound, sr)

def calculate_sound_quality(sound, time_stamp = 0):
    max_amp = abs(max(sound))
    arr = np.array(sound)
    mx = np.max(arr)
    rms = np.sqrt(np.mean(arr**2))
    return 10*np.log(mx/rms)


if __name__ == "__main__":
    #path = "/home/yohansh/Music/test_audio.mp3"
    #path = "/home/yohansh/Music/test_audio_2.mp3"
    #sound, _ = librosa.load(path)
    #calculate_sound_quality(sound)

    video_path = "/home/yohansh/Videos/video_files/20s_coca_cola_ad.mp4"

    sound, sr = get_audio(video_path)
    total_second = 10 
    start = int(total_second) - 5
    end  = int(total_second)
    sound_part = sound[start*sr:end*sr]
    sound_quality = calculate_sound_quality(sound_part)
