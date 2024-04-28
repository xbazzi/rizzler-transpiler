from lex import *
from parse import *

def main():
    print("BlueCollar Compiler")

    if len(sys.argv) != 2:
        sys.exit("Error: Compiler needs a source file as argument")
    with open(sys.argv[1], 'r') as inputFile:
        source = inputFile.read()
    
    # Initialize the lexer and parser.
    lexer = Lexer(source)
    parser = Parser(lexer)
    parser.program()
    print("Parsing complete.")

main()