intro = input("Introduce Yourself: ")
characterCount = 0
wordCount = 1

for i in intro:
    characterCount=characterCount+1
    #print(characterCount)
    if(i==' '):
        wordCount+=1

print("Number of Words in the string: ", wordCount)
print("Number of charachters in the string: ", characterCount)