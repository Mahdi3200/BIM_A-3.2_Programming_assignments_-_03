# Enter the number of points you need
n = int(input("Enter the number of points you need"))

# Store coordinates
x = []
y = []

# Input coordinates
for i in range(0, n):
    inputx = (int(input("enter x")))
    x.append(inputx)
    inputy = (int(input("enter y")))
    y.append(inputy)
    

# Print coordinates
for i in range(0, n):
        print("point", i+1, ":", x[i], y[i])

# store individual areas
lax = []
for i in range (0, n-1):
        ax = (x[i+1]+x[i]) * (y[i+1]-y[i])
        lax.append(ax)   
tax = 0.5*sum(lax)
print(n)
print(x)
print(y)
print(F"ax: {tax:.2F}")
lax = []
for i in range (0, n-1):
    sx = (x[i+1]-x[i]) * (y[i+1]**2+y[i]*y[i+1]+y[i]**2)
    lax.append(sx)
tsx = (-1/6)*sum(lax)
print(F"Sx: {tsx:.2F}")
lax = []
for i in range (0, n-1):
    sy = (y[i+1]-y[i]) * (x[i+1]**2+x[i]*x[i+1]+x[i]**2)
    lax.append(sy)
tsy = (1/6)*sum(lax)
print(F"Sy: {tsy:.2F}")
lax = []
for i in range (0, n-1):
    ix = (x[i+1]-x[i]) * (y[i+1]**3+y[i]*y[i+1]**2+y[i]**2*y[i+1]+y[i]**3)
    lax.append(ix)
tix = (-1/12)*sum(lax)
print(F"ix: {tix:.2F}")
lax = []
for i in range (0, n-1):
    iy = (y[i+1]-y[i]) * (x[i+1]**3+x[i]*x[i+1]**2+x[i]**2*x[i+1]+x[i]**3)
    lax.append(iy)
tiy = (1/12)*sum(lax)
print(F"iy: {tiy:.2F}")
lax = []
for i in range (0, n-1):
    ixy = (y[i+1]-y[i])*((y[i+1]*(3*x[i+1]**2+2*x[i+1]*x[i]+x[i]**2))+(y[i]*(3*x[i]**2+2*x[i+1]*x[i]+x[i+1]**2)))
    lax.append(ixy)
tixy = (-1/24)*sum(lax)
print(F"ixy: {tixy:.2F}")
lax = []
for i in range (0, n-1):
    xt =(tsy/tax)
    lax.append(xt)
txt = (tsy/tax)
print(F"xt: {txt:.2F}")
lax = []
for i in range (0, n-1):
    yt =(tsx/tax)
    lax.append(yt)
tyt = (tsx/tax)
print(F"yt: {tyt:.2F}")
for i in range (0, n-1):
    ixt =(tix)-(tyt**2*tax)
    lax.append(ixt)
print(F"ixt: {ixt:.2F}")
for i in range (0, n-1):
    iyt =(tiy)-(txt**2*tax)
    lax.append(iyt)
print(F"iyt: {iyt:.2F}")
for i in range (0, n-1):
    ixyt =(tixy)+(txt*tyt*tax)
    lax.append(ixyt)
print(F"ixyt: {ixyt:.2F}")

    


