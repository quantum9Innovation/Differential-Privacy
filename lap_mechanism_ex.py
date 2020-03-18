def avg(arr):

    sum = 0
    for i in arr: sum += i
    return sum / len(arr)

file = open('lm-test.csv', 'r')
lapmech(file, 'lm-encrypted_test.csv', 1.0, avg)
print('Procedure finished.')
