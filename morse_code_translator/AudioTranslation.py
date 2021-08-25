import speech_recognition as sr
import TextTranslation as tt

# audio_file -> path to the audio file that will be translated
# lang -> language code that represented in audio file (en-US default) 
# (supported languages: https://cloud.google.com/speech-to-text/docs/languages)
# returns morse code as text from audio
def translate(audio_file, lang="en-US"):
    recog = sr.Recognizer()
    file = sr.AudioFile(audio_file)

    recog.energy_threshold = 300
    with file as source:
        processed_audio = recog.record(source)

    audio_text = recog.recognize_google(audio_data=processed_audio, language=lang)
    return tt.text_to_morse(audio_text)