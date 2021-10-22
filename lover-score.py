# GET YOUR LOVE SCORE TO SEE IF YOU ARE COMPATIBLE WITH YOUR CRUSH
print("welcome to the love scroe! ")
name1 = input("what is your name? ")
name2 = input("what is your name? ")
name3 = name1.lower()
name4 = name2.lower()

L = name3.count("l")
O = name3.count("o")
V = name3.count("v")
E = name3.count("e")

T = name3.count("t")
R = name3.count("r")
U = name3.count("u")
E= name3.count("e")

namecount = (L + O + V + E + T + R + U + E)
print(namecount)

L = name4.count("l")
O = name4.count("o")
V = name4.count("v")
E = name4.count("e")

T = name4.count("t")
R = name4.count("r")
U = name4.count("u")
E= name4.count("e")

namecount1 = (L + O + V + E + T + R + U + E)
lovescore = (str(namecount) + str(namecount1))

if lovescore < "10" or lovescore > "90":
    print(f"Your score is {lovescore}, you go together like coke and methos. ")
if lovescore > "40" and lovescore < "51":
    print(f" Your score is {lovescore}, you are alright together ")
else:
    print(f"Your score is {lovescore}")
