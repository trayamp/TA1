print("Name: Justin Fernando")
print("Student No: 202420033")
print("Year: 2 - BSIT | transferee")

#using nested 'for' statement
def output_a():
    for i in range(6):
        print(' ' * (5 - i) + ''.join(str(j) for j in range(1, i + 1)))

#Using nested 'while' statement
def output_b():
    i = 1
    while i <= (7):
        if i % 2 != 0:
            print(' ' * (7 - i) + str(i) * i)
        i += 1

# printing out
output_a()
print() 
output_b()