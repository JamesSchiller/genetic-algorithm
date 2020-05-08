from tkinter import *

root = Tk()

CHROMOSOMES = [
    [0, 0, 0, 0], 
    [0, 1, 0, 1], 
    [1, 0, 1, 0], 
    [1, 1, 1, 0], 
    [0, 0, 1, 1], 
    [1, 1, 0, 0], 
    [1, 0, 1, 0], 
    [0, 0, 1, 1], 
    [0, 0, 0, 0], 
    [0, 1, 0, 1]
]

ENV_INPUTS = [
    "square", "s", "z", "T", "L", "J", "l", "square", "s", "z", "T", "L", "J", "l", "s", "z", "T", "L", "J", "l", "square", "square", "square", "square", "T", "L", "s", "s", 
    "z", "z", "z", "T", "T", "L", "z", "J", "I", "I", "I", "I", "square", "square", "z", "s", "I", "s", "l", "J", "T", "z", "square", "s", "s", "s", "l", "J", "J", "I", "l", "J", "J", 
    "I", "L", "J", "l", "square", "square", "square", "square", "T", "T", "T", "L", "z", "J", "I", "I", "I", "I", "square", "square", "J", "J", "T", "s", "l", "J", "T", "z", 
    "square", "s", "s", "s", "l", "T", "z", "z", "J", "square", "l", "T", "z", "z", "J", "square", "l", "T", "z", "z", "J", "square", "square", "J", "J", "L", "s", "z", "l", "J", 
    "J", "L", "s", "z", "l", "square", "s", "square", "s", "J", "J", "L", "s", "z", "l", "L", "L", "s", "s", "I", "z", "z", "z", "L", "s", "z", "l", "square", "s", "square", "s", "J", 
    "J", "L", "s", "z", "T", "L", "J", "l", "s", "z", "T", "L", "J", "l", "square", "z", "T", "L", "J", "l", "s", "z", "T", "L", "J", "l", "square", "T", "T", "L", "L", "s", "z", "l", "square", 
    "T", "L", "L", "s", "z", "T", "L", "L", "s", "z", "T", "L", "L", "s", "z", "s", "s", "s", "s", "s", "s", "z", "z", "z", "z", "L", "L", "T", "T", "z", "z", "L", "L", "T", "square", "z", "square", 
    "z", "square", "z", "square", "z", "square", "z", "square", "z", "s", "s", "s", "s", "s", "s", "L", "T", "T", "L", "l", "l", "l", "l", "l", "l", "l", "l", "square", "z", "square", 
    "z", "s", "s", "square", "z", "square", "z", "s", "s", "l", "T", "l", "L", "l", "T", "l", "L", "l", "T", "l", "L", "square", "z", "L", "T", "l", "l", "s", "z", "z", "L", "T", "l", "l", "s", 
    "L", "l", "T", "l", "L", "square", "z", "L", "T", "l", "l", "s", "z", "z", "L", "T", "l", "l", "s", "square", "s", "z", "T", "L", "J", "l", "square", "s", "z", "T", "L", "J", "l", "s", "z", 
    "T", "L", "J", "l", "square", "square", "square", "square", "T", "L", "s", "s", "z", "z", "z", "T", "T", "L", "z", "J", "I", "I", "I", "I", "square", "square", "z", "square", 
    "s", "z", "T", "L", "J", "l", "square", "s", "z", "T", "L", "J", "l", "s", "z", "T", "L", "J", "l", "square", "square", "square", "square", "T", "L", "s", "s", "z", "z", "z", "T", "T", 
    "L", "z", "J", "I", "I", "I", "I", "square", "square", "z", "l", "l", "z", "J", "I", "I", "T", "T", "L", "z", "J", "I", "I", "I", "I", "square", "square", "z", "l", "l", "z", "z", "T", 
    "T", "L", "z", "J", "I", "I", "I", "I", "square", "square", "z", "s", "I", "s", "l", "J", "T", "z", "square", "s", "s", "s", "l", "J", "J", "I", "l", "J", "J", "I", "L", "J", "l", "square", 
    "square", "square", "s", "s", "s", "T", "J", "I", "l", "J", "J", "I", "L", "J", "l", "square", "T", "s", "l", "J", "T", "z", "square", "s", "s", "s", "l", "T", "z", "z", "J", "square", 
    "l", "T", "z", "z", "J", "square", "l", "T", "z", "z", "J", "square", "square", "J", "J", "L", "s", "z", "l", "J", "J", "L", "s", "z", "l", "square", "s", "square", "s", "J", "J", "L", 
    "T", "T", "L", "l", "l", "l", "l", "l", "l", "l", "l", "square", "z", "square", "z", "L", "L", "T", "T", "square", "square", "z", "z", "z", "z", "z", "T", "L", "J", "l", "square", 
    "square", "square", "square", "T", "L", "s", "s", "z", "z", "z", "square", "J", "L", "T", "T", "L", "l", "l"
]

GENERATIONS = 1

scores = [0] * len(CHROMOSOMES)
cdf = [0] * len(CHROMOSOMES)
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

    for i in range(len(CHROMOSOMES)):
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
        for env_input in ENV_INPUTS:
            for chromosome in CHROMOSOMES:
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
    value_of_gene1 = binary_to_decimal(chromosome[0], chromosome[1])
    value_of_gene2 = binary_to_decimal(chromosome[2], chromosome[3])
    pass

def rate_chromosomes():
    pass

def replace_old_population():
    pass

def reproduce():
    pass

def save_highest_individual():
    pass

def binary_to_decimal(high, low):
 res = 0
 if high == 1: res += 2
 if low == 1: res += 1

 return res

for i in range(height): # rows
    for j in range(width): # columns
        clothtextboxes[str(count)] = Entry(root, width="2")
        clothtextboxes[str(count)].grid(row=i, column=j)
        clothtextboxes[str(count)].config(justify=CENTER)
        count += 1

evolve()

mainloop()