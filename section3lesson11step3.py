# Дана строка. Найдите в ней все глассные и разверни их в обратную строну.
word = input()
print(word)

vowels = ['a', 'e', 'i', 'o', 'u', 'y']

vowels_in_word = []

for i in range(len(word)):
    if word[i] in vowels:
        vowels_in_word.append(word[i])
        
print(vowels_in_word)
