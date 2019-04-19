import time
start_time = time.time()
import sys
import math
import random
import pandas as pd

#def main():
	# print command line arguments
	


def dist_calc(C1,C2):
    return math.sqrt((C1[1]-C2[1])**2+(C1[2]-C2[2])**2)

def initialisation(pop_size,City_Order_Std):
    City_Population=[]
    City_Population.append(list(City_Order_Std))
    #print(City_Population)
    for i in range(pop_size-1):
        random.shuffle(City_Order_Std)
        City_Population.append(list(City_Order_Std))
        #print(City_Population)
    return City_Population

def fitness(City_Order):
    fitval=0
    for i in range(len(City_Order)-1):
        fitval=fitval+dist_table[City_Order[i]][City_Order[i+1]]
    fitval+=dist_table[City_Order[-1]][City_Order[0]]
    return 1/fitval

def Selection(method,fitness_array,k):
    sorted_fitness=sorted(fitness_array,reverse=True)
    if method=='Roulette_Wheel':
        max = sum(fitness_array)
        pick = random.uniform(0, max)
        current = 0
        for i,fitness_values in enumerate(sorted_fitness):
            current += fitness_values
            if current > pick:
                return fitness_array.index(fitness_values)
    else:
        val_best=0
        for i in range(k):
            ind = random.randint(0,len(fitness_array)-1)
            if fitness_array[ind] > val_best:
                best = ind
                val_best=fitness_array[best]
        return best


def Crossover(Father,Mother):
    i=random.randint(0,len(Father)-1)
    #j=random.randint(0,len(Mother)-1)
    son=Father[0:i]
    for k in range(len(Mother)):
        if Mother[k] not in son:
            son.append(Mother[k])
    
    
#     daughter=Mother[:i]
#     for k in range(len(Father)):
#         if Father[k] not in daughter:
#             daughter.append(Father[k])
    return son#,daughter

def swapPositions(list, pos1, pos2): 
      
    # popping both the elements from list 
    first_ele = list.pop(pos1)    
    second_ele = list.pop(pos2-1) 
     
    # inserting in each others positions 
    list.insert(pos1, second_ele)   
    list.insert(pos2, first_ele)   
      
    return list

def TSPGA(pop_size,chrom_len,mut_ratio,cross_ratio,method,Tournament_Size,time_limit):
    random.seed(30)
    graph_fitness=[]
    City_Order_Std=[]
    for i in range(chrom_len):
        City_Order_Std.append(i)
    
    City_Population=initialisation(pop_size,City_Order_Std)
    #print(City_Population[0])
    fitness_array=[fitness(City_Populations) for City_Populations in City_Population]
    #print(1/fitness_array[0])
    itr=0
    while (time.time()-start_time<=time_limit):
        itr+=1
#         if itr%20==0:
#             mut_ratio=mut_ratio+0.03
#             cross_ratio=cross_ratio-0.03
        NextGen_City_population=[]
        print("No .of iterations is " +str(itr))    

        #Do Mating based on Cross OVer after selecting parents using roulette wheel


        while(len(NextGen_City_population)<int(cross_ratio*pop_size)):
                Father=City_Population[Selection(method,fitness_array,Tournament_Size)]
                Mother=City_Population[Selection(method,fitness_array,Tournament_Size)]
#                 son,daughter=Crossover(Father,Mother)
#                 NextGen_City_population.append(son)
#                 NextGen_City_population.append(daughter)
                child=Crossover(Father,Mother)
                NextGen_City_population.append(child)
        #print(NextGen_City_population) 
        #Do Swap Mutation
        
        while(len(NextGen_City_population)<int((cross_ratio+mut_ratio)*pop_size)):
            Parent=City_Population[Selection(method,fitness_array,Tournament_Size)]
            #x=random.randint(0,pop_size-1)
            y=random.randint(0,chrom_len-1)
            z=y
            while(z!=y):
                z=random.randint(0,chrom_len-1)
            NextGen_City_population.append(swapPositions(Parent,y,z))
        
        #Choose Elite Population:
        elites=sorted(fitness_array)
        #print(1/elites[-1])
        
        while(len(NextGen_City_population)<pop_size):
            NextGen_City_population.append(City_Population[fitness_array.index(elites.pop())])

        fitness_array=[fitness(NextGen_City_populations) for NextGen_City_populations in NextGen_City_population]

        fittest=max(fitness_array)
        #print(1/fittest)
        graph_fitness.append(fittest)

        # if fittest>(1/28000):
        #     print("Hurray")
        #     return (NextGen_City_population[fitness_array.index(fittest)],graph_fitness)

        City_Population=NextGen_City_population
    return (NextGen_City_population[fitness_array.index(fittest)],graph_fitness)

#Main Body
city_list=pd.read_csv(sys.argv[1],sep=" ",header=None)
dist_table=[]
for i in range(len(city_list)):
    temp_list=[]
    for j in range(len(city_list)):
        temp_list.append(dist_calc(city_list.iloc[i,:],city_list.iloc[j,:]))
    dist_table.append(temp_list)
chrom_len=len(city_list)
pop_size=100*(chrom_len+1)
mut_ratio=0.3
cross_ratio=0.6
elite_ratio=0.1
method="Tournament Selection"
Tournament_Size=2
time_limit=int(sys.argv[3])
result,graph_fitness=TSPGA(pop_size,chrom_len,mut_ratio,cross_ratio,method,Tournament_Size,time_limit)
min_cost=1/fitness(result)
f= open(sys.argv[2],"w+")
f.write("%d\r\n" % min_cost)
for i in range(len(result)):
	f.write("%d " % result[i])

f.close()

# if __name__=="__main__":
# 	main()




