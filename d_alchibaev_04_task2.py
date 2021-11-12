import timeit
import cProfile


# максимально долгий расчет из-за рекурсивной вложенности и расчета в лоб
def prime(n):
    if n == 1:
        return 2
    if n == 2:
        return 3
    primes = [prime(i) for i in range(1, n)]
    rslt = primes[-1] + 2
    while True:
        if True not in [rslt % prime_num == 0 for prime_num in primes]:
            return rslt
        rslt = rslt + 2


# немного затянутый расчет из-за рекурсии и большого диапазона данных для фильтрации для больших простых чисел
def sieve(n):
    if n == 1:
        return 2
    prime_ = sieve(n-1)
    nums = [i for i in range(prime_ ** 2)]
    nums[1] = 0
    mult_ = 2
    while mult_ <= prime_:
        if nums[mult_] != 0:
            j = mult_ * 2
            while j < len(nums):
                nums[j] = 0  # заменить на 0
                j = j + mult_  # перейти в позицию на m больше
        mult_ += 1
    primes_ = [num for num in nums if num > 0]
    return primes_[n-1]


# получился наудивление быстрый расчет, скорость которого линейно зависит
# от величины простого числа намного больше, чем номера
def prime_alt(n):
    if n == 1:
        return 2
    primes_ = [2]
    while len(primes_) < n:
        iter_ = primes_[-1] + 1
        while True in [iter_ % prime_ == 0 for prime_ in primes_]:
            iter_ = iter_ + 1
        primes_.append(iter_)
    return primes_[-1]


print(timeit.timeit('sieve(10)', number=100, globals=globals())) # 0.036103400000001784
print(timeit.timeit('prime(10)', number=100, globals=globals())) # 0.019351578999703634
print(timeit.timeit('prime_alt(10)', number=100, globals=globals())) # 0.0019493600000259903

print(timeit.timeit('sieve(15)', number=100, globals=globals())) # 0.17966150600022956
print(timeit.timeit('prime(15)', number=100, globals=globals())) # 0.6017456249992392
print(timeit.timeit('prime_alt(15)', number=100, globals=globals())) # 0.003969829000027403

print(timeit.timeit('sieve(30)', number=100, globals=globals())) # 8.65628975200002
#print(timeit.timeit('prime(20)', number=100, globals=globals())) # расчет для 20, для 30 уже долго 15.140994717000467
print(timeit.timeit('prime_alt(30)', number=100, globals=globals())) # 0.014902705999929822

cProfile.run('sieve(40)')
# огромное количество вызовов из-за рекурсий
'''
         587273 function calls (587234 primitive calls) in 0.165 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.165    0.165 <string>:1(<module>)
     40/1    0.107    0.003    0.165    0.165 d_alchibaev_04_task2.py:20(sieve)
       39    0.010    0.000    0.010    0.000 d_alchibaev_04_task2.py:24(<listcomp>)
       39    0.010    0.000    0.010    0.000 d_alchibaev_04_task2.py:34(<listcomp>)
        1    0.000    0.000    0.165    0.165 {built-in method builtins.exec}
   587152    0.036    0.000    0.036    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
'''

cProfile.run('prime_alt(200)')
# расчет линейный, какие-то наблюдаемые изменения возникают при n 200
'''
         1624 function calls in 0.009 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.009    0.009 <string>:1(<module>)
        1    0.001    0.001    0.009    0.009 d_alchibaev_04_task2.py:40(prime_alt)
     1221    0.008    0.000    0.008    0.000 d_alchibaev_04_task2.py:46(<listcomp>)
        1    0.000    0.000    0.009    0.009 {built-in method builtins.exec}
      200    0.000    0.000    0.000    0.000 {built-in method builtins.len}
      199    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
'''