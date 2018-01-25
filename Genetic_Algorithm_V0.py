# Genetic_Algorithm_V0.py

import random
import heapq

class Individual:
   gene_set = ("abcdefghijklmnopqustuvwxyz"
            +  "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            +  " !@#$%^&*()-_+=")
   target = "William Miller"

   def __init__(self):
      self.genes   = random.sample(self.gene_set, len(self.target)) 
      self.fitness = self.Eval_fitness()

   def Eval_fitness(self):
      fitness = 0
      for i, gene in enumerate(self.genes):
         if gene == self.target[i]:
            fitness += 1
      fitness /= len(self.target)
      
      return round(fitness, 2)


population = []
for i in range(5):
   population.append(Individual())

for member in population:
   print(member.genes)
   print("fitness: ", member.fitness)
