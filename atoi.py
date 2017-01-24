# @param A : string
# @return an integer
def atoi(self, A):
    integer = 0
    int_began = False
    negative = False
    positive = False
    for i in A:
        if i.isdigit():
            if int_began == False:
                int_began = True
            integer *= 10
            integer += int(i)
        else:
            if int_began:
                break
            else:
                if i == '-':
                    negative = True
                elif negative or positive:
                    return 0
                elif i == ' ' or i == '+':
                    if i == '+':
                        positive = True
                    continue
                else:
                    return 0
    if integer > 2147483647:
        integer = 2147483647
    if negative:
        if integer == 2147483647:
            integer = 2147483648
        return 0 - integer
    return integer