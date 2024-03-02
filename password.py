s=input("Enter the password:\n")
if len(s)>=8:
    c="[!@#$%^&*()_]"
    if " " in s:
            print("invalid space")
            exit(0)
    countu=countl=countd=countc=0
    for ele in s:
        if ele.isupper():
            countu +=1
        elif ele.islower():
            countl +=1
        elif ele.isdigit():
            countd +=1
        elif any(c[i] in s for i in range(len(c))):
            countc +=1
        else:
            print("invalid character")
            exit(0)
    if countu>=1 and countl>=1 and countd>=1 and countc>=1:
        print("valid")
    else:
        print("invalid insufficiency")