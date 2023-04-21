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
    message = input("Enter your message in ALL CAPS: ")
    key = input("Enter your keyword in ALL CAPS: ")
    encryptedoutput = encr(message,key) 
    print(encryptedoutput) 

