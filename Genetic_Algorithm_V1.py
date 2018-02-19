# Genetic_Algorithm_V1.py

import random
import heapq

class Individual:
   gene_set = ("abcdefghijklmnopqustuvwxyz"
            +  "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            +  " !@#$%^&*()-_+=")
   target = "William Miller"

   def __init__(self):
      self.genes   = random.sample(self.gene_set, len(self.target)) 
      self.fitness = 1
      self.prob    = 0

   def Eval_fitness(self):
      fit_score = 0
      for i, gene in enumerate(self.genes):
         if gene == self.target[i]:
            fit_score += 1
      self.fitness = round(fit_score / len(self.target), 3)
      

def Calc_probability(pop):
   total = 0
   for member in pop:
      total += member.fitness

   if total == 0: total = 1 #prevent division by 0 if all members have 0 fitness

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
      '''
      index = 0
      r = random(1)
      while r > 0:
         r = r - pop[index].prob
         index += 1

      return pop[index - 1]

   return(pop[1])

def Breed(parent1, parent2):
   pass

#Declare variables------------------------------------------
solution_found = False
pop_size = 10

#Create a initial population--------------------------------
population = []
for i in range(5):
   population.append(Individual())

#Evolve solution--------------------------------------------
'''Evaluate fitness and probability of each member:------'''
for member in population:
   member.Eval_fitness()
Calc_probability(population)

'''Natural selection:------------------------------------'''
new_pop = []
for i in range(pop_size):
   parent1 = Select_member(population)
   parent2 = Select_member(population)

   child = Breed(parent1, parent2)
   new_pop.append(child)


for i, member in enumerate(population):
   print("member {}:-----------------------------------------------".format(i))
   print(member.genes)
   print("fitness: ", member.fitness, " : ", "prob: ", member.prob)
   print("")
