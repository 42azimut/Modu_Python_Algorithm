def palindroms(s):
    i = 0
    j = len(s) - 1
    while (i < j):
        if s[i].isalpha() == False:
            i += 1
        elif s[j].isalpha() == False:
            j -= 1
        elif s[i].lower() != s[j].lower():
            return False
        else:
            i += 1
            j -= 1
    return True

print(palindroms("Wow"))
print(palindroms("Madam, I'm Adam."))
print(palindroms("Madam, I am Adam.")) 

