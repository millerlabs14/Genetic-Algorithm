import window
import Population

def Create_pop():
   pop = Population.Population(window.target_entry.get())
   pop.size = int(window.pop_entry.get())
   pop.mutation_rate = float(window.mut_entry.get())
   return pop

window = window.Window()
pop = Create_pop()


while True:
   while not pop.ideal_found:
      pop.Natural_selection()
      pop.Calc_probability()
      pop.Sort()
      
      window.best_match.set("".join(pop.members[0].genes))
      window.generation.set(pop.generation)
      window.highest_fitness.set(int((pop.members[0].fitness / pop.highest_fitness) * 100))
      window.root.update()
      
      pop.generation += 1


      if window.reset == True:
         pop = Create_pop()
         window.reset = False
         
   if window.reset == True:
      pop = Create_pop()
      window.reset = False

   window.root.update()
         
