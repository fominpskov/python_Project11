user_input = input("please enter someting")
print(type(user_input))

a = float(input("side A:"))
b = float(input("side B:"))
c = float(input("side C:"))

half_P = (a + b + c)/2
area = (half_P * (half_P - a)*(half_P - b)*(half_P -c))**0.5
print(area)
