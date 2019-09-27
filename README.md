# SurvivalProbability

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
