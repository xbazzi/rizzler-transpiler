# Rizzler
A simple transpiler written in Python for an internet slang language, taken from Austin Henley's <a href="https://austinhenley.com/blog/teenytinycompiler1.html">Teeny Tiny Compiler project</a>. The output is C code, which needs to be further compiled into assembly code (I know...).

![figuring out computers](transpiler.png "Rizzlers")

Check out the  [example](example/) directory for a (bitter) taste of the language.

Usage:
```
$ python3 rizzler.py <file>.rizz
$ gcc out.c -o <whatever>
$ ./<whatever>
```
## TODO list
 - Spit the C file with the same name as the .rizz file
 - Replace all keywords with brainrot Ohio gyatt rizz
 - Add code formatting for C output
 - Automate compilation with bash script (all my homies hate cross-platform)
 - Add an AST for intermediate representation and optimizations