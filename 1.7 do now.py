#Gabe DeHerrera 1/7 daily code if statement

score = int(input("Enter the lines you cleared in tetris: "))
if score < 100:
    print("Novice 0-100 lines")
elif score < 200:
    print("intermediate 100-200 lines")
elif score < 300:
    print("advanced 200-300 lines")
else:
    print("expert 300+ lines
