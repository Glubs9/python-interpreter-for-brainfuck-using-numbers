import sys

def lexer(data):
    data = list(data)
    tokens = []
    for char in data:
        if char == ">" or char == "<" or char == "+" or char == "-" or char == "/" or char == "." or char == "," or char == "[" or char == "]":
            #this is a really big if statement, if there is some way to make it smaller that i find out i will change it.
            tokens.append(char)
    return tokens

def interp(tokens):
    tape = [0]
    pos = 0 #this is the position on the tape
    n = 0 #this is used to iterate through the tokens

    while n < len(tokens):
        
        if tokens[n] == ">":
            if pos + 1 >= len(tape):
                tape.append(0)
                pos += 1
            else:
                pos += 1
        elif tokens[n] == "<":
            if pos - 1 < 0:
                print("at token " + str(n) + " tried to go below 0th place on the tape")
                exit()
            else:
                pos -= 1
        elif tokens[n] == "+":
            tape[pos] += 1
        elif tokens[n] == "-":
            tape[pos] -= 1
        elif tokens[n] == ".":
            print(tape[pos])
        elif tokens[n] == ",":
            tape[pos] = int(input("enter the number for tape place " + str(pos) + ": "))
        elif tokens[n] == "[":
            #should probably add some sorta max loop amount
            if tape[pos] == 0:
                numofbrackets = 1
                n += 1
                while numofbrackets != 0:
                    if tokens[n] == "[":
                        numofbrackets += 1
                    elif tokens[n] == "]":
                        numofbrackets -= 1
                    n += 1 
        elif tokens[n] == "]":
            if tape[pos] != 0:
                numofbrackets = 1
                n -= 1
                while numofbrackets != 0:
                    if tokens[n] == "[":
                        numofbrackets -= 1
                    elif tokens[n] == "]":
                        numofbrackets += 1
                    n -= 1
        n += 1
        #note, there are no switch statements in python as far as i know

def main():
    tokens = lexer(open(sys.argv[1], "r").read())
    #i decided not to go with a parser since an ast would be overkill for bf
    interp(tokens)

main()
#todo
#add comments/documentation
