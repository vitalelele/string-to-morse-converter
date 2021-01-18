morse_code_alphabet = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
normal_alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]



def convert(string_to_code):
    morse = ""
    for char in string_to_code:
        if char != " ":
            index_alph = normal_alphabet.index(char)
            morse = morse + f"{morse_code_alphabet[index_alph]} "

    return morse

def decode(morse):
    normal_phrase = ""
    morse = morse.split()
    for char in morse:
            index_alph = morse_code_alphabet.index(char)
            normal_phrase = normal_phrase + f"{normal_alphabet[index_alph]}"
    
    return normal_phrase.lower()

def main():
    flag = False
    while not flag:
        choose = int(input("1.Code a string\n2.Decode a morse code string (using . and -)\nChoose: "))
        if choose == 1:
            string_tocode = input("Give a string you want to convert: ").upper()
            print(convert(string_tocode))
        elif choose == 2:
            string_todecode = input("Give a string you want to decode in format . and - : ")
            print(decode(string_todecode))
        else:
            print("Typed something wrong.")

main()