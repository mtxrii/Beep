import sys

from .Keys import txt_to_beep
from .Keys import beep_to_txt

separator = '+------------------------------------------------------------------------------------------------------+'
filename_in = ''
filename_out = ''

# Returns an iterable of every line, decoded in a file
# Params:
#   file - file to be read
#   bb - whether file is of type .bb
def decoded(file, bb=False):
    opened_file = None
    try:
        opened_file = open(file, 'r')
    except IOError:
        sys.exit("[Error]: '" + file + "' could not be found. Exiting...")

    if bb:
        for line in opened_file:
            prepared = ''
            for word in line.split('|'):
                for char in word.split(','):
                    char = char.strip()
                    if char in beep_to_txt.keys():
                        prepared += beep_to_txt[char]
                    else:
                        prepared += char
                prepared += ' '
            yield prepared

    else:
        for line in opened_file:
            prepared = ''
            for char in line:
                if char == ' ':
                    prepared += ' | '
                elif char in txt_to_beep.keys():
                    prepared += txt_to_beep[char] + ', '
                else:
                    prepared += char
            yield prepared

    opened_file.close()

while True:
    print("Hello. Welcome to Beep. This program reads from and writes to .bb files. If you choose to write, it will\n"
          "take any text file and convert it to a .bb file. If you choose to read, it will take any .bb file and\n"
          "translate it to a .txt file.")
    print(separator)
    cmd = input('(Read|Write) -> ').upper()

    if cmd == 'READ':
        filename_in = input('File to translate -> ')
        filename_out = input('File to output translation -> ')

        print('\n Decoding file...')
        with open(filename_out, 'w') as out:
            for line in decoded(filename_in, bb=True):
                out.write(line)
            out.write('\n')

        print(separator + "\nDone! Check out '" + filename_out + "'")
        break

    elif cmd == 'WRITE':
        filename_in = input('File to encode -> ')
        filename_out = input('File to output encoding -> ')
        break

    else:
        print(separator + '\n[Error]: Unknwon command. Exiting...')
        break