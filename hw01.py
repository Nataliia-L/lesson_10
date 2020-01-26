import string
step = 4
keys = list(string.ascii_lowercase) 
values = list(string.ascii_lowercase[step:] + string.ascii_lowercase[:step]) 
d = dict (zip(keys, values))
enc = ''
s = input ('Введите строку, пожалуйста. ')
while len (s)<2:
    s = input ('Введите строку, пожалуйста. ')
for lit in s:
    enc = enc+d[lit]
print ('Зашифрованное слово: ', enc)
