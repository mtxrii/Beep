filename = ''

while True:
    print("Hello. Welcome to Beep. This program reads from and writes to .bb files. If you choose to write, it will\n"
          "take any text file and convert it to a .bb file. If you choose to read, it will take any text file and\n"
          "translate it to a .bb file.")
    print("+-------------------------------------+")
    cmd = input('(Read|Write) -> ').upper()

    if cmd == 'READ':
        print('Reading...')

    elif cmd == 'WRITE':
        filename = input('What file would you like to write to? -> ')

    else:
        print('Unknwon command. Exiting...')
        break