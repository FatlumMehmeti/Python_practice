#Write a function that takes a list of numbers and returns their average.
def avg(a:object):
    sum =0
    for i in a:
        sum+=i
    return sum/len(a)
#print(avg([1,3,5,6,8,9,7,5,2,3]))
#Write a function that takes a string and returns a dictionary showing the count of each character in the string.
def chardi(s:str):
    di={}
    for i in s:
        if i in di:
            di[i]+=1
        else:
            di[i]=1
    return di
#print(chardi("o you got this now what is you"))                        
#Write a function that merges two lists into a dictionary (first list = keys, second list = values).
def merge(li:object,li2:object):
    dic={}
    if len(li)!=len(li2):
        print("The lenght it's not the same")
    for i in range(len(li)):
        dic[li[i]]=li2[i]
    return dic
print(merge(['1','gfg','fdfd','4585'],[1,22,5,8]))
#Write a function that removes duplicate elements from a list.
def rm_dup(l:object):
    t=[]
    for i in l:
        if i not in t:
            t.append(i)
    return t
print(rm_dup([1,1,2,2,3,5,6,6,8,9,7,7]))        

#Write a function that checks if a given word is a palindrome.
def palindrom(s:str):
    inv=s[::-1]
    return s.lower()==inv.lower()
print(palindrom("Noon"))
