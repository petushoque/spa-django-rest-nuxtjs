# Предположим вы пишите требование о выкупе ransomNote из вырезанных букв из журнала magazine. Верни True, если из вырезанных букв из журнала можно составить записку о выкупе. Учти, каждую букву из журнала можно использовать только 1 раз.
ransomNote = input()
print(ransomNote)
magazine = input()
print(magazine)

for i in range(len(ransomNote)):
    # Если буква в журнале есть, вырезаем ее
    if magazine.find(ransomNote[i]) != -1:
        magazine = magazine.replace(ransomNote[i], '', 1)
    # Если нужной буквы не нашлось, заканчиваем цикл
    else:
        
print(magazine)