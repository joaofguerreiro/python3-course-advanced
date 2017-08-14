import cProfile
cProfile.run("[x for x in range(1500)]")
   #       4 function calls in 0.000 seconds

   # Ordered by: standard name

   # ncalls  tottime  percall  cumtime  percall filename:lineno(function)
   #      1    0.000    0.000    0.000    0.000 <string>:1(<listcomp>)
   #      1    0.000    0.000    0.000    0.000 <string>:1(<module>)
   #      1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
   #      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

"""
ncalls is the number of calls made.
tottime is a total of the time spent in the given function.
percall refers to the quotient of tottime divided by ncalls.
cumtime is the cumulative time spent in this and all subfunctions. It’s even accurate for recursive functions!
The second percall column is the quotient of cumtime divided by primitive calls.
filename:lineno(function) provides the respective data of each function.
"""

# [terminal command] $ python3 -m cProfile timer_context_manager.py
# The function took 13.016324758529663 seconds to complete
#          2116 function calls (2073 primitive calls) in 13.044 seconds

#    Ordered by: standard name

#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         9    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:102(release)
#         9    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:142(__init__)
#         9    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:146(__enter__)
#         9    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:153(__exit__)
#         ..................................................................................
