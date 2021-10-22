print("Welcome to the rollercoater ride!")
height = int(input("what is your height? " ))

bill = " "

if height < 10:
  print("sorry you cannot ride this roalorcoater :|" )
else:
  age = int(input("what is your age? "))
  if age <= 5:
    bill = 5
    print("your bill is $5")
  elif age <=12:
    bill = 8
    print("your bill is $8")
  elif age <= 17:
    bill = 12
    print("your  bill is $12")
  else:
    bill = 15
    print("your bill is $15 ")

photos = input("you you lke a photo taken of you, Y, N? ")
if photos == "Y":
  bill +=3
  print(f"your total bill is {bill}")
else:
  pass
