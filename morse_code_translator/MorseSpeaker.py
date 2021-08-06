from re import ASCII
import wave
from AudioTranslation import translate as tr

__FILES = ['sound_source/short.wav', 'sound_source/long.wav', 'sound_source/silent.wav']
__SOUNDS = []

w = wave.open(__FILES[0], 'rb')
__PARAMS = w.getparams()
w.close()

for file in __FILES:
    w = wave.open(file, 'rb')
    __SOUNDS.append(w.readframes(w.getnframes()))
    w.close()

def create_morse_sound(morse_text):
    sound = []

    for c in morse_text:
        if c == '.':
            sound.append(__SOUNDS[0])
        elif c == '-':
            sound.append(__SOUNDS[1])
        elif c == ' ':
            sound.append(__SOUNDS[2])
    
    return sound

def export_sound(sound, file_name='output.wav', format_name='wav'):
    out_sound = wave.open(file_name, 'wb')
    out_sound.setparams(__PARAMS)

    for frames in sound:
        out_sound.writeframes(frames)
    
    out_sound.close()
