# -*- coding: utf-8 -*-
"""
Created on Sun Jul 20 11:25:30 2025

@author: Kai 
"""

import matplotlib.pyplot as plt # for plots
import numpy as np  # for statistical analysis
import csv # CSV library; easier than what we've done before


# Very simple plot, only specify Y values, and the X values get assumed by MPL

plt.plot([1, 2, 3, 4])
plt.ylabel('some numbers')


plt.xlabel("Some data")

plt.show()







x_vals = [5,10,15,20]

y_vals = [x**2 for x in x_vals]
# x vs y plot; also shows how to specify labels for both axes and an overall title

plt.plot(x_vals, y_vals)
plt.xlabel("X values")
plt.ylabel("Y values")
plt.title("Plot of y = x^2")
plt.show()







# styled plot; same as before expect "g^" does green triangles instead of a blue line

plt.plot(x_vals, y_vals, "b--")
plt.xlabel("X values")
plt.ylabel("Y values")
plt.title("Plot of y = x^2")
plt.show()



# first version -- plotting a bunch of data from a CSV file
with open("transistor_data.csv") as cpu_file:

    # there are two columns we want to grab out of the file 
    # -- others are not interesting
    
    
    _trans = "MOS transistor count"
    _year = "Date of Introduction"
    
    # we'll keep track of the index of those columns
    _trans_col = 0
    _year_col = 0
    
    # use Python's built-in CSV reader module to make our life a bit easier
    cpu_data = csv.reader(cpu_file)
    
    # this is where we'll put the data we pull out of the file
    year_list = []
    trans_list = []

    for rownum, row in enumerate(cpu_data):
        
        # first row is the header; use that to figure out column idxs
        if 0 == rownum:
            _trans_col = row.index(_trans)
            _year_col = row.index(_year)

        # everything else is data!
        else:
            year_list.append(row[_year_col])
            trans_list.append(row[_trans_col])


    # same sort of plot we've done before, give it a list of X and Y values to plot
    # you also know how to do the xlabel and ylabel by now
    plt.plot(year_list, trans_list, "g^")
    plt.xlabel("Year")
    plt.ylabel("Transistor Count")
    plt.title("CPU Transistor Counts Over Time")

    
    plt.show()






# ahhhhh -- that one didn't come out too good.  Make sure well tell PyPlot that the numbers are in fact numbers :)
with open("transistor_data.csv") as cpu_file:

    _trans = "MOS transistor count"
    _year = "Date of Introduction"

    _trans_col = 0
    _year_col = 0

    cpu_data = csv.reader(cpu_file)

    year_list = []
    trans_list = []

    for rownum, row in enumerate(cpu_data):

        if 0 == rownum:
            _trans_col = row.index(_trans)
            _year_col = row.index(_year)

        else:
            
            # the only difference in this version vs the last one
            # is that we use int() so the numbers are treated as such
            
            year_list.append(int(row[_year_col]))
            trans_list.append(int(row[_trans_col]))


    # same sort of plot we've done before, give it a list of X and Y values to plot
    # you also know how to do the xlabel and ylabel by now
    plt.plot(year_list, trans_list, "g^")
    plt.xlabel("Year")
    plt.ylabel("Transistor Count")
    plt.title("CPU Transistor Counts Over Time")

    
    plt.show()







# if we look at the plot, it looks like it's exponential, or at least something
# relatively close to it (so, we see a doubling over the data, over and over)
# there's also a little something that would lead me to epxect this: https://en.wikipedia.org/wiki/Moore%27s_law 

# to make it easier to see what's going on (otherwise, we can't really see 
# anything at the left end of the chart) we can add a logarithmic y-scale


with open("transistor_data.csv") as cpu_file:



    _trans = "MOS transistor count"
    _year = "Date of Introduction"

    _trans_col = 0
    _year_col = 0

    cpu_data = csv.reader(cpu_file)

    year_list = []
    trans_list = []

    for rownum, row in enumerate(cpu_data):

        if 0 == rownum:
            _trans_col = row.index(_trans)
            _year_col = row.index(_year)

        else:
            year_list.append(int(row[_year_col]))
            trans_list.append(int(row[_trans_col]))


    # same sort of plot we've done before, give it a list of X and Y values to plot
    # you also know how to do the xlabel and ylabel by now
    plt.plot(year_list, trans_list, "g^")
    plt.xlabel("Year")
    plt.ylabel("Transistor Count")
    plt.title("CPU Transistor Counts Over Time")
	
	
    # log scale to make it easier to see the (very wide) range of data
    # otherwise, what we've got is the same as above
    plt.yscale("log")

    
    plt.show()





