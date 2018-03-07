from tkinter import *

class Window:
   def __init__(self):
      #Create Window:
      self.root = Tk()
      self.root.title("Genetic Text Generator")
      self.root.geometry("300x250+500+100")     #(width x height + x_coord + y_coord)
      self.root.resizable(False, False)
      for i in range(4):
         self.root.columnconfigure(i, weight = 1)

      #Declare Variables
      self.reset = False
      self.UI_text = "Input text to generate"
      self.UI_pop_size = 500
      self.UI_mutation = 0.08
      self.generation = StringVar()
      self.highest_fitness = StringVar()
      self.best_match = StringVar()


      #Add things to Window-------------------------------------------------
      #Best Organism:
      best = Label(self.root, textvariable = self.best_match, font = "monospace 14 bold")
      best.grid(column = 0, columnspan = 4, row = 0)



      #Generation:
      generation = Label(self.root, text = "Generation: ")
      generation.grid(column = 0, row = 1, sticky = "E")

      gen_value = Label(self.root, textvariable = self.generation, width = 4)
      gen_value.grid(column = 1, row = 1, sticky = "W")



      #Fitness:
      fitness = Label(self.root, text = "Fitness: ")
      fitness.grid(column = 2, row = 1, sticky = "E")

      fit_value = Label(self.root, textvariable = self.highest_fitness, width = 4)
      fit_value.grid(column = 3, row = 1, sticky = "W")



      #Blank Row:
      blank = Label(self.root, height = 5)
      blank.grid(columnspan = 4, row = 2)



      #Population Size:
      pop_label = Label(self.root, text = "Population Size: ")
      pop_label.grid(column = 0, row = 3, sticky = "E")

      self.pop_entry = Entry(self.root, width = 5)
      self.pop_entry.grid(column = 1, row = 3, sticky = "W")
      self.pop_entry.insert(END, "500")
      


      #Mutation Rate:
      mut_label = Label(self.root, text = "Mutation Rate: ")
      mut_label.grid(column = 0, row = 4, sticky = "E")

      self.mut_entry = Entry(self.root, width = 5)
      self.mut_entry.grid(column = 1, row = 4, sticky = "W")
      self.mut_entry.insert(END, "0.05")



      #Blank Row:
      blank = Label(self.root, height = 3)
      blank.grid(columnspan = 4, row = 5)

      
      #Reset Button:
      def reset_button():
         self.reset = True
         
      reset = Button(self.root, text = "Reset", command = reset_button)
      reset.grid(column = 3, row = 6)

      #Target:
      target_label = Label(self.root, text = "Target: ")
      target_label.grid(column = 0, row = 6)

      self.target_entry = Entry(self.root, width = 10)
      self.target_entry.grid(column = 1, row = 6)
      self.target_entry.insert(END, "Target Text")

      self.root.update()
