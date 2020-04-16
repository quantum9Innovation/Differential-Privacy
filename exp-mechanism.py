def expmech(data, file_name, epsilon, u, r, sample_size=10, delta_u=None):

    new_data = open(file_name, 'w+')
    raw_data = data.readlines()

    rows = len(raw_data)
    sample_size = min(rows, sample_size)
    columns = len(raw_data[0].split(','))

    if delta_u is None:

        delta_u = []
        data_draft = []

        for c in range(columns):

            data_draft.append([float(raw_data[ro].split(',')[c]) for ro in range(rows)])
            samples = [int(rows * random.random()) for i in range(sample_size)]
            delta_u.append(0.01)

            for i in samples:

                for k in r:

                    x_prime = [x for x in data_draft[-1]]
                    x_prime[i] += 1
                    delta_u[-1] = max(delta_u[-1], abs(u(data_draft[-1], k)-u(x_prime, k)))

    line = []

    for c in range(columns):

        data = [float(raw_data[ro].split(',')[c]) for ro in range(rows)]
        probabilities = [math.exp(epsilon*u(data, k)/(2*delta_u[c])) for k in r]
        rand = sum(probabilities)*random.random()

        r_choice = 0
        running_sum = 0

        for choice in r:

            if rand <= running_sum + probabilities[choice]:
                r_choice = choice
                break

            else:
                running_sum += probabilities[choice]

        line.append(r_choice)

    new_data.writelines(str(line)+'\n')

    return new_data
