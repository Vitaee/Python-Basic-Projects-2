word = input("Enter the word to encrypt: ")
pas = ""
for k in word:
    print(ord(k))
    print(k,"== " , chr(ord(k) + 3))
    pas = pas + chr(ord(k) + 3)
    print(pas)
print(word, "== " ,pas)    

word1 = input("Enter the word to be decrypted: ")
pas1 = word
for k in word1:
    print(k,"=> ", chr(ord(k) - 3))
    mword1 = word1 + chr(ord(k) - 3)
print(word, " => ",word1) 