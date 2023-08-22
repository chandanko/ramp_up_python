S=input("Enter string -> ")
print( S)
count=0
for i in S:
    count+=1
print(f" {count} characters present in the string")

Dup_char=""
Dup_char_count=0
for j in S:
    if j not in Dup_char:
        Dup_char+=j
    else:
        Dup_char_count+=1
print(f" The duplicate characters present in the string are {Dup_char_count}")

S1=""
for i in S[::-1]:
    S1+=i
print(f" The reverse of charectors ->  {S1}")

# S=input("Enter a string -> ")
S1=S.split()
print(S1)
count=0
for i in S1:
    count+=1
print(f" The number of words present in a sentence is {count}")

S2=[]
Dup_words=0
for k in S1:
    if k not in S2:
        S2.append(k)
    else:
        Dup_words+=1
print(f" Number of duplicate words present in the sentence are {Dup_words}")

S3=[]
for j in S1[::-1]:
    S3.append(j)

print(f" The reverse order of sentense is {S3}")

S4=" ".join(S3)
print(f" The new statement fron reverse order is {S4}")

S5=[]
for i in S3:
    if i not in S5:
        S5.append(i)
    else:
        pass
print(f"The sentence after removing duplicate words - > {S5}")
print("The final latest string statement is -> ", " ".join(S5))

S6=" ".join(S5)
Dup_char2=""
for i in S6:
    if i not in Dup_char2:
        Dup_char2+=i
    elif i==" ":
        Dup_char2+=i
    else:
        pass
print(f" The sentence after removal of duplicate characters in latest string is -> {Dup_char2}")

