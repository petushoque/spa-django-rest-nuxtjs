# Дана строка. Найдите в ней все глассные и разверни их в обратную строну.
word = input()
print(word)

vowels = ['a', 'e', 'i', 'o', 'u', 'y']

vowels_in_word = []
result = []
counter = -1

for i in range(len(word)):
    if word[i] in vowels:
        vowels_in_word.append(word[i])
        
print(vowels_in_word)

for i in range(len(word)):
    if word[i] not in vowels:
        result.append(word[i])
    else:
        result.append(vowels_in_word[counter])
        counter -= 1
        
print(result)