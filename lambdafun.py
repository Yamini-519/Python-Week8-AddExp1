greet=lambda:print("yamini")
greet()
s1="yamini mulagapaka"
s2=lambda x:x.upper()
print("convert lower to upper:",s2(s1))
add=lambda a,b:a+b
print("add:",add(2,3))
add=lambda a:a+10
print("add:",add(5))
add=lambda a,b,c:a+b+c
print("add:",add(5,6,7))
n=lambda x:"positive" if x>0 else "negative" if x<0 else "zero"
print("check value is postive or negative:",n(5))
print(n(-1))
print(n(0))
square=lambda x:x*x
print("sqare of x:",square(5))
max_val=lambda a,b :a if a>b else b
print("max of a and b:",max_val(10,20))
