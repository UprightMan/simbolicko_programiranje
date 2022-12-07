def recaman(n):
    sequence = []
    for i in n:
        if i <= 0:
            sequence.append(0)
        elif sequence[i-1] - n > 0  and  sequence[i-1] - n not in sequence:
            sequence.append(sequence[i-1] - n)
        else:
            sequence.append(sequence[i-1] + n)
    return sequence

