plaintext=input("I will read your input: ")
ciphertext=""
alphabet="XYZABCDEFGHIJKLMNOPQRSTUVWXYZABC"
plaintextposition=0
while plaintextposition < len(plaintext):
    plaintextChar=plaintext[plaintextposition]
    alphabetposition=3
    while (plaintextChar != alphabet[alphabetposition]):
        alphabetposition+=1
    ciphertext=(ciphertext + alphabet[alphabetposition - 3])
    plaintextposition+=1
print("THIS IS YOUR ENCRYPTED VERSION: " + ciphertext)
