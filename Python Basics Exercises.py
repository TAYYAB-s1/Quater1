#1. Simple Message
a = "this is a message"
print(a)

#2. Simple Messages
b = "this is also a message"
print(b)
b = "\n this is new message"
print(b)

#3. Personal Message
person_name = "\t tayyab shahabz"
print(person_name)
print(f"hello{person_name},how are you doing")

#4. Name Cases
person_name = "tayyab"
print(person_name.lower())
print(person_name.upper())
print(person_name.title())

#5. Famous Quote
print( "- Albert Einstein once said “Life is like riding a bicycle. To keep your balance,you must keep moving.”")

#6. Famous Quote 2
famous_person = "Albert Einstein"
print(f"{famous_person} said: \"Life is like riding a bicycle. To keep your balance, you must keep moving.\"")

#7. Stripping Names
person_name = "\t\n tayyeb\n \t"
print(f"original name is\n {person_name}")
print(f"name after lstrip(): {person_name.lstrip()}")
print(f"name after rstrip(): {person_name.rstrip()}")
print(f"name after strip(): {person_name.strip()}")

#8. Variable Sum
x,y,z = 1,2,3
sum_of_variables = x+y+z
print("\nsum is :",sum_of_variables)

#9. Variable Swap
a = 12
b = 21
#before swap
print("\na =",a)
print("b =",b)
#after swap
a,b = b,a
print("a=",a)
print("b=",b)

#10. Favorite Color

favorite_color ="ed"
print("\nMy favorite color is:", favorite_color)
color = favorite_color
print("The color is still:", color)

#11. Changing Pet Name
pet_name = "\nbuddy"
print("\npet name is:",pet_name)
pet_name = "Max"
print("new pet name:",pet_name)

#12. Observing Name Error
person_name = "sunshine"
print("\nperson name is:",person_name)
print("person name is:",person_name)

#13. Reassigning Score
score = "100"
print("\nscore is:",score)
score = "101"
print("new score is:",score)

#14. City Name
city ='lahore'
print("\ncity is\n:",city)

#15. Title Case Text
text ="python programming"
print(text.title())
print("\n")

#16. Uppercase Conversion
upper_string = 'helo world!'
print( upper_string.upper())
print("\n")

#17. Lowercase Conversion
lower_string ='HILOO WORLD'
print(lower_string.lower())
print("\n")

#18. Current Temperature
temp ="25"
print(f"the current tempurature is {temp} degree")
print("\n")

#9. Printing a Poem
poem ="""The sun sets in the west,
Painting the sky with hues of red.
Stars begin to twinkle bright,
As day gently turns to night."""
print(poem)
print("\n")

