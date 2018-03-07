import random

#---------------------------------------------------------------------------------------------------
class Individual:
   def __init__(self):
      self.genes = []
      self.fitness = 1
      self.prob = 0



#-----------------------------------------------------------------------------------------------------      
class Population:
   def __init__(self, target):
      self.gene_set = ("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz ")
      self.target = target
      self.members = []
      self.size = 500
      self.mutation_rate = 0.08
      self.cull_count = int(self.size/4)
      self.generation = 0
      self.ideal_found = False
      self.highest_fitness = len(self.target)**2 + 0.05

      for i in range(self.size):
         self.members.append(Individual())
         self.members[i].genes = random.sample(self.gene_set, len(self.target))
         self.Eval_fitness(self.members[i])

      self.Calc_probability()

   def Eval_fitness(self, member):
      match = 0
      for i, gene in enumerate(member.genes):
         if gene == self.target[i]:
            match += 1
            if match == len(member.genes):
               self.ideal_found = True
      member.fitness = 0.05 + (match**2)

   def Calc_probability(self):
      total = 0
      for member in self.members:
         total += member.fitness

      for member in self.members:
         member.prob = member.fitness / total

   def Sort(self):
      self.members.sort(key=lambda x: x.fitness, reverse = True)

   def Natural_selection(self):
      new_members =[]
      
      for i in range(self.cull_count):
         parent1 = self.Select_member()
         parent2 = self.Select_member()
         child = self.Breed(parent1, parent2)
         self.Eval_fitness(child)
         new_members.append(child)
         
      del self.members[self.size - self.cull_count:]
      self.members += new_members

   def Select_member(self):
      total = 0
      for member in self.members:
         total += member.prob

      r = random.random()
      index = 0
      while r > 0:
         r = r - self.members[index].prob
         index += 1

      return self.members[index - 1]

   def Breed(self, parent1, parent2):
      child = Individual()
      child.genes = random.sample(self.gene_set, len(self.target))

      for i in range(len(parent1.genes)):
         if i%2 == 0:
            child.genes[i] = parent1.genes[i]
         else:
            child.genes[i] = parent2.genes[i]
      
      chance = random.random()
      if chance <= self.mutation_rate:
         index = random.randint(0, len(child.genes) - 1)
         mutation = random.sample(self.gene_set, 1)
         child.genes[index] = mutation[0]

      return child
