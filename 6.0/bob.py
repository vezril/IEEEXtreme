#!/usr/bin/env python
import mat, sys



if __name__ == "__main__":
    N = 1
    C = 651.70
    # Percentage to invest monthly after taxes
    PFC = 59
    # Monthly salary bonus for the year, depends on N; MSFTY = [[Si, Bi]]
    MSBFTY = [[12.29 103.89]]
    # Property taxes
    T = 0.42
    # Property registration fee percentage
    F = 2
    # Number of properties available for perchase
    P = 4
    # Properties data
    prop = [[(1, 1, 72.62, 741.97), (1, 6, 67.66, 646.20), (1, 7, 58.83, 563.79), (1, 10, 57.95, 526.55), (1, 12, 62.73, 656.49) ],[(1, 1, 80.65, 832.35), (1, 11, 92.79, 951.74), (1, 12, 102.73, 975.86)],[(1, 1, 111.34, 976.17), (1, 3, 105.85, 895.93), (1, 7, 110.76, 920.65), (1, 10, 102.63, 887.31), (1, 11, 104.72, 1094.79), (1, 12, 94.91, 898.43)],[(1, 1, 67.15, 564.28), (1, 11, 65.47, 553.74), (1, 12, 52.53, 530.26)]]

    # N = raw_input()
    # C = raw_input()
    # PFC = raw_input()
    # MSBFTY
    # T = raw_input()
    # F = raw_input()
    # P = raw_input()
    # prop = []
    living_house = (1,1, 9999999, 9999999999)
    if(P > 15):
        sys.exit(0)

    for year in range(0, N):
        for month in range(0,12):
            # determine if move
            for houses in prop:
                for current_state in houses:
                    if((year < current_state[0]) or (month < current_state[1])):
                        continue
                if(living_house(2) > current_state(2)):
                    if(living_house(3) > current_state(3)):




# [(1, 1, 72.62, 741.97), (1, 6, 67.66, 646.20), (1, 7, 58.83, 563.79), (1, 10, 57.95, 526.55), (1, 12, 62.73, 656.49)]
# [(1, 1, 80.65, 832.35), (1, 11, 92.79, 951.74), (1, 12, 102.73, 975.86)]
# [(1, 1, 111.34, 976.17), (1, 3, 105.85, 895.93), (1, 7, 110.76, 920.65), (1, 10, 102.63, 887.31), (1, 11, 104.72, 1094.79), (1, 12, 94.91, 898.43)]
#[(1, 1, 67.15, 564.28), (1, 11, 65.47, 553.74), (1, 12, 52.53, 530.26)]]


            
        
