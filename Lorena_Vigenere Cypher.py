#First things first is to make a function on how our program will encrypt the message using the def method
def encr(message, key):
  # In our function, we will make use of the len method to find the length of the keyword given by the user
    klen = len(key)
    # Next is to make use of the ord(i) method which will return the string input of our message and key into each character's unicode
    kord = [ord(i) for i in key]
    mesord = [ord(i) for i in message]
    # Then, we will create a new variable which will contain an empty quotation as it will be returned by the next method
    enc = ''
    # In this part, we made use of the for method which will use the length of unicode of the message
    for i in range(len(mesord)):
      # Here, we create a new variable which is based upon the formula of the cipher, (message + key) % 26
        x = (mesord[i] + kord[i % klen]) % 26
        # Another variable is added with the append operator and the chr function which will basically convert the given integers to strings with the number 65 added because chr(65) is "A" as "A" is the first letter of the alphabet
        enc += chr(x + 65)
        #Finally, the result will be kept on our "empty" variable.
    return enc

# The last step is to use the if __name__ == "__main__" method in python to run the program not as a module but as a script.
if __name__ == "__main__":
  # We will then make a program that will ask the user for the message and key then make use of the function we made and then print the overall encrypted message.
  message = input("Enter your message in ALL CAPS: ")
  key = input("Enter your keyword in ALL CAPS: ")
  #Now we will use the function that we used earlier.
  encryptedoutput = encr(message,key) 
  print(encryptedoutput) 
