f1 = lambda x:x+1
f2 = lambda x:x**2
f3=lambda x,y:lambda x:3+y(4)+f1(3)
print(f3(f1,f2)(3))