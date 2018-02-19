# Genetic_Algorithm_V6.py

from tkinter import *
import random
import time


class Individual:
   gene_set = ("abcdefghijklmnopqrstuvwxyz ")
   target = "Amber Marzheuser"

   def __init__(self):
      self.genes = random.sample(self.gene_set, len(self.target))
      self.mutation_rate = 0.05
      self.fitness = 1
      self.prob = 0

      self.Eval_fitness()

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
      mutation = random.sample(child.gene_set, 1)
      child.genes[index] = mutation[0]

   return child




#============================Main Program==============================================
#======================================================================================
#Declare variables------------------------------------------
solution_found = False
pop_size = 1000
kill_number = int(pop_size/4)
gen_count = 0

#Create Window----------------------------------------------
root = Tk()
root.title("Genetic Algorithm")            
root.geometry("610x320")        
root.resizable(False,False)
for i in range(4):
   root.columnconfigure(i, weight = 1)

#Put objects in window--------------------------------------
best_match_value = StringVar()
best_match_display = Label(root, textvariable = best_match_value, font = "monospace 14 bold")
best_match_display.grid(row = 0, column = 0, columnspan = 6)

generation_label = Label(root, text = "Generation:")
generation_label.grid(row = 1, column = 0, sticky = "E")
generation_text = StringVar()
generation_display = Label(root, textvariable = generation_text)
generation_display.grid(row = 1, column = 1, sticky = "W")

fitness_label = Label(root, text = "Fitness:")
fitness_label.grid(row = 1, column = 2, sticky = "E")
fitness_text = StringVar()
fitness_display = Label(root, textvariable = fitness_text)
fitness_display.grid(row = 1, column = 3, sticky = "W")

blank_space = Label(root, text = "", font = "monospace 15")
blank_space.grid(row = 2, column = 0)

pop_size_label = Label(root, text = "Population Size:")
pop_size_label.grid(row = 3, column = 0, sticky = "E")
pop_size_display = Label(root, text = str(pop_size))
pop_size_display.grid(row = 3, column = 1, sticky = "W")

mutation_rate_label = Label(root, text = "Mutation Rate:")
mutation_rate_label.grid(row = 4, column = 0, sticky = "E")
mutation_rate_text = StringVar()
mutation_rate_display = Label(root, text = str(Individual().mutation_rate))
mutation_rate_display.grid(row = 4, column = 1, sticky = "W")

#Create a initial population--------------------------------
population = []
for i in range(pop_size):
   population.append(Individual())

population.sort(key=lambda x: x.fitness, reverse = True)

#Evolve solution--------------------------------------------
while not solution_found:
   '''Evaluate fitness and probability of each member:------'''
   for member in population:
      member.Eval_fitness()
      if member.fitness == 1.05:
         solution_found = True
   Calc_probability(population)

   '''Natural selection:------------------------------------'''
   population.sort(key=lambda x: x.fitness, reverse = True)
   new_members = []
   for i in range(kill_number):
      parent1 = Select_member(population)
      parent2 = Select_member(population)
      child = Breed(parent1, parent2)
      new_members.append(child)
   del population[(len(population)-kill_number):]
   population += new_members

   '''Display values:------------------------------'''   
   gen_count += 1
   best_match_value.set("".join(population[0].genes))
   generation_text.set(str(gen_count))
   fitness_text.set("{}".format(round(population[0].fitness - 0.05, 2 )))
   root.update()

   




   
