def minWindow(S, T):
    ts = dict.fromkeys(T, -1)
    count = 0
    windows = {}

    for i in range(0, len(S)):
        if S[i] in ts:
            if ts[S[i]] == -1:
                count += 1
                ts[S[i]] = []
            ts[S[i]] += [i]
        if (len(ts) > 1 and count == len(ts)) or (len(ts) == 1 and count == len(T)) or (len(ts) == 1 and len(T) > 0 and ts[T[0]] != -1 and len(ts[T[0]]) == len(T)):
            min_val = len(S) + 1
            min_list = []
            max_val = -1
            max_list = []
            for k, v in ts.items():
                for val in v:
                    if val <= min_val:
                        min_val = val
                        min_list = v
                    if val >= max_val:
                        max_val = val
                        max_list = v
                ts[k] = -1
            if min_list == max_list:
                indxs = min_list[0: len(T)]
                if len(indxs) == 1:
                    return S[indxs[0]]
                return S[indxs[0]: indxs[-1] + 1]
            if len(windows) == 0:
                windows[max_val - min_val] = [min_val, max_val]
            elif max_val - min_val < windows.items()[0][0]:
                windows = {}
                windows[max_val - min_val] = [min_val, max_val]
            count = 0

    if len(windows) == 0:
        return ''

    inds = windows.items()[0][1]

    return S[inds[0]: inds[1] + 1]

## need to make sure the count of letters in T and solution is the same