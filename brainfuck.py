import sys #this is for the exit function when an error occurs and for getting command line arguments
import re #this is for the replacement in the lexer to ignore all non bf characters

def lexer(data):
    #this just finds all non-acceptable characters and ignores them because thats how comments work in bf.
    return list(re.sub(r"[^><+-/.,\[\]]", "", data)) #re.sub replaces the characters and list makes the string returned into a list
    #the first argument in re.sub is the regular expression, the second is what to replace it with and the third is the string to use

def interp(tokens):
    #tokens is a list of instructions
    tape = [0] #this is the tape of numbers manipulated in the program
    pos = 0 #this is the position on the tape
    n = 0 #this is used to iterate through the tokens and is the token number

    while n < len(tokens):
        
        if tokens[n] == ">":
            if pos + 1 >= len(tape):
                tape.append(0) #this is just in case the users program goes beyond the tapes length it extends it
            pos += 1
        elif tokens[n] == "<":
            if pos - 1 < 0:
                tape.insert(0, 0) #this is just in case the users program goes backwards beyond the tapes length it then extends it
                #since it is moving the whole list one to the right (>>) and the position doesn't go with it the position doesn't have to be changed
            else:
                pos -= 1 
        elif tokens[n] == "+":
            tape[pos] += 1 #this is not the position but the item at that index
        elif tokens[n] == "-":
            tape[pos] -= 1 #see 2 lines above
        elif tokens[n] == ".":
            print(tape[pos]) #see 2 lines above
        elif tokens[n] == ",":
            tape[pos] = int(input("enter the number for tape place " + str(pos) + ": "))
        elif tokens[n] == "[":
            if tape[pos] == 0:
                #this will skip until this brackets closing bracket if the current index is 0
                numofbrackets = 1  #this is the number of brackets needed to find the closing one
                n += 1 #n is the position and this is the global n for the tokens and it changes that instead of having a temporary variable
                while numofbrackets != 0:
                    #while the current number of needed brackets is still not satisified
                    if n >= len(tokens):
                        print("closing bracket not found")
                        exit() #closes the program
                    elif tokens[n] == "[":
                        numofbrackets += 1
                    elif tokens[n] == "]":
                        numofbrackets -= 1
                    n += 1 #moves the tokens index forward one
                n -= 1 # this is because the loop automatically adds one to the position at the end so normally it goes one too many tokens across
                
        elif tokens[n] == "]":
            #this is pretty much the same as the previous bracket except
            if tape[pos] != 0:
                #the loop will go backward if the current index is not 0
                numofbrackets = 1
                n -= 1
                while numofbrackets != 0:
                    if n < 0:
                        print("opening bracket not found")
                        exit()
                    if tokens[n] == "[":
                        numofbrackets -= 1
                    elif tokens[n] == "]":
                        numofbrackets += 1
                    n -= 1 # this goes backward thorugh the tokens until the openning brackets are found
                    
        n += 1 #this is used to advance to the next position in the tokens list
        
interp(lexer(open(sys.argv[1], "r").read()))
#this opens up the file from the name passed as a parameter and gets its contents as a string with the open(sys.argv[1], "r").read()
#it then removes all non bf characters, so that people can use comments in their files, and makes the string input a list using the lexer function
#it then runs through that list and runs all of the commands that it was told to do by the file with the interp function
