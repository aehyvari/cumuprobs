#!/usr/bin/env python
"""Operations on cumulative probabilities"""
import sys

class Prob:

    def __init__(self, data, linfit):
        self.max_value = 0.0
        self.cumuprob = self.get_cumuprob(data)
        self.linfit = linfit

    def getMaxVal(self):
        return self.max_value

    def get_cumuprob(self, data):
        n_data = []
        nof_timeouts = 0
        nof_memouts = 0
        for l in data:
            if l > 0.0:
                n_data.append(l)
            else:
                nof_timeouts += 1
                if l < -1:
                    nof_memouts += 1
        data = n_data

        data.sort()
        cumuprob = []
        for (index, d) in enumerate(data):
            i = index + 1
            if cumuprob and cumuprob[-1][0] == d:
                cumuprob[-1] = (d, float(i)/(len(data)+nof_timeouts))
            else:
                cumuprob.append((d, float(i)/(len(data)+nof_timeouts)))

#        print cumuprob
        if nof_timeouts == 0:
            self.prob_memout = 0
        else:
            self.prob_memout = float(nof_memouts)/float(nof_timeouts)

        self.max_value = float(data[-1])

        return cumuprob

    def get_qt(self, t):
        """Return the probability that the run time is at most t"""
        cumuprob = self.cumuprob
        if t < cumuprob[0][0]:
            return 0.0
        if t >= cumuprob[-1][0]:
            return cumuprob[-1][1]
        i=0
        while True:
            if cumuprob[i+1][0] > t:
                break
            i += 1
        if self.linfit:
            b = (t - cumuprob[i][0]) / (cumuprob[i+1][0] - cumuprob[i][0])
            rval = cumuprob[i][1] + (b * (cumuprob[i+1][1] - cumuprob[i][1]))
        else:
            if t < .5*(cumuprob[i][0]+cumuprob[i+1][0]):
                rval = cumuprob[i][1]
            else:
                rval = cumuprob[i+1][1]

        return rval

    def get_t(self, qt):
        """Return the time by which qt of the runs are finished"""
        cumuprob = self.cumuprob
        if qt <= cumuprob[0][1]:
            return cumuprob[0][0]
        if qt > cumuprob[-1][1]:
            # This is a timeout
            return -1
#        assert qt <= cumuprob[-1][1]
        i = 0
        while True:
            if cumuprob[i+1][1] >= qt:
                break
            i += 1
        if self.linfit:
            b = (qt - cumuprob[i][1]) / (cumuprob[i+1][1] - cumuprob[i][1])
            rval = cumuprob[i][0] + (b * (cumuprob[i+1][0] - cumuprob[i][0]))
        else:
            rval = 0.5*(cumuprob[i+1][0]+cumuprob[i][0])
        return rval

