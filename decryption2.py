plaintext=input("I will read your input: ")
ciphertext=""
plaintextposition=0
while (plaintextposition < len(plaintext)):
    ASCII_Value=ord(plaintext[plaintextposition])
    ciphertext=ciphertext + chr(ASCII_Value+3)
    plaintextposition += 1

print("THIS IS YOUR ENCRYPTED VERSION: " + ciphertext)
