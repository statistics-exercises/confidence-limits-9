# Histograms for continuous random variables I

In previous exercises, the process of estimating the probability mass function for a discrete random variable by repeatedly sampling and constructing a histogram has been discussed. An obvious question we might ask, given what we are studying this week, is how do we apply this business of computing histograms if we have continuous as opposed to discrete random variables.  In other words, can we estimate the probability density function for a continuous random variable by repeatedly sampling that random variable and by constructing a histogram?

The answer to this question is obviously yes.  Furthermore, when we estimate histograms in this way we use the `np.floor` function that we learned about in the context of generating discrete uniform random variables.  To understand how we do this suppose we want to compute the histogram by repeatedly sampling a uniform random variable between 0 and 1.  We would divide the range between 0 and 1 into n discrete segments, which each have a length of 1/n and which are often referred to as bins.  If we then sample our uniform random variable U we can determine which of the subranges the random variable falls into by performing the following calculation:

````
delr = 1 / n
mybin = int( np.floor( U / delr ) ) 
````

We can thus use the above within the normal code that we would employ to compute the histogram.  Now, however, the height of the bars in the unormalized histogram are equal to the number of random variable that fall into each of the line segments of interest. 

To understand this idea better see if you can complete the code in the cell on the right and thus estimate the probability density function for a uniform random variable between 0 and 1.   To complete this code you will need to:

1. Write a loop that generates 300 uniform random variables that lie between 0 and 1.
2. Use the array called `counts` to count how many of each of these random variables fall into each of the 100 bins that we have divided the line segment between 0 and 1 into.
3. Write a loop that normalises the histogram in `counts` and coverts each count from the number of random variables that were inside this bin into the fraction of random variables that we inside this bin.  By the time you exit this loop the sum of all the elements of counts should be one.
4. Within the loop that normalises the `counts` list you should also generate the x-coordinates at which you will plot each of the data points in the counts list.  These x-coordinates should be placed at the midpoint of each of the bins.  Furthermore, as you can see the zeroth element of the histogram will be plotted at `(xdata[0], counts[0])`, the first element of the histogram will be plotted at `(xdata[1],counts[1])` and so on.  Your midpoints should thus be stored in the list called `xdata`.
