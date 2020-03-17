def randrep(data, file_name):

    new_data = open(file_name, 'w+')
    raw_data = data.readlines()

    for l in raw_data:

        validity = int(l.split(',')[0])
        coin_flip = round(random.random())

        if coin_flip == 1:

            coin_flip_2 = round(random.random())
            if coin_flip_2 == 0:
                validity = 0
            if coin_flip_2 == 1:
                validity = 1

        new_data.writelines([str(validity)+"\n"])

    return new_data
