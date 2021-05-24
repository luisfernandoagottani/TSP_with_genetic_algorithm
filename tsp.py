from audioop import cross
from lib2to3.pgen2.pgen import generate_grammar
from charles.charles import Population, Individual
from charles.search import hill_climb, sim_annealing
from charles.selection import fps, tournament
from charles.mutation import swap_mutation, inversion_mutation
from charles.crossover import cycle_co, pmx_co
from data.tsp_data import distance_matrix
from random import choices
from copy import deepcopy
import pandas as pd
import os
import time

def evaluate(self):
    """A simple objective function to calculate distances
    for the TSP problem.

    Returns:
        int: the total distance of the path
    """

    fitness = 0

    for i in range(len(self.representation)):
        # Calculates full distance, including from last city
        # to first, to terminate the trip
        fitness += distance_matrix[self.representation[i - 1]][self.representation[i]]

    return int(fitness)


def get_neighbours(self):
    """A neighbourhood function for the TSP problem. Switches
    indexes around in pairs.

    Returns:
        list: a list of individuals
    """
    n = [deepcopy(self.representation) for i in range(len(self.representation) - 1)]

    for count, i in enumerate(n):
        i[count], i[count + 1] = i[count + 1], i[count]

    n = [Individual(i) for i in n]
    return n


# Monkey patching
Individual.evaluate = evaluate
Individual.get_neighbours = get_neighbours


#First try

#Initialization Hill Climbing, selection = tournament, crossove = cyclo_co, mutate = inversion_mutation

# run
 #if best return best_run representation, best_run fitness and i count

def test_function(n_tests,test_name, initialization, size, gens, select, crossover, mutate, co_p, mu_p, elitism):
    best_score = 10000000000
    best_population = []
    best_scores_list = []
    best_generations_list = []
    if initialization == 'random':
        for testes in range(n_tests):
            pop = Population(
                size=size,
                sol_size=len(distance_matrix[0]),
                valid_set=[i for i in range(len(distance_matrix[0]))],
                replacement=False,
                optim="min",
            )
            pop.evolve(
                gens=gens,
                select= select,
                crossover= crossover,
                mutate=mutate,
                co_p=co_p,
                mu_p=mu_p,
                elitism= elitism
            )
            if pop.individuals[-1].fitness < best_score:
                best_score = pop.individuals[-1].fitness
                best_population = pop.individuals[-1][:]
                best_scores_list = pop.scores
                best_generations_list = pop.generation
            else:
                best_score = best_score
                best_population = best_population
                best_scores_list = best_scores_list
                best_generations_list = best_generations_list
        #Create directory
        directory = test_name
        path = os.path.join(directory)
        if not os.path.isdir(directory):
            os.mkdir(path)    
        #Create Data Frames for scores
        data = {'best_score_list': best_scores_list, 'best_generations_list': best_generations_list}
        df = pd.DataFrame.from_dict(data)
        df.to_excel(directory + '/' + test_name + '_co_p_' + str(co_p) + '_mu_p_'+ str(mu_p) +'.xlsx')

        #Save best score and destinations
        df = data = {'best_score': best_score, 'best_population': best_population}
        df = pd.DataFrame.from_dict(data)
        df.to_excel(directory + '/' + 'Best' + test_name + '_co_p_' + str(co_p) + '_mu_p_'+ str(mu_p) +'.xlsx')

        return best_scores_list, best_generations_list, best_score, best_population

    elif initialization == "hill_climb":
        for testes in range(n_tests):
            pop_initial = Population(
                size=size,
                sol_size=len(distance_matrix[0]),
                valid_set=[i for i in range(len(distance_matrix[0]))],
                replacement=False,
                optim="min",
            )
            hill_climb_initialization = hill_climb(pop_initial)[:]
            pop = Population(
                size=size,
                representation = hill_climb_initialization,
                sol_size=len(distance_matrix[0]),
                valid_set=[i for i in range(len(distance_matrix[0]))],
                replacement=False,
                optim="min",
            )
            pop.evolve(
                gens=gens,
                select=select,
                crossover=crossover,
                mutate=mutate,
                co_p=co_p,
                mu_p=mu_p,
                elitism=elitism
            )
            if pop.individuals[-1].fitness < best_score:
                best_score = pop.individuals[-1].fitness
                best_population = pop.individuals[-1][:]
                best_scores_list = pop.scores
                best_generations_list = pop.generation
            else:
                best_score = best_score
                best_population = best_population
                best_scores_list = best_scores_list
                best_generations_list = best_generations_list
        #Create directory
        directory = test_name
        path = os.path.join(directory)
        if not os.path.isdir(directory):
            os.mkdir(path)    
        #Create Data Frames for scores
        data = {'best_score_list': best_scores_list, 'best_generations_list': best_generations_list}
        df = pd.DataFrame.from_dict(data)
        df.to_excel(directory + '/' + test_name + '_co_p_' + str(co_p) + '_mu_p_'+ str(mu_p) +'.xlsx')

        #Save best score and destinations
        df = data = {'best_score': best_score, 'best_population': best_population}
        df = pd.DataFrame.from_dict(data)
        df.to_excel(directory + '/' + 'Best' + test_name + '_co_p_' + str(co_p) + '_mu_p_'+ str(mu_p) +'.xlsx')

        return best_scores_list, best_generations_list, best_score, best_population

    elif initialization == "sim_annealing":
        for testes in range(n_tests):
            pop_initial = Population(
                size=size,
                sol_size=len(distance_matrix[0]),
                valid_set=[i for i in range(len(distance_matrix[0]))],
                replacement=False,
                optim="min",
            )
            sim_annealing_initialization = sim_annealing(pop_initial)[:]
            pop = Population(
                size=size,
                representation = sim_annealing_initialization,
                sol_size=len(distance_matrix[0]),
                valid_set=[i for i in range(len(distance_matrix[0]))],
                replacement=False,
                optim="min",
            )
            pop.evolve(
                gens=gens,
                select=select,
                crossover=crossover,
                mutate=mutate,
                co_p=co_p,
                mu_p=mu_p,
                elitism=elitism
            )
            if pop.individuals[-1].fitness < best_score:
                best_score = pop.individuals[-1].fitness
                best_population = pop.individuals[-1][:]
                best_scores_list = pop.scores
                best_generations_list = pop.generation
            else:
                best_score = best_score
                best_population = best_population
                best_scores_list = best_scores_list
                best_generations_list = best_generations_list
        #Create directory
        directory = test_name
        path = os.path.join(directory)
        if not os.path.isdir(directory):
            os.mkdir(path)    

        #Create Data Frames for scores
        data = {'best_score_list': best_scores_list, 'best_generations_list': best_generations_list}
        df = pd.DataFrame.from_dict(data)
        df.to_excel(directory + '/' + test_name + '_co_p_' + str(co_p) + '_mu_p_'+ str(mu_p) +'.xlsx')

        #Save best score and destinations
        df = data = {'best_score': best_score, 'best_population': best_population}
        df = pd.DataFrame.from_dict(data)
        df.to_excel(directory + '/' + 'Best' + test_name + '_co_p_' + str(co_p) + '_mu_p_'+ str(mu_p) + '.xlsx')

        return best_scores_list, best_generations_list, best_score, best_population

