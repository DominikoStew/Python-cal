
def separator():
    print("-------------")
    print("")


print("Hello Python!")

# data types

name = "Dominique "
age = 27
found = True
average = 123.389

print(name)
print(age)
print(average)

# alg opeartions
print(age - 10)
print(21 * 2)
print(100 / 3)
print(100 % 3)  # modulus operator (return the residiue of the division)


separator()


print(name + name)
print(name + str(age))

if(age < 80):
    print("You are still a young man!")
    print("this is inside the if")

elif(age == 80):
    print("You are on the border line")

else:
    print("You are getting old")

separator()  # execute the function
