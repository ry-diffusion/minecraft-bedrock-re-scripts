with open('ggames3.png', 'rb') as img:
    payload = img.read()
    print('read payload')
    with open('libminecraftpe.so', 'rb+') as file:
        file.seek(0xd97bb47)
        file.write(payload)
        print('wrotten payload')
