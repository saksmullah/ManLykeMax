my_name = input("please enter your name ")
print(my_name)

file = open('name.txt', mode='w')
print(file)
print(file.write(my_name))
file.close()
file = open('name.txt', mode='r')
print(file.read())

