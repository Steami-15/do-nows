def mult_table(n):
  print(n, "times 1 is", n * 1)
  print(n, "times 2 is", n * 2)
  print(n, "times 3 is", n * 3)
  print(n, "times 4 is", n * 4)
  print(n, "times 5 is", n * 5)
  print(n, "times 6 is", n * 6)
  print(n, "times 7 is", n * 7)
  print(n, "times 8 is", n * 8)
  print(n, "times 9 is", n * 9)
  print(n, "times 10 is", n * 10)

mult_table(3)
print("")

def battery_check(level):
  if level == 100:
      print("battery full")
  elif level >= 50:
      print("battery ok")
  else:
      print("battery low")

battery_check(100)

print("")

def replace_vowels(word):
  vowels = 'aeiou'
  new_word = ''
  for char in word:
      if char in vowels:
          new_word += '*'
      else:
          new_word += char
  return new_word
#this reminds me of the ceaser cipher idk why
print(replace_vowels("skibidi toilet is so awesome"))

print("")

def cost_per_square_inch(diameter, price):
  radius = diameter / 2  # Calculate the radius
  area = 3.14159265359 * radius ** 2  # Area of the pizza (πr²)
  cost_per_inch = price / area  # Cost per square inch
  return cost_per_inch



print("cost per square inch of pizza is:", cost_per_square_inch(12, 10))
