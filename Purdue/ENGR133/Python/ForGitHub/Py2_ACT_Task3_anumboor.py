#!/usr/bin/env python3

'''
===============================================================================
ENGR 133 Program Description 
	Calculate Solar Panel surface area to make a mars rover move.

Assignment Information
	Assignment:     Py3_ACT Task 3
	Author:         Anurag Numboori, anumboori@purdue.edu
	Team ID:        003-10
	
Contributor:    Name, login@purdue [repeat for each]
	My contributor(s) helped me:	
	[ ] understand the assignment expectations without
		telling me how they will approach it.
	[ ] understand different ways to think about a solution
		without helping me plan my solution.
	[ ] think through the meaning of a specific error or
		bug present in my code without looking at my code.
	Note that if you helped somebody else with their code, you
	have to list that person as a contributor here as well.
===============================================================================
'''

def solarPanelArea(P,E,n):
    A_c = (P)/(n*E)
    return(A_c)
def distanceRover(speed_m,time_seconds):
    distance = speed_m * time_seconds
    return(distance)
def main():
    speed_cm  = 1
    speed_m = speed_cm / 100
    time_hours = 2
    time_seconds = time_hours * 60 * 60
    P = 100
    E = 590
    n = 0.25
    surface_area = solarPanelArea(P,E,n)
    distance = distanceRover(speed_m,time_seconds)
    print(f'Surface Area = {surface_area}')
    print(f'Distance = {distance}')
main()

'''
===============================================================================
ACADEMIC INTEGRITY STATEMENT
    I have not used source code obtained from any other unauthorized
    source, either modified or unmodified. Neither have I provided
    access to my code to another. The project I am submitting
    is my own original work.
===============================================================================
'''