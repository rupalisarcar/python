print("Hello World")
print ("This is a sample python script.\n And this is a new line")
print ("This is a sample python script.\nnow And this is a new line")
print ("This is a sample python script.\\ And this is a new line")
print ("This is a sample python's script And this is a new line")
print ('This is a sample python\'s script And this "is" a new line')
print ("This is a sample python\'s script And this \"is\" a new line")
print ("This is a sample python's script \t And this  a new line")



''' by default print function will print the output in new line but if you want to print the output in same line then you can use end parameter of print function. By default end parameter is set to \n which means new line. If you want to print the output in same line then you can set end parameter to empty string or space. '''

print ("This is a sample python's script", "And this is a new line", 5)
print ("This is a sample python's script")
print("And this is a new line")



print ("This is a sample python's script", "And this is a new line", 5, sep=", ")
print ("This is a sample python's script", end=". ")
print("And this is a new line")


