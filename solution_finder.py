''' solution_finder.py
    Auth: Patrick Craig
    Date: 12/30/14
    last modified: 12/30/14
    Purpose: Takes an input representing a target number and returns a list of
    possible arithmetic solutions using +, -, * and / that will generate the
    target number
    Notes: * based on code from ai-junkie.com
           * first time in a long time porting C/C++ to python, so forgive me if
           * the style is... eclectic.
'''
    
from math import *
from time import *
from random import random

crossover_rate = 0.7
mutation_rate = 0.001
pop_size = 100
chromo_length = 300
gene_length = 4
max_allowable_generations = 400

class Chromo_Type
    def init(self, bits="", fitness=0.0):
        self.bits = bits
        self.fitness = fitness

def get_random_bits(length):
    bits = ""
    for i in range(length):
        if random() > 0.5:
            bits += "1"
        else:
            bits += "0"
    
    return bits

def bin_to_dec(bits):
    val = 0
    val_to_add = 1;
    
    # iterating backwards through bits
    for i in range(len(bits)-1, -1, -1):
        if bits[i] == '1':
            val += val_to_add
        
            value_to_add *= 2

    return val
#TODO: return buffer/len tuple
def parse_bits(bits, buff=[]):
    b_operator = True
    this_gene = 0

    for i in range(0, chromo_length, gene_length):
        this_gene = bin_to_dec(bits[i:gene_length])

        # looking for arithmetic operators
        if b_operator:
            if ((this_gene < 10)) || (this_gene > 13)):
                pass
            else:
                b_operator = False
                buff.append(this_gene)
        
        # looking for numbers       
        else:
            if (this_gene > 9):
                pass
            else:
                b_operator = True
                buff.append(this_gene)

    for i in range(0, len(buff)):
        if ((buff[i] == 13) && (buff[i+1] == 0)):
            buff[i] = 10

    return len(buff)

def assign_fitness(bits, target_value):
    buff = []
    num_elements = parse_bits(bits)
    result = 0.0

    for i in range(0, len(num_elements)-1, 2):
        if buff[i] == 10:
            result += buff[i+1]
        elif buff[i] == 11:
            result -= buff[i+1]
        elif buff[i] == 12:
            result *= buff[i+1]
        elif buff[i] == 13:
            result /= buff[i+1]
        else:
            pass

    if result == float(target_value):
        return 0.999
    else:
        return 1.0/fabs(target_value - result)
# resume point
def print_chromo(bits):
    buff = []
    num_elements = parse_bits(bits)

    for i in range(0, num_elements):
        print_gene_symbol(buff

def print_gene_symbol:
    pass
