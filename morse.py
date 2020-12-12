import sys
table = {'a': ".-", 'b': "-...", 'c': "-.-.", 'd': "-..", 'e': ".", 'f': "..-.", 'g': "--.", 'h': "....", 'i': "..", 'j': ".---", 'k': "-.-", 'l': ".-..", 'm': "--", 'n': "-.", 'o': "---", 'p': ".--.", 'q': "--.-", 'r': ".-.",
         's': "...", 't': "-", 'u': "..-", 'v': "...-", 'w': ".--", 'x': "-..-", 'y': "-.--", 'z': "--..", '1': ".----", '2': "..---", '3': "...--", '4': "....-", '5': ".....", '6': "-....", '7': "--...", '8': "---..", '9': "----.", '0': "-----"}

prosigns = {"roger": ".-.", "over": "-.-", "out": ".-.-.", "closing": "-.-. .-..",
            "say again": "..--..", "affirmative": "-.-.", "correct": "-.-.", "negative": "-.", "nothing heard": "-. .. .-..", "wrong": "--.. .-- ..-.", "i acknowledge": "-.-. ..-. --"}


def is_prosign(string):
    return string.lower() in prosigns.keys() or string in prosigns.values()


def convert_long(string):
    chars = []
    for char in string:
        chars.append(char)
    for i in range(len(chars)):
        if(chars[i] in table.keys()):
            chars[i] = table[chars[i]]
    str2 = ""
    for char in chars:
        str2 += char
        str2 += " "
    return str2


def convert_condensed(string):
    chars = [char.lower() for char in string]
    chars = [table[chars[i]]
             for i in range(len(chars)) if chars[i] in table.keys()]
    return " ".join(chars)


def convert_prosign(string):
    return prosigns[string.lower()]


def convert(string):
    if(is_prosign(string)):
        return convert_prosign(string)
    else:
        return convert_condensed(string)


def revert_long(string):
    codes = string.split(" ")
    chars = []
    for code in codes:
        for char in table:
            if(code == table[char]):
                chars.append(char)
    return "".join(chars)


def revert_condensed(string):
    return "".join([char for code in string.split(" ") for char in table if code == table[char]])


def revert_prosign(string):
    for sign in prosigns:
        if(prosigns[sign] == string):
            return sign


def revert(string):
    if(is_prosign(string)):
        return revert_prosign(string)
    else:
        return revert_condensed(string)


def get_type(string):
    if(string[0] == '.' or string[0] == '-'):
        return "morse"
    return "normal"


def translate(string):
    if(len(string) == 0):
        return ""
    elif(get_type(string) == "morse"):
        return revert(string)
    else:
        return convert(string)


def get_arguments(args):  # [-t text -i inputfile -o outputfile]
    arg_map = {'-t': "", '-i': "", '-o': "output.txt"}
    for i in range(len(args) - 1):
        if(args[i] == '-t'):
            arg_map['-t'] = args[i + 1]
        elif(args[i] == '-i'):
            arg_map['-i'] = args[i + 1]
        elif(args[i] == '-o'):
            arg_map['-o'] = args[i + 1]
    return arg_map


def read_file(input_file):
    content = []
    with open(input_file, 'r') as file:
        for line in file:
            content.append(line)
    return content


def write_out(content, output_file):
    with open(output_file, 'w') as file:
        for text in content:
            file.write(text)
            file.write("\n")


def convert_file(input_file, output_file):
    content = read_file(input_file)
    changed = []
    for line in content:
        changed.append(translate(line.strip()))
    # print(changed)
    write_out(changed, output_file)


def main(argv):
    args = get_arguments(argv)
    if(args["-t"] != ""):
        print("Word given; translating!")
        print(translate(args["-t"]))
    if(args['-i'] != "" and args['-o'] != ""):
        print("Translating from file!")
        convert_file(args['-i'], args['-o'])
    if(len(argv) < 2):
        print("No word given; in interactive form!")
        while(True):
            try:
                string = input("Please input a string: ^C to stop: ")
                print(translate(string))
            except KeyboardInterrupt:
                print()
                print("Stopping!")
                break


main(sys.argv)
