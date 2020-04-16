def bid_yield(arr, sell):

    count = 0
    for i in range(len(arr)):

        if arr[i] >= sell:
            count+=1

    return sell*count


file = open('C:\\Users\\Teki\\PycharmProjects\\dif-prvcy\\em-test.csv', 'r')
expmech(file, 'C:\\Users\\Teki\\PycharmProjects\\dif-prvcy\\em-encrypted_test.csv', 3.0, bid_yield, range(0, 10))
print('Procedure finished.')
