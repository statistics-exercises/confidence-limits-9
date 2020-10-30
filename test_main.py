import unittest
import scipy.stats as st
import scipy.special as sp
from main import *

class UnitTests(unittest.TestCase) :
    def test_xplot(self) :
       fighand = plt.gca()
       figdat = fighand.get_lines()[0].get_xydata()
       this_x, this_y = zip(*figdat)
       for i in range(len(this_x)) :
           self.assertTrue( np.fabs( (i+0.5)/len(this_x) - this_x[i] )<1e-7, "the x-coordinates of the points in your graph are incorrect" )
  
    def test_normalised(self) : 
        ssum = 0.
        fighand = plt.gca()
        figdat = fighand.get_lines()[0].get_xydata()
        this_x, this_y = zip(*figdat)
        for i in range(len(this_x)) : ssum = ssum + this_y[i]
        self.assertTrue( np.fabs(ssum - 1.)<1e-7, "the histogram that you have plotted has not been normalised" )

    def test_plot(self) : 
        fighand=plt.gca()
        figdat = fighand.get_lines()[0].get_xydata()
        this_x, this_y = zip(*figdat)
        for i in range( len(this_y) ) :
            bar = np.sqrt( (1/len(this_y))*(1-(1/len(this_y))) )*st.norm.ppf( (0.99 + 1) / 2 )
            self.assertTrue( np.fabs( this_y[i]- (1/len(this_y)) )<bar, "the y-coordinats of the points in your graph appear to be incorrect" )
