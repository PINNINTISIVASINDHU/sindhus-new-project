f = 0 # first no in fibonaci series 
s = 1 # second no in fibonacci series
n = int(input("enter range for fibonacci series:"))
if n<=0:
   print("sry !u can't access fibonacci series")
else:
   print(f)
   print(s)
   for i in range(0,n-2):    # cause i had already printed first two no's in fibonacci series
       next = f + s          # here next indicates the next value in fibonacci series
       print(next)
       f = s
       s = next
   
