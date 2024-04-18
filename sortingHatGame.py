points = {'Gryffindor': 0, 'Ravenclaw': 0, 'Hufflepuff': 0, 'Slytherin': 0}

print("Q1) Do you like Dawn or Dusk?")
print("   1) Dawn")
print("   2) Dusk")
answer = input("Your choice (1/2): ")

# Update points based on the user's answer
if answer == '1':
    points['Gryffindor'] += 1
    points['Ravenclaw'] += 1
elif answer == '2':
    points['Hufflepuff'] += 1
    points['Slytherin'] += 1
else:
    print("Wrong input.")

print("Q2) When I'm dead, I want people to remember me as:")
print("   1) The Good")
print("   2) The Great")
print("   3) The Wise")
print("   4) The Bold")
answer = input("Your choice (1-4): ")

# Update points based on the user's answer
if answer == '1':
    points['Hufflepuff'] += 2
elif answer == '2':
    points['Slytherin'] += 2
elif answer == '3':
    points['Ravenclaw'] += 2
elif answer == '4':
    points['Gryffindor'] += 2
else:
    print("Wrong input.")

print("Q3) Which kind of instrument most pleases your ear?")
print("   1) The violin")
print("   2) The trumpet")
print("   3) The piano")
print("   4) The drum")
answer = input("Your choice (1-4): ")

# Update points based on the user's answer
if answer == '1':
    points['Slytherin'] += 4
elif answer == '2':
    points['Hufflepuff'] += 4
elif answer == '3':
    points['Ravenclaw'] += 4
elif answer == '4':
    points['Gryffindor'] += 4
else:
    print("Wrong input.")

# Print points for each house
print("Points for each house:")
for house, point in points.items():
    print(f"{house}: {point}")

