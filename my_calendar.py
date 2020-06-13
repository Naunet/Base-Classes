import matplotlib.pylab as plt
import numpy as np
import calendar


class My_Calendar:
    def __init__(self, month, year):
        self.month = month
        self.year = year
        self.table_vals = self.makeCalendar()
        self.col_labels = list()
        for i in range(7):
            self.col_labels.append(calendar.day_abbr[i])
        self.draw()

    def makeCalendar(self):
        vals = list()
        week = list()
        start, limit = calendar.monthrange(self.year, self.month)
        for i in range(start):
            week.append('')
        for i in range(1, limit+1):
            if(len(week) == 7):
                vals.append(week)
                week = list()
            week.append(i)
        while(len(week) < 7):
            week.append('')
        vals.append(week)
        return vals

    """
    Based on Bas Swinckels answer on StackOverflow
    https://stackoverflow.com/a/22107085
    """
    def draw(self):
        ncol = len(self.col_labels)
        nrow = len(self.table_vals)
        plt.axis('off')
        # add title
        plt.title(calendar.month_name[self.month] + ' ' + str(self.year))
        # draw grid lines
        plt.plot(np.tile([0, ncol], (nrow+2, 1)).T,
                 np.tile(np.arange(nrow+2), (2, 1)),
                 'k', linewidth=3)
        plt.plot(np.tile(np.arange(ncol+1), (2, 1)),
                 np.tile([0, nrow+1], (ncol+1, 1)).T,
                 'k', linewidth=3)
        # plot labels
        for icol, col in enumerate(self.col_labels):
            plt.text(icol + 0.5, nrow + 0.5,
                     col, ha='center', va='center')
        # plot table content
        for irow, row in enumerate(self.table_vals):
            for icol, cell in enumerate(row):
                plt.text(icol + 0.5, nrow - irow - 0.5,
                         cell, ha='center', va='center')
        plt.show()


# Example
cal = My_Calendar(2, 1968)
