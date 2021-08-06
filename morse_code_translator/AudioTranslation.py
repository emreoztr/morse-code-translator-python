import speech_recognition as sr

__MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                'C':'-.-.', 'D':'-..', 'E':'.',
                'F':'..-.', 'G':'--.', 'H':'....',
                'I':'..', 'J':'.---', 'K':'-.-',
                'L':'.-..', 'M':'--', 'N':'-.',
                'O':'---', 'P':'.--.', 'Q':'--.-',
                'R':'.-.', 'S':'...', 'T':'-',
                'U':'..-', 'V':'...-', 'W':'.--',
                'X':'-..-', 'Y':'-.--', 'Z':'--..',
                '1':'.----', '2':'..---', '3':'...--',
                '4':'....-', '5':'.....', '6':'-....',
                '7':'--...', '8':'---..', '9':'----.',
                '0':'-----', ', ':'--..--', '.':'.-.-.-',
                '?':'..--..', '/':'-..-.', '-':'-....-',
                '(':'-.--.', ')':'-.--.-', ' ': ' '}

def translate(audio_file, lang="en-US"):
    recog = sr.Recognizer()
    file = sr.AudioFile(audio_file)

    recog.energy_threshold = 300
    with file as source:
        processed_audio = recog.record(source)

    audio_text = recog.recognize_google(audio_data=processed_audio, language=lang)
    return __text_to_morse(audio_text)

def __text_to_morse(text):
    morse_list = [__MORSE_CODE_DICT.get(ch) for ch in text.upper()]
    return ' '.join(morse_list)