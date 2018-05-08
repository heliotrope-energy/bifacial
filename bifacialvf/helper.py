from bifacialvf import simulate
import os
dir_path = os.path.dirname(os.path.realpath(__file__))
print (dir_path)

def threading_helper(lower_bound, upper_bound):
    writefiletitle = "data/Output/rtr" + str(lower_bound)

    while lower_bound != upper_bound:
        simulate("data/724010TYA.csv", writefiletitle, 10, 180, 1, lower_bound, "interior",
                 0.013 , 6, "glass", "glass", 0.62, False, True, )
        lower_bound = lower_bound+1



