from tkinter import *

root = Tk()

CHROMOSOMES = 1
ENV_INPUTS = 90
GENERATIONS = 1

scores = [0] * CHROMOSOMES
cdf = [0] * CHROMOSOMES
highest_rating = 0
cdf_sum = 0

height = 20
width = 20
count = 0
clothtextboxes = {}

def clear_clothes():
    for i in range(height*width):
        clothtextboxes[str(i)].delete(0, END)
        clothtextboxes[str(i)].insert(0, "0")

def clear_variables():
    i = 0

    for i in range(CHROMOSOMES):
        scores[i] = 0
        cdf[i] = 0

    highest_rating = 0
    cdf_sum = 0

def evolve():
    chromosome = 0
    env_input = 0
    generation = 0

    clear_variables()
    init_dna_instructions()
    clear_clothes()

    for generation in range(GENERATIONS):
        for env_input in range(ENV_INPUTS):
            for chromosome in range(CHROMOSOMES):
                interpret(env_input, chromosome)
        rate_chromosomes()
        if generation < GENERATIONS:
            reproduce()
            replace_old_population()
            clear_variables()
            clear_clothes()
    
    save_highest_individual()

def init_dna_instructions():
    pass

def interpret(env_input, chromosome):
    pass

def rate_chromosomes():
    pass

def replace_old_population():
    pass

def reproduce():
    pass

def save_highest_individual():
    pass

for i in range(height): # rows
    for j in range(width): # columns
        clothtextboxes[str(count)] = Entry(root, width="2")
        clothtextboxes[str(count)].grid(row=i, column=j)
        clothtextboxes[str(count)].config(justify=CENTER)
        count += 1

evolve()

mainloop()