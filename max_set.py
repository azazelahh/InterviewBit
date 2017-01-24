# @param A : list of integers
# @return a list of integers
def maxset(self, A):
    max_sum = sub_sum = max_len = sub_len = 0
    max_arr = sub_arr = []

    for i in A:
        if i >= 0:
            sub_sum += i
            sub_len += 1
            sub_arr.append(i)
            if sub_sum > max_sum:
                max_sum = sub_sum
                max_len = sub_len
                max_arr = sub_arr
            elif sub_sum == max_sum and sub_len >= max_len:
                max_sum = sub_sum
                max_len = sub_len
                max_arr = sub_arr
        else:
            if sub_sum > max_sum:
                max_sum = sub_sum
                max_len = sub_len
                max_arr = sub_arr
            elif sub_sum == max_sum and sub_len >= max_len:
                max_sum = sub_sum
                max_len = sub_len
                max_arr = sub_arr

            sub_sum = 0
            sub_len = 0
            sub_arr = []
    return max_arr