"""
a = 'СЛОВО'
print(a)
b = list(a)
b[2] = "\033[31m{}".format(b[2])
b[3] = "\033[0m{}".format(b[3])
c = ''.join(b)
print(c)
"""
a = "СЛОВО"
print(a)
a_l = list(a)
word = input()
word = word.upper()
word_l = list(word)

if word_l[0] == a_l[0]:
    word_l[0] = "\033[32m{}\033[0m".format(word_l[0])
elif word_l[0] in a_l:
    word_l[0] = "\033[33m{}\033[0m".format(word_l[0])

if word_l[1] == a_l[1]:
    word_l[1] = "\033[32m{}\033[0m".format(word_l[1])
elif word_l[1] in a_l:
    word_l[1] = "\033[33m{}\033[0m".format(word_l[1])

if word_l[2] == a_l[2]:
    word_l[2] = "\033[32m{}\033[0m".format(word_l[2])
elif word_l[2] in a_l:
    word_l[2] = "\033[33m{}\033[0m".format(word_l[2])

if word_l[3] == a_l[3]:
    word_l[3] = "\033[32m{}\033[0m".format(word_l[3])
elif word_l[3] in a_l:
    word_l[3] = "\033[33m{}\033[0m".format(word_l[3])

if word_l[4] == a_l[4]:
    word_l[4] = "\033[32m{}\033[0m".format(word_l[4])
elif word_l[4] in a_l:
    word_l[4] = "\033[33m{}\033[0m".format(word_l[4])

full_word = ''.join(word_l)
#print(word_l_s)
#print(word_l[0])
print(full_word)