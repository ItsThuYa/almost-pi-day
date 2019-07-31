for i in range(1, 6):
    print(i * '* ')
print()

for i in range(5, 0, -1):
    print(i * '* ')
print()

for i in range(1, 6):
    print("{:>10}".format(" *" * i))
print()

for i in range(5, 0, -1):
    print("{:>10}".format(" *" * i))
print()

for i in range(1, 11, 2):
    print("{:^20}".format(" *" * i))
print()

for i in range(9, 0, -2):
    print("{:^20}".format(" *" * i))
print()