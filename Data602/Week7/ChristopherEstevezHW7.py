import timeit


setup = '''
import sys
import pandas as pd
from scipy.optimize import curve_fit
from scipy import stats
import numpy as np

try:

        File = pd.read_csv('brainandbody.csv')


except:
    print "Unexpected error:", sys.exc_info()[0]
    raise

br = File['brain']
bo = File['body']
np_br = np.array(br)
np_bo = np.array(bo)

def least_square(x,y):
    # variables for calculations
    Size = len(File)
    Xvar = sum(x)
    Yvar = sum(y)
    XY = sum(x * y)
    Xsqr = sum(x**2)

    m = (Size * XY - Xvar * Yvar) / (Size * Xsqr - Xvar**2)
    b = (Yvar - m * Xvar) / Size
    return ("bo = %.2f X br + %.2f" % (m, b))

# regressions using SciPy


def func(x, a, b):
    return a * x+ b


def curve_fitting(x, y):
    cur = curve_fit(func, bo, br)
    ans = 'y = %.2f X br + %.2f' % (cur[0][1], cur[0][0])
    return ans

'''
if __name__ == "__main__":


    n = 5000

t = timeit.Timer('least_square(bo,br)', setup=setup)
print 'Original                :', t.timeit(n), " seconds"

t = timeit.Timer("least_square(np_bo,np_br)", setup=setup)
print 'Original & numpy arrays :', t.timeit(n), " seconds"

t = timeit.Timer("curve_fitting(bo,br)", setup=setup)
print 'scipy                   :', t.timeit(n), " seconds"

t = timeit.Timer("curve_fitting(np_bo,np_br)", setup=setup)
print 'scipy & numpy arrays    :', t.timeit(n), " seconds"




#testing for functions
#print "\nLeast square model"
#print least_square(bo, br)


#print "\nCurve Fitting"
#print curve_fitting(bo, br)
