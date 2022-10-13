plaintext=""
ciphertext=input("I will read your input: ")
alphabet="XYZABCDEFGHIJKLMNOPQRSTUVWXYZABC"
ciphertextposition=0
while ciphertextposition < len(ciphertext):
    ciphertextChar=ciphertext[ciphertextposition]
    alphabetposition=3
    while (ciphertextChar != alphabet[alphabetposition]):
        alphabetposition+=1
    plaintext=(plaintext + alphabet[alphabetposition + 3])
    ciphertextposition+=1
print("THIS IS YOUR DECRYPTED VERSION: " + plaintext)
