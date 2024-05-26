from lex import *
from parse import *
from emit import *
import sys

def main():
    print("*****Rizzler Compiler*****")

    if len(sys.argv) != 2:
        sys.exit("Error: Bro really forgot the input file, cope + L.")
    with open(sys.argv[1], 'r') as inputFile:
        source = inputFile.read()
    
    # Initialize the lexer, emitter, and parser.
    lexer = Lexer(source)
    outfile = sys.argv[1].split(".")
    emitter = Emitter(outfile[0] + ".c")
    parser = Parser(lexer, emitter)

    parser.program() # Start the parser
    emitter.writeFile() #Write the output to file
    print("Ws in the chat. We just compiled fr fr.")

main()