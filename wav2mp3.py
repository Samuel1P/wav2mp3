#!D:\Python\wav2mp3\mp3_venv\Scripts\python.exe

from pydub import AudioSegment
import os,sys

def get_wav_list():
    dir = os.getcwd()

    dirty_dir = os.path.join(dir, 'dirty')
    global clean_dir
    clean_dir = os.path.join(dir, 'clean')
    assert os.path.exists(dirty_dir), "DIRTY DIRECTORY IS NOT PRESENT"
    assert os.path.exists(dirty_dir), "CLEAN DIRECTORY IS NOT PRESENT"
    os.chdir(dirty_dir)
    print (os.getcwd())
    wav_list = os.listdir(dirty_dir)
    dirty_list=[]
    for i in wav_list:
        if i.endswith("wav"): #Refactor this with glob later
            dirty_list.append(os.path.join(dirty_dir,i))
    assert (len(dirty_list) >= 1), "No Wav Files present."
    print (dirty_list)
    return dirty_list

def convert(wav_list):
    for wav in wav_list:
        track = AudioSegment.from_wav(wav)
        file_name = os.path.basename(wav)
        print (f"{file_name} conversion in progress...")
        clean_name_wav = os.path.join(clean_dir,file_name)
        clean_name_mp3 = os.path.splitext(clean_name_wav)[0]+".mp3"
        track.export(clean_name_mp3, format="mp3", bitrate="320k")
    print ("Conversion is complete.")

if __name__ == "__main__":
    x = get_wav_list()
    convert(x)



