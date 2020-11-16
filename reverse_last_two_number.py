n=int(input("enter number=",))
#lets take number=12345
l=len(str(n))#conver in to string to use it in loop


a=n%10  #a=12345%10=5
b=n//10 #b=12345//10=1234
c=b%10  #c=1234%10=4

 
print(a,end="") #a=5
print(c,end="") #c=4
 
#beacuse of end output be like 54

#now by using loop print remaining character 
for i in range(1,l-1,1):
          print(i,end="")
          
#output be like 54123

