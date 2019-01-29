def fibo(n):
    seq = [1, 1]
    a = 0
    while a < (n - 1):
        assert len(seq) > a
        next = seq[a] + seq[a+1]
        seq.append(next)
        a += 1

    return seq[n - 1]
