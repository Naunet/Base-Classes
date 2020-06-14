import matplotlib.pylab as plt
import numpy as np
import calendar


class My_Calendar:
    def __init__(self, month, year):
        self.month = month
        self.year = year
        self.table_vals = self.makeCalendar()
        self.personal_vals = None
        self.col_labels = list()
        for i in range(7):
            self.col_labels.append(calendar.day_abbr[i])

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
        # plot dates
        for irow, row in enumerate(self.table_vals):
            for icol, cell in enumerate(row):
                plt.text(icol + 0.1, nrow - irow - 0.1,
                         cell, va='top')
        # plot data
        if self.personal_vals:
            for irow, row in enumerate(self.personal_vals):
                for icol, cell in enumerate(row):
                    plt.text(icol + 0.5, nrow - irow - 0.6,
                             cell, ha='center', va='center',
                             color='blue')
        plt.show()

    """
    @param content an iterable structure
    @param day between 1 and number of days in the month, default 1
    Sets data to line up with given day
    One element of iterable per day
    Truncates at number of days in the month
    """
    def set_personal_data(self, content, day=1):
        vals = list(content)
        _, limit = calendar.monthrange(self.year, self.month)
        vals = vals[:limit]
        prefix = list()
        i = 0
        j = 0
        while self.table_vals[j][i] != day:
            prefix.append('')
            i += 1
            if i == 7:
                i = 0
                j += 1
                vals = prefix + vals
                prefix = list()
        vals = prefix + vals
        self.personal_vals = list()
        start = 0
        for end in range(7, len(vals)+7, 7):
            self.personal_vals.append(vals[start:end])
            start = end

    """
    @param day between 1 and the number of days in the month
    @return tuple of position from top left
    """
    def day_to_pos(self, day):
        pos_x = (day-1) % 7
        pos_y = (day-1)//7
        while(self.table_vals[pos_y][pos_x] != day):
            if pos_x == 7:
                pos_y += 1
                pos_x = 0
            else:
                pos_x += 1
        return(pos_x, pos_y)

    """
    @param x between 0 and 6
    @param y between 0 and number of weeks in the month -1
    @return tuple of position from bottom left
    """
    def pos_to_coord(self, x, y):
        coord_x = x
        coord_y = len(self.table_vals)-y-1
        return(coord_x, coord_y)

    def color_date(self, day, color):
        pos = self.day_to_pos(day)
        x, y = self.pos_to_coord(*pos)
        plt.fill([x, x, x+1, x+1], [y, y+1, y+1, y], color)
