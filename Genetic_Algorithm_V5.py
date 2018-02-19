# Genetic_Algorithm_V5.py

from tkinter import *
import random
import time


class Individual:
   gene_set = ("abcdefghijklmnopqrstuvwxyz ")
   target = "amber marzheuser"

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
max_fitness = Label(root, text = "Max Fitness: ")
max_fitness.grid(row = 0, column = 0, sticky = "E")
gen_count_label = StringVar()
generation = Label(root, textvariable = gen_count_label)
generation.grid(row = 1, column = 0, sticky = "E")
mutation_rate = Label(root, text = "Mutation Rate: ")
mutation_rate.grid(row = 2, column = 0, sticky = "E")
pop_size_display = Label(root, text = "Population Size: ")
pop_size_display.grid(row = 3, column = 0, sticky = "E")
pop_display = Text(root, height = 10, width = 20, font = "monospace 14 bold")
pop_display.grid(row = 0, column = 2, columnspan = 2, rowspan = 10, pady = 5, padx = 5, sticky = "E")
#pop_display.insert(END, "test\nhi\nabc\n123")
#pop_display.delete('1.0', '1.2')

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

   '''Display fittest members:------------------------------'''   
   gen_count += 1
   gen_count_label.set("Generation: " + str(gen_count))
   pop_display.delete(1.0, END)
   for i in range(10):
      member =  "".join(population[i].genes)
      pop_display.insert(END, member + "\n")
      root.update()

   




   
