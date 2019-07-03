ar =int(input())
if (ar>1):   
   for i in range(2, ar//2):   
       if (ar %i) == 0: 
           print("no")
           break
   else: 
       print("yes") 
else: 
   print("no")
