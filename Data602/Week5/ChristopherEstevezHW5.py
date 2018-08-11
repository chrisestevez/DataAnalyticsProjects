import sys
import pandas as pd
import Tkinter
import tkFileDialog
import heapq
# used http://www.emathzone.com/tutorials/basic-statistics/example-method-of-least-squares.html
#http://www.livephysics.com/tools/mathematical-tools/calculate-linear-regression-graph-scatter-plot-line-fit/
#bo = X * br + Y

# I used tkinter to load the file and checked for correct csv format
try:
    root = Tkinter.Tk()
    root.withdraw()
    filename = tkFileDialog.askopenfilename(parent=root)
    if filename.lower().endswith('.csv'):
        File = pd.read_csv(filename)
    else:
        sys.exit("File format incorrect, please load correct csv file")

except:
    print "Unexpected error:", sys.exc_info()[0]
    raise

print "---------------Top 10 records of file"
print File.head(10)

# Separated the brain and body columns in order to perform calculation.
br = File['brain']
bo = File['body']

# variables for calculations
Size = len(File)
Xvar = sum(bo)
Yvar = sum(br)
XY = sum(bo * br)
Xsqr = sum(bo**2)

print " Length of observations"
print Size
print "X var"
print Xvar
print "Y var"
print Yvar
print "XY"
print XY
print " X^2"
print Xsqr

m = (Size * XY - Xvar * Yvar) / (Size * Xsqr - Xvar**2)
b = (Yvar - m * Xvar) / Size
print "Least square model"
print ("bo = %.2f X br + %.2f" % (m, b))

