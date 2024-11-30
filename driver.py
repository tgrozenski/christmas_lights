from pydub import AudioSegment
from pydub.playback import play
import threading
import time

def play_audio():
    song = AudioSegment.from_mp3("audio/little_drummer_boy.mp3")
    print('playing sound using  pydub on thread 1')
    play(song)

def lights_subprocess():
    count = 0
    while True:
        print('subprocess 2 is executing', count)
        count += 1
        time.sleep(3)

if __name__ == "__main__":
    t1 = threading.Thread(target=play_audio)
    t2 = threading.Thread(target=lights_subprocess)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print('done')
