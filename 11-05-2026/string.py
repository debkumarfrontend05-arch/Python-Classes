a = 'D';
print(ord(a)); #letter to Unicode


d = 68;
print(chr(d)); #Unicode to letter

name = 'Debkumar Mondal';
print(name[1])

b = "Debkumar Mondal";
print(b[9::1])


#Type Conversion

# c = 12;
# c = str(c);

# print(type(c));


c = '12';
c = int(c);
print(type(c));


# fasly Values
# False
# 0
# 0.0
# ""
# []
# ()
# {}

# remaining all are truthy value


name = "Debkumar Mondal"
age = 26;

# print("My name is ",name, "My age is ",age);
# print(f"my name is {name} and my age is {age}");

newAge = int(input("Hello what is your age"));
print(f"My age is {newAge}");
print(type(newAge))