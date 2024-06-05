#code by joy dhairyalakshmi gowda

beatles = []
# step 1
print("Step 1:", beatles)

beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print("Step 2:", beatles)

for member in range[2]:
    beatleName = []
#step 3
    beatleName = input("Enter new Beatle name: ")
    beatles.append(beatleName)
print("Step 3:", beatles)

del beatles [-1]
del beatles [-1]
# step 4
print("Step 4:", beatles)

beatles.insert(0, "Ringo Starr")
#step 5
print("Step 5:", beatles)


# testing list legth
print("The Fab", len(beatles))
