import sys
import matplotlib
matplotlib.use('Agg')
import pandas as pd
import matplotlib.pyplot as plt

class CorrCalcs ():
    def __init__(self):
        pass

    def display_positive_plot (self, data_frame, arg1, arg2):
        display_data = data_frame
        display_data.plot(x = arg1, y = arg2, kind = 'scatter'),
        plt.show()

        plt.savefig(sys.stdout.buffer)
        sys.stdout.flush()