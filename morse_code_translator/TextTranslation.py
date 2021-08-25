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

__REVERSE_DICT = {k:v for v, k in __MORSE_CODE_DICT.items()}

# text -> text will be translated to morse code
# returns morse code as string
def text_to_morse(text):
    morse_list = [__MORSE_CODE_DICT.get(ch) for ch in text.upper()]
    return ' '.join(morse_list)

# morse -> morse will be translated to text
# returns text as string
def morse_to_text(morse):
    word_morse_list = morse.split("   ")
    word_text_list = []

    for morse_word in word_morse_list:
        text_word = [__REVERSE_DICT.get(ch) for ch in morse_word.split()]
        word_text_list.append(''.join(text_word))

    return ' '.join(word_text_list)