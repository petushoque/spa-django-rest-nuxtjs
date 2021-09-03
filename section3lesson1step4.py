# решение с подключением дополнительной библиотеки

import roman;
s = input()
print(roman.fromRoman(s))

# готовая функция для перевода

def romanToInt(s):
        result=0
        f={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        i=0
        while i < len(s)-1:
                if f[s[i+1]] > f[s[i]]:
                        result+=f[s[i+1]]-f[s[i]]
                        i+=2
                else:
                        result+=f[s[i]]
                        i+=1
        if i<len(s):
                result+=f[s[len(s)-1]]
        return result

print(romanToInt('III'))