a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = int(input("Enter the value of c: "))

d = (b**2) - (4*a*c)

if d <  0 :
    print("There are no real roots")

elif d == 0 :
    root = (-b)/(2*a)
    print("The root of the equation is ",root)

else :
    root1 = (-b + d**0.5) / (2*a)
    root2 = (-b - d**0.5) / (2*a)
    print("The roots of the quadratic equation are", root1, "and", root2)
