DAY 4 HOMEWORK   



numpy.array(object, dtype=None, *, copy=True, order='K', subok=False, ndmin=0, like=None)
Create an array.



numpy.around(a, decimals=0, out=None)[source]
Evenly round to the given number of decimals.



numpy.arange([start, ]stop, [step, ]dtype=None, *, like=None)
Return evenly spaced values within a given interval.

arange can be called with a varying number of positional arguments:

arange(stop): Values are generated within the half-open interval [0, stop) (in other words, the interval including start but excluding stop).

arange(start, stop): Values are generated within the half-open interval [start, stop).

arange(start, stop, step) Values are generated within the half-open interval [start, stop), with spacing between values given by step.

For integer arguments the function is roughly equivalent to the Python built-in range, but returns an ndarray rather than a range instance.

#MY PSEUDOCODE INTERPRETATION
#set probs variable as:  --> evenly round the following values:    values spaced 0.05 apart, between 0.55 and 1.05     evenly round them bad boys to 2 decimals <--(all shall be mirrored)
      probs   =                    numpy.around                          (numpy.arange(0.55, 1.05, 0.05),                              decimals=2)                        [::-1]


#this code:
print(run_experiment(0.5, 100, 100, 389, False))

tosses = numpy.array([10, 50, 100, 250, 500, 1000])
probs = numpy.around(numpy.arange(0.55, 1.05, 0.05), decimals=2)[::-1]
print(tosses)
print("ok ok ok")
print(probs)

#.......    gives this result:
(base) [~/qbb2022-answers/day4-homework $]python binomial_power_interactive_lecture.py 
0.04
[  10   50  100  250  500 1000]
ok ok ok
[1.   0.95 0.9  0.85 0.8  0.75 0.7  0.65 0.6  0.55]


