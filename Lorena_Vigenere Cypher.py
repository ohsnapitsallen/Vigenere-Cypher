def encr(message, key):
    klen = len(key)
    kord = [ord(i) for i in key]
    mesord = [ord(i) for i in message]
    enc = ''
        for i in range(len(mesord)):
        x = (mesord[i] + kord[i % klen]) % 26
        enc += chr(x + 65)
    return enc

if __name__ == "__main__":
