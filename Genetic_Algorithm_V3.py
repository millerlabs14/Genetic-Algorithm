# Genetic_Algorithm_V3.py

from tkinter import *
import random
import heapq


class Individual:
   gene_set = ("abcdefghijklmnopqustuvwxyz ")
   target = "william miller"

   def __init__(self):
      self.genes = random.sample(self.gene_set, len(self.target))
      self.mutation_rate = 0.02
      self.fitness = 1
      self.prob = 0

   def Eval_fitness(self):
      fit_score = 0
      for i, gene in enumerate(self.genes):
         if gene == self.target[i]:
            fit_score += 1
      self.fitness = 0.05 + (fit_score / len(self.target))
      

def Calc_probability(pop):
   total = 0
   for member in pop:
      total += member.fitness

   for member in pop:
      member.prob = member.fitness / total

def Select_member(pop):
   #check to see if some members have prob > 0
   total = 0
   for member in pop:
      total += member.prob

   if total == 0:
      for member in pop:
         member.prob = 1 / len(pop)
   else:
      r = random.random()
      index = 0
      while r > 0:
         r = r - pop[index].prob
         index += 1

      return pop[index - 1]

def Breed(parent1, parent2):
   child = Individual()

   for i in range(len(parent1.genes)):
      if i%2 == 0:
         child.genes[i] = parent1.genes[i]
      else:
         child.genes[i] = parent2.genes[i]
   
   chance = random.random()
   if chance <= child.mutation_rate:
      index = random.randint(0, len(child.genes) - 1)
      mutation =  random.sample(child.gene_set, 1)
      child.genes[index] = mutation[0]

   return child




#============================Main Program==============================================
#======================================================================================
#Declare variables------------------------------------------
solution_found = False
pop_size = 300

#Create a initial population--------------------------------
population = []
for i in range(pop_size):
   population.append(Individual())

#Evolve solution--------------------------------------------
for i in range(1):
   '''Evaluate fitness and probability of each member:------'''
   fitness_rank = []
   for member in population:
      member.Eval_fitness()
      fitness_rank.append(member.fitness)
   Calc_probability(population)

   '''Natural selection:------------------------------------'''
   new_pop = []
   for i in range(pop_size):
      parent1 = Select_member(population)
      parent2 = Select_member(population)
      child = Breed(parent1, parent2)
      new_pop.append(child)

#Need to sort population according to fitness : population..sort(key=lambda x: x.fitness)<<<===================================
   population = new_pop

print(max(fitness_rank))
print(population[fitness_rank.index(max(fitness_rank))].genes)
