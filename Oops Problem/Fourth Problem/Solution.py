string1=input()
string2=input()
flag=True
for word in string1.split():
    for ch in word:
        if ch.lower() not in string2:
            flag=False
            break
    
                
if flag:
    print("Input string is valid")
    print(string1)
else:
    print("Input string is not valid")
    print(string1) 



        