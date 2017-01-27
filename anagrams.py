def anagrams(self, A):
    solutions = {}
    for i in range(len(A)):
        word = A[i]
        sorted_word = "".join(sorted(word))
        if solutions.get(sorted_word, []) == []:
            solutions[sorted_word] = []
            solutions[sorted_word] += [i + 1]
        else:
            solutions[sorted_word] += [i + 1]
    return solutions.values()