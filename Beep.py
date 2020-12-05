while True:
    print("Hello. Welcome to Beep. Read or write?")
    print("+-------------------------------------+")
    cmd = input('(Read|Write) -> ').upper()

    if cmd == 'READ':
        print('Reading...')

    elif cmd == 'WRITE':
        print('Writing...')

    else:
        print('Unknwon command. Exiting...')
        break