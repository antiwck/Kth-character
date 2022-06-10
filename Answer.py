string=input()
dict={}
for index in string:
    if index not in dict:
        dict[index] = None 
strings=[]
for i in dict:
    strings.append(string.replace(i, ''))
print(min(strings))
