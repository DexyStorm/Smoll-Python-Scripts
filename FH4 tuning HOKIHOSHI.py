wd = float(input("What is your Weight distribution? (for example: 55% = 0.55)"))

print("")
print("DAMPING:")
dampmax = float(20)
dampmin = float(3)


rsfone = float(dampmax) - float(dampmin)
rsftwo = float(rsfone) * float(wd)
rsfthree = float(rsftwo) + float(dampmin)
print("Rebound Stiffness front", + rsfthree)

rsrone = float(dampmax) - float(dampmin)
revone = float(wd) - 1
revtwo = -revone
rsrtwo = float(rsrone) * float(revtwo)
rsrthree = float(rsrtwo) + float(dampmin)
print("Rebound Stiffness rear", + rsrthree)


bsfone = float(rsfthree) / 100
bsftwo = float(bsfone) * 60
print("Bump Stiffnes front", + bsftwo)

bsrone = float(rsrthree) / 100
bsrtwo = float(bsrone) * 60
print("Bump Stiffnes rear", + bsrtwo)



print("")
print("SPRINGS")
smax = input("What is the springs max?")
smin = input("What is the springs min?")


sfone = float(smax) - float(smin)
sftwo = float(sfone) * float(wd)
sfthree = float(sftwo) + float(smin)
print("Springs front", + sfthree)

srone = float(smax) - float(smin)
srtwo = float(srone) * float(revtwo)
srthree = float(srtwo) + float(smin)
print("Springs rear", + srthree)


print("")
print("ANTIROLLBARS")
armax = float(65)
armin = float(1)

arfone = float(armax) - float(armin)
arftwo = float(arfone) * float(wd)
arfthree = float(arftwo) + float(armin)
print("Anti Rollbars front", + arfthree)

arrone = float(armax) - float(armin)
arrtwo = float(arrone) * float(revtwo)
arrthree = float(arrtwo) + float(armin)
print("Anti Rollbars rear", + arrthree)




input()