# and a trend line!
# now, we'll add a trend line to see how well our intuition matches a 
# mathematical fit
with open("transistor_data.csv") as cpu_file:


    # This CSV reading stuff we've all seen before
    # really the only difference is that we're reading
    # in two columns instead of the one we did before


    _trans = "MOS transistor count"
    _year = "Date of Introduction"

    _trans_col = 0
    _year_col = 0

    cpu_data = csv.reader(cpu_file)

    year_list = []
    trans_list = []

    for rownum, row in enumerate(cpu_data):

        if 0 == rownum:
            _trans_col = row.index(_trans)
            _year_col = row.index(_year)

        else:
            year_list.append(int(row[_year_col]))
            trans_list.append(int(row[_trans_col]))


    # same sort of plot we've done before, give it a list of X and Y values to plot
    # you also know how to do the xlabel and ylabel by now
    plt.plot(year_list, trans_list, "g^")
    plt.xlabel("Year")
    plt.ylabel("Transistor Count")
    plt.title("CPU Transistor Counts Over Time")

    # log scale to make it easier to see the (very wide) range of data
    # try commenting this out to see what happens
    plt.yscale("log")

    # to do this, we need to use another library.  Matplotlib is _just_ a plotting
    # library.  It's a _very_ good one, but all it does is plot.  A trend
    # line is doing data analysis, and that's not what Matplotlib does.
    
    # this is where we use Numpy, which we practiced with last week


    # this uses numpy to calculate a trend line (best fit)
    # we tell it to fit a first-order polynomial (y=ax + b) to the data
    # after applying a log_10 to the y-values
    z = np.polyfit(year_list, np.log10(trans_list), 1)
    p = np.poly1d(z)

    # use the function numpy calculated for us to calculate 
    # expected y-values for each year for the fit line
    
    
    trend_line_values = [10**p(year) for year in year_list]

    # plotting is pretty similar to what we did previously
    plt.plot(year_list, trend_line_values, "r--")


    plt.show()






#now we're starting to have fun :)
# this one has a legend, too
with open("transistor_data.csv") as cpu_file:


    # This CSV reading stuff we've all seen before
    # really the only difference is that we're reading
    # in two columns instead of the one we did before


    _trans = "MOS transistor count"
    _year = "Date of Introduction"

    _trans_col = 0
    _year_col = 0

    cpu_data = csv.reader(cpu_file)

    year_list = []
    trans_list = []

    for rownum, row in enumerate(cpu_data):

        if 0 == rownum:
            _trans_col = row.index(_trans)
            _year_col = row.index(_year)

        else:
            year_list.append(int(row[_year_col]))
            trans_list.append(int(row[_trans_col]))


        
    # a few changes here relative to the last version.  first, we add this label=
    # this means that when we add a legend to the plot, we get a descriptive
    # name for whatever this piece of data we're plotting is
    plt.plot(year_list, trans_list, "g^", label="Transistor counts over time")
    plt.xlabel("Year")
    plt.ylabel("Transistor Count")
    plt.title("CPU Transistor Counts Over Time")

    # log scale to make it easier to see the (very wide) range of data
    # try commenting this out to see what happens
    plt.yscale("log")

    # this uses numpy to calculate a trend line (best fit)
    z = np.polyfit(year_list, np.log10(trans_list), 1)
    p = np.poly1d(z)

    trend_line_values = [10**p(year) for year in year_list]

    
    # once again, add a label
    plt.plot(year_list, trend_line_values, "r--", label="Logarithmic best fit")

    # now that we've got MPL told what each of the lines represent, all we 
    # need to do is tell it to add a legend, and it'll do so
    # given what our data looks like (increasing left -> right), this
    # seems like the most suitable location for the legend
    plt.legend(loc="upper left")

    plt.show()

"""