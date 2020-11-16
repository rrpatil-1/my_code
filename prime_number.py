n=int(input('enter last term of series:',))

for i in range(2,n+1,1):
     for j in range(2,i,1):
         if i%j==0:
              break
         j=j+1
 #if break part excuted then else part will not excute.
#so when if condition true else part will not exucate.
#if condition is only true when number  is even
 
     else:
         print(i,end=" ")
     i=i+1
