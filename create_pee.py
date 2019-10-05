import sys # user input
from pee import * # my function for Pee(L, E)

def create_pee():
    '''
    Format:
    Option 1: Pee as a function of L, different energy (E) in GeV
    python create_pee.py E=2
    python create_pee.py E=0.01,0.02,0.05

    Option 2: Pee as a function of E, different distance (L) in km
    python create_pee.py L=200
    python create_pee.py L=180,200,300

    Option 3: 3D surface as a function of both E and L
    python create_pee.py surface

    By default, you will be shown the resulting plot. If you wish to save the
    PNG of the plot and the .csv files with the points, type 'save' at the end
    of your command e.g.
    python create_pee.py L=180,200,300 save

    Run these examples to try it out :)

    Advanced:
    If you want to change the range on the x-axis for E or L, go to the top
    of pee.py and change the values where it says "CHANGE THIS"
    '''

    # possible input
    if not len(sys.argv) in [2,3]:
        print create_pee.__doc__
        # print create_pee.__doc__
        return


    if 'surface' in sys.argv:
        # 2D plot
        Pee = PeePlot()
        Pee.plot_3d()
    else:
        # get points from user input
        points = np.array(sys.argv[1].split('=')[1].split(',')).astype(float) # [a, b, c]
        # get variable from user input
        var = sys.argv[1].split('=')[0] # E or L
        # check if correct variable usage
        if not var in ['E', 'L']:
            print create_pee.__doc__
            return

        Pee = PeePlot((10,8))
        Pee.plot_points(var, points)
    #create_pee(var, points)

create_pee()
