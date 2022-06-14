#Question 1
#calculate fine based on rules

#input
date1 = input('')
date2 = input('')

#input processing
date1 = date1.split()
date2 = date2.split()

#change list value type to int
date1 = list(map(int, date1))
date2 = list(map(int, date2))

#conditional output
if date2[2] > date1[2]:
    fine = 12000
elif date2[1] > date1[1]:
    fine = (date2[1]-date1[1])*500
elif date2[0] > date1[0]:
    fine = (date2[0]-date1[0])*15
else:
    fine = 0
print(fine)