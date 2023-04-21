def encr(message, key):
    klen = len(key)
    kord = [ord(i) for i in key]
    mesord = [ord(i) for i in message]
