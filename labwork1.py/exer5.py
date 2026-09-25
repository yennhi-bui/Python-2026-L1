fav = ["orange", "blue", "green", "white"]
color = input('What is your favorite color?')

for i in range (len(fav)):
    if color == fav[i]:
        print(f"Your colod is at index {i} in my list")
        break
else:
    print(f"Sorry, I could not find your color")
    
       