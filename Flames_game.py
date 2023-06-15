import time
print('Entering in Flames Game...  ')
time.sleep(2)
other_name=input('Enter your other name  ')
your_name=input('Enter your name  ')
other_list=list(other_name)
your_list=list(your_name)

i=0
c=0
while i< len(other_list):
    for j in your_list:
        if other_list[i]==j:
            your_list.remove(j)
            c=c+1
    i=i+1

total_length=len(your_list) + len(other_list) - (c)
print('total length ', total_length)


res = ["Friends", "Lovers", "Affectionate", "Marriage", "Enemies", "Siblings"]  
  
while len(res) > 1 :  
        splitIndex = (total_length % len(res) - 1)  
        if splitIndex >= 0 :  
            right = res[splitIndex + 1 : ]  
            left = res[ : splitIndex]  
            res = right + left  
        else :  
            res = res[ : len(res) - 1]  
print("Relationship Status :", res[0])  


