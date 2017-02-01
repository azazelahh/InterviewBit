from decimal import Decimal

def maxPoints(A, B):
    if len(A) == 0:
        return 0
    max_slopes = 0

    for i in range(0, len(A)):
        x1 = A[i]
        y1 = B[i]
        point_slopes = {}
        dups = 1
        for j in range(i + 1, len(A)):
            if i != j:
                x2 = A[j]
                y2 = B[j]
                y = y2 - y1
                x = x2 - x1
                slope = 0
                if x1 == x2 and y1 == y2:
                    dups += 1
                else:
                    if y == 0:
                        slope = 'y'
                    elif x == 0:
                        slope = 'x'
                    else:
                        slope = Decimal(y2 - y1) / (x2 - x1)
                    if slope not in point_slopes:
                        point_slopes[slope] = 0

                    point_slopes[slope] += 1
        if dups == len(A):
            return dups
        slope_count = 0
        if len(point_slopes) > 0:
            slope_count = max(point_slopes.values())
        slope_count += dups
        if slope_count > max_slopes:
            max_slopes = slope_count

    return max_slopes