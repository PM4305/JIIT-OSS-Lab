def func(s1,s2):
    string1=""
    string2=""
    i=0
    j=0
    while i<len(s1):
        if s1[i]==s2[j]:
            i+=1
            j+=1
            string1+=s1[i]
        else:
            string2+=s1[i]
            string2+=s2[j]
            j+=1
    
    print(string1,string2)
s1="Refer"
s2="Regfree"
func(s1,s2)