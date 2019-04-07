import sys
script, input_encoding, error = sys.argv
#sets these files equal, same as doing this
#script = sys.argv[0] (0 is always script)
#input_encoding = sys.argv[1] (is the first argument you type when running)
#error = sys.argv[2] (is the second arg you type when running)


#main is just the name of the function
def main(language_file, encoding, errors):#these var names mean nothing, just place holders,could be a, b, c
    line = language_file.readline() #find line x and read it

    if line: #this is sort of like a true or false statement
        print_line(line, encoding, errors) #if line, run print_line(def below)
        return main(language_file, encoding, errors) #this tells the program to run again from the start,to repeat until done with all data


def print_line(line, encoding ,errors):
    next_lang = line.strip() #python understands things like strip or endcode from the functs of what ever class the object is in, called methods
    raw_bytes = next_lang.encode(encoding, errors=errors)
    cooked_string = raw_bytes.decode(encoding, errors=errors)

    print(raw_bytes, "<===>", cooked_string)


languages = open("languages.txt", encoding="utf-8")

main(languages, input_encoding, error) #this tells the program to actually run your function
