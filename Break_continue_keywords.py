print("The break instruction:")
for i in range(1,6):
    if i == 3:
        break
    print("inside the loop",i)
print("Ouside the loop")

print("\nThe Continue instructions:")
for i in range(1,6):
    if i==3:
        continue
    print("inside the loop",i)
print("outside the loop")