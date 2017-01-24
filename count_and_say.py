# @param A : integer
# @return a strings
def countAndSay(self, n):
    s = '1'
    for i in range(0, n - 1):
        s = self.get_next(s)

    return s


def get_next(self, seq):
    i, next_seq = 0, ''
    while i < len(seq):
        cnt = 1
        while i < len(seq) - 1 and seq[i] == seq[i + 1]:
            cnt += 1
            i += 1
        next_seq += str(cnt) + seq[i]
        i += 1
    return next_seq