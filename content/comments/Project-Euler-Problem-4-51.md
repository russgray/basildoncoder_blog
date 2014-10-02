post_id: project-euler-problem-4
Author: sseraph
Date: 2010-10-19 01:38:12
Author_Email: noreply@blogger.com
Author_IP: None

I used python.  I made a simple generate to generate 6 digit palindromes
highest to lowest. For each one I got its prime factors and checked to see if
a pair of 3 digit numbers could be generated from those factors.

    :::python
    def factor(num):
        max = int(num ** 0.5)
        gen = primes_upto(max)
        factors = []
        for f in gen:
            if f > num: break
            while not num % f:
                num = num / f
                factors.append(f)
        if num > 1: factors.append(num)
        return factors


    def gen_pal6():
        for i in range(9,1,-1):
            for j in range(9,0,-1):
                for k in range(9, 0, -1):
                    pal = i * 100000 + j * 10000 + k * 1000 + k * 100 + j * 10 + i * 1
                    yield pal

    def factor_pairs(factors, size):
        ''' given list of factors find pairs of factors of given size equal to the factored number.  Presumes factors are prime and in increasing order.'''
        pair = []
        maxv = 10 ** size
        minv = 10 ** (size - 1)
        ilen = lambda x: len(str(x))
        #if largest factor is > size then impossible
        last = factors[-1]
        factors = factors[:-1]
        if last < maxv:
            while (last * factors[0]) < maxv:
                last = last * factors[0]
                factors = factors[1:]
            rest = reduce(lambda a,b: a * b, factors)
            if ilen(rest) == size:
                return rest,last
        return None



    def euler4():
        gen = gen_pal6()
        for i in gen:
            pairs = factor_pairs(factor(i), 3)
            if pairs:
                return i, pairs
