# @param X : list of integers
# @param Y : list of integers
# Points are represented by (X[i], Y[i])
# @return an integer
def coverPoints(self, X, Y):
    steps = 0
    x = y = 0
    for i in range(0, len(X)):
        if i == 0:
            x = X[i]
            y = Y[i]
        else:
            new_x = X[i]
            new_y = Y[i]

            sum_x = abs(new_x - x)
            sum_y = abs(new_y - y)

            if sum_x >= sum_y:
                steps += sum_x
            else:
                steps += sum_y

            x = new_x
            y = new_y

    return steps