#Test code

co_p = [0.3, 0.6, 0.8]
mu_p = [0.3, 0.6, 0.8]

start = time.time()
print("hello")
for i in range(len(co_p)):
    for j in range(len(mu_p)):
        test_function(n_tests = 10, 
        test_name= 's100_random_tournament_pmx_co_inversion_mutation',
        initialization = 'random' , 
        size = 100, 
        gens = 100, 
        select = tournament, 
        crossover = pmx_co, 
        mutate = inversion_mutation, 
        co_p = co_p[i], 
        mu_p = mu_p[j],
        elitism = True)
end = time.time()
print(end - start)

        # test_function(n_tests = 10, 
        # test_name= 's100_hill_climp_tournament_pmx_co_inversion_mutation',
        # initialization = 'hill_climb' , 
        # size = 100, 
        # gens = 100, 
        # select = tournament, 
        # crossover = pmx_co, 
        # mutate = inversion_mutation, 
        # co_p = co_p[i], 
        # mu_p = mu_p[j],
        # elitism = True)

        # test_function(n_tests = 10, 
        # test_name= 's100_sim_annealing_tournament_pmx_co_inversion_mutation',
        # initialization = 'sim_annealing' , 
        # size = 100, 
        # gens = 100, 
        # select = tournament, 
        # crossover = pmx_co, 
        # mutate = inversion_mutation, 
        # co_p = co_p[i], 
        # mu_p = mu_p[j],
        # elitism = True)

        # test_function(n_tests = 10, 
        # test_name= 's100_random_tournament_cycle_co_inversion_mutation',
        # initialization = 'random' , 
        # size = 100, 
        # gens = 100, 
        # select = tournament, 
        # crossover = cycle_co, 
        # mutate = inversion_mutation, 
        # co_p = co_p[i], 
        # mu_p = mu_p[j],
        # elitism = True)

        # test_function(n_tests = 10, 
        # test_name= 's100_random_tournament_pmx_co_swap_mutation',
        # initialization = 'random' , 
        # size = 100, 
        # gens = 100, 
        # select = tournament, 
        # crossover = pmx_co, 
        # mutate = swap_mutation, 
        # co_p = co_p[i], 
        # mu_p = mu_p[j],
        # elitism = True)

        # test_function(n_tests = 10, 
        # test_name= 's50_random_tournament_pmx_co_inversion_mutation',
        # initialization = 'random' , 
        # size = 100, 
        # gens = 100, 
        # select = tournament, 
        # crossover = pmx_co, 
        # mutate = inversion_mutation, 
        # co_p = co_p[i], 
        # mu_p = mu_p[j],
        # elitism = True)

        # test_function(n_tests = 10, 
        # test_name= 's100_random_tournament_pmx_co_inversion_mutation_EF',
        # initialization = 'random' , 
        # size = 100, 
        # gens = 100, 
        # select = tournament, 
        # crossover = pmx_co, 
        # mutate = inversion_mutation, 
        # co_p = co_p[i], 
        # mu_p = mu_p[j],
        # elitism = False)

        