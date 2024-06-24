a="notinterested"
print(a[0])
print(a[1])
print(a[2])
print(a[5])

for character in a:
  print(character)

names= "John,Doe"
print(names[0:4])
print(len(names))
print(names[:4])
print(names[0:-2])
print(names[0:len(names)-2])
print(names[-1:len(names)-2])
print(names[:])

# Strings are immutable
name="Aarchishya !!!!! Kapoor"
print(name.upper())
print(name.lower())
print(name.rstrip("!"))
print(name.replace("Aarchishya","Ruchir"))
print(name.split(" "))

str1="welcome to the world!!!"
print(str1.capitalize())
print(len(str1))
print(str1.center(50))
print(str1.endswith("!!!"))
print(str1.endswith("to", 4, 10))

str1 = "He's name is Dan. He is an honest man."
print(str1.find("Dan"))
print(str1.index("Dan"))

# If alphanumaric returns true 
str1 = "WelcomeToTheConsole"
print(str1.isalnum())
str1 = "Welcome"
print(str1.isalpha())

str1 = "hello world"
print(str1.islower())

str1 = "We wish you a Merry Christmas\n"
print(str1.isprintable())
str1 = "         "       #using Spacebar
print(str1.isspace())
str2 = "  "       #using Tab
print(str2.isspace())

str1 = "World Health Organization" 
print(str1.istitle())

str2 = "To kill a Mocking bird"
print(str2.istitle())

str1 = "Python is a Interpreted Language" 
print(str1.startswith("Python"))

str1 = "Python is a Interpreted Language" 
print(str1.swapcase())

str1 = "His name is Dan. Dan is an honest man."
print(str1.title())
str1 = "WelcomeToTheConsole"
print(str1.isalnum())
str1 = "Welcome"
print(str1.isalpha())

str1 = "hello world"
print(str1.islower())

str1 = "We wish you a Merry Christmas\n"
print(str1.isprintable())
str1 = "         "       #using Spacebar
print(str1.isspace())
str2 = "  "       #using Tab
print(str2.isspace())

str1 = "World Health Organization" 
print(str1.istitle())

str2 = "To kill a Mocking bird"
print(str2.istitle())

str1 = "Python is a Interpreted Language" 
print(str1.startswith("Python"))

str1 = "Python is a Interpreted Language" 
print(str1.swapcase())

str1 = "His name is Dan. Dan is an honest man."
print(str1.title())