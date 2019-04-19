# TravelingSalesmanProblemGA
Class project for the course 3510: Design and Analysis of Algorithms. Using Genetic Algorithms to solve the TSP.
Algorithm:
Distance precomputed and stored in a matrice. where d[i][j] means distance between city i and j. This saves lot of time as calculating distance every time can really slow down this algorithm.

Fitness is defined as 1/(totaldistance). To calculate fitness of an individual distances are lokked up from the distance matrix and added and the total distance arrived at is inverted.

Random intialisation done. (Possible a greedy one will be better. Thinking about how to implement it)
Tournament selection: Size of tournaments is taken as 2.

Crossover: Ordered crossover employed. Crossover rate of 0.6

Mutation: Swap mutation employed. Mutation rate of 0.3.

Elitism: Some members of population are saved for next generation. Elitism rate of 0.1.

Size of population: 3000

Please acknowledge me if you use any of the functions in this script. Thanks!

Mat-test.txt is the input file.

tsp-3510.py is the script file.

mat-output.py is the output text file which has the cost on first line and the optimum tour on second line.

Navigate to this folder on terminal and type to run this project:

python tsp-3510.py mat-test.txt mat-output.txt 300
