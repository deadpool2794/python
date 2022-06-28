word = input()
wordsList = list(word)
i, j = 0, len(wordsList)-1
vowelArray = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
while i< j:
    while wordsList[i] not in vowelArray and i< j:
        i += 1
    while wordsList[j] not in vowelArray and i < j:
        j -= 1
    
    if i < j:
        temp = wordsList[i]
        wordsList[i] = wordsList[j]
        wordsList[j] = temp
        i += 1
        j -= 1
print(''.join(wordsList))

