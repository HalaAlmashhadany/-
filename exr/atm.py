def balance(request , cons):
    j=request/cons
    if j>0 :
       s=0
       while s<j:
          print "give ",cons
          request-=cons
          s+=1
    return request
request0=390
x=balance(request0,100)
x=balance(x,50)
x=balance(x,10)
x=balance(x,5)
x=balance(x ,2)


