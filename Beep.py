filename_in = ''
filename_out = ''

while True:
    print("Hello. Welcome to Beep. This program reads from and writes to .bb files. If you choose to write, it will\n"
          "take any text file and convert it to a .bb file. If you choose to read, it will take any .bb file and\n"
          "translate it to a .txt file.")
    print("+------------------------------------------------------------------------------------------------------+")
    cmd = input('(Read|Write) -> ').upper()

    if cmd == 'READ':
        filename_in = input('File to translate -> ')


        filename_out = input('File to output translation -> ')


    elif cmd == 'WRITE':
        filename_in = input('File to encode -> ')


        filename_out = input('File to output encoding -> ')

    else:
        print('+------------------------------------------------------------------------------------------------------+\n'
              'Unknwon command. Exiting...')
        break