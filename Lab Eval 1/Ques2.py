def rever(s):
    s2=s.split()
    l=[]
    for i in s2:
        l.append(i[::-1])
    return " ".join(l)
s1="ViDeo SurVeiLLance SyStems"
print(rever(s1))