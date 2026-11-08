math=int(input("Enter the math score: "))
english=int(input("Enter the english score: "))

if math >=40 and english>=40:
    print("Both pass")
elif math>=40 or english>=40:
    print("One pass")
else:
    print("Both fail")