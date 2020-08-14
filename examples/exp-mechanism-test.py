def bid_yield(arr, sell):

    count = 0
    for i in range(len(arr)):

        if arr[i] >= sell:
            count+=1

    return sell*count


file = open('em-test.csv', 'r')
expmech(file, 'em-encrypted_test.csv', 3.0, bid_yield, range(0, 10))
print('Procedure finished.')
