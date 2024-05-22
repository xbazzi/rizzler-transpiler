from lex import *
from parse import *
from emit import *
import sys

def main():
    print("*****Rizzler Compiler*****")

    if len(sys.argv) != 2:
        sys.exit("Error: Compiler needs a source file as argument")
    with open(sys.argv[1], 'r') as inputFile:
        source = inputFile.read()
    
    # Initialize the lexer, emitter, and parser.
    lexer = Lexer(source)
    emitter = Emitter("out.c")
    parser = Parser(lexer, emitter)

    parser.program() # Start the parser
    emitter.writeFile() #Write the output to file
    print("Compiling complete no cap.")

main()