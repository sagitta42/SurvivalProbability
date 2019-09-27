import sys # user input

from pee import * # my function for Pee(L, E)


def create_pee(var, points):
    '''
    Format:
    Option 1: Pee as a function of L, different energy (E) in GeV
    python create_pee.py E=2
    python create_pee.py E=2,3,5

    Option 2: Pee as a function of E, different distance (L) in km
    python create_pee.py L=200
    python create_pee.py L=180,200,300

    By default, you will be shown the resulting plot. If you wish to save the
    PNG of the plot and the .txt files with the points, type 'save' at the end
    of your command e.g.
    python create_pee.py L=180,200,300 save

    Run these examples to try it out :)

    Advanced:
    If you want to change the range on the x-axis for E or L, go to the top
    of pee.py and change the values where it says "CHANGE THIS"
    '''

    # class for plotting everything
    Pee = PeePlot()
    Pee.plot_points(var, points)


def main():
    # one input has to be given
    if not len(sys.argv) in [2,3]:
        print create_pee.__doc__
        return

    # get points from user input
    points = np.array(sys.argv[1].split('=')[1].split(',')).astype(int) # [a, b, c]
    # get variable from user input
    var = sys.argv[1].split('=')[0] # E or L
    # check if correct variable usage
    if not var in ['E', 'L']:
        print create_pee.__doc__
        return

    create_pee(var, points)

main()
