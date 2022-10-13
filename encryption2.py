plaintext=input("I will read your input: ")
ciphertext=""
plaintextposition = 0
while(plaintextposition < len(plaintext)):
    plaintextChar = plaintext[plaintextposition]
    ASCII_Value= ord(plaintextChar)
    ciphertext = ciphertext + chr(ASCII_Value-3) 
    plaintextposition += 1
print(ciphertext)

