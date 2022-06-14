#Question 3
#find an element in an array where the sum of elements to the left 
# is equal to the sum of all elements to the right.

#input
length = int(input(''))
val = input('')

#input processing
arr = val.split()

#change list value type to int
arr = list(map(int, arr))

i = 0
j = length-1

#just in case the length of list does not match with count of numbers given
try:
    sum_i = arr[i]
    sum_j = arr[j]
    cek = False
    #compare the sum of left side of array with right side of array
    while i != j:
        if sum_i == sum_j:
            cek = True
            i = j
        elif sum_i < sum_j:
            i += 1
            sum_i += arr[i]
        elif sum_i > sum_j:
            j -= 1
            sum_j += arr[j]
    if cek:
        print('YES')
    else:
        print('NO')
except:
    print('Wrong input')