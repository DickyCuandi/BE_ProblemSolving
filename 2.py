#Question 2
#determine which one of the students got the sour candy

#input
number = input('')

#input processing
number = number.split()

#change list value type to int
number = list(map(int, number))

#output
print(number[1]%number[0]+number[2]-1)