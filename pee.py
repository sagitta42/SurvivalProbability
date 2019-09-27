#############################
#### CHANGE THIS IF YOU WANT ####

# range in km
Lmin = 0.001
Lmax = 300
# range in GeV
Emin = 0.001 # to avoid division by zero
Emax = 2

#############################

# for Pee function
from math import cos
# for PeePlot class
import numpy as np
import pandas as pd # tables
from myplot import * # plotting


def Pee(x, dct):
    '''
    I know it basically says 'pee', but this stands for "electron flavour
    neutrino survival probability". It's typically denoted as
    P(nu_e -> nu_e), probability that an electron neutrino will NOT oscillate
    to become any other flavour, but still stay the same

    L is in km (distance travelled), E is in GeV (energy of neutrino)
    dct has a format {var: a} where var is 'L' or 'E' and a is the value that
    variable takes
    x is an array of values for the variable that is NOT in dct
    '''

    ## well known parameters

    # sin^2(2*theta_13), error 0.008; known from results of Daya Bay, RENO and Double Chooz
    sin22theta13 = 0.093 # no unit
    # delta_m31^2, i.e. (m3 - m1)^2, mass difference
    dm31 = 2.44 * 1e-3 # eV^2
    # the factor 1.27 is calculated s.t. L is in km and E is in GeV
    if 'E' in dct:
        delta = 1.27 * dm31 * x*1. / dct['E']
    elif 'L' in dct:
        delta = 1.27 * dm31 * dct['L']*1. / x
    else:
        print 'Incorrect variable, how did we get here?'
        return -1

    return 1. - 0.5 * sin22theta13 * (1. - cos(delta))


class PeePlot():
    '''
    Class that contains all the plotting info
    '''

    def __init__(self):
        self.df = pd.DataFrame() # empty table
        # plot
        self.p = Plot((10,8))
        self.p.ax.set_title('Electron neutrino survival probability')


    def plot_points(self, var, points):
        '''
        Plot Pee as a function of given variable (L or E) for given fixed the other variable (E, L)
        e.g. Pee(L) for E = 5 GeV, or Pee(E) for L = 200 km

        Create a .png plot and a txt file with the x and y points of the plot
        '''

        # if var is L, var2 is E and vice versa
        vars = ['E', 'L']
        vars.remove(var)
        var2 = vars[0]

        # points for the other variable (which is on the x axis)
        self.df[var2] = RANGE[var2]

        # Pee as a function of var2 for constant var
        for p in points:
            label = var + ' = ' + str(p) + UNIT[var]
            print label
            self.df[label] = self.df[var2].apply(Pee, dct={var: p})

        self.df = self.df.set_index(var2)
        self.df.plot(ax = self.p.ax, style='-')
        self.p.ax.set_xlabel(LABEL[var2] + ' [' + UNIT[var2] + ']')
        self.p.ax.set_ylabel(r'$P(\nu_e \rightarrow \nu_e)$')

        self.p.legend()

        # output name if PNG and txt
        name = 'pee_' + var + '-'.join((str(x) for x in points)) + UNIT[var]
        self.p.figure(name + '.png') # save or show depending on user input

        # save the txt file if requested
        if 'save' in sys.argv:
            self.df.to_csv(name + '.csv', sep = ',')
            print 'Saved to', name + '.csv'


# ranges for variables of choice
RANGE = {'L': np.linspace(Lmin, Lmax, (Lmax - Lmin) * 2000), # step of 0.005km
        'E': np.linspace(Emin, Emax, (Emax - Emin) * 2000)} # step of 0.005GeV

# unit of the variable
UNIT = {'L': 'km', 'E': 'GeV'}
# label of the variable
LABEL = {'L': 'Distance', 'E': 'Energy'}
