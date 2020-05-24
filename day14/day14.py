#!/usr/bin/env python3
#=======================================================================
# Solutions to Advent of Code 2019, day 14.
#=======================================================================

import math

#-------------------------------------------------------------------
#-------------------------------------------------------------------
def get_input(filename):
    mix = []
    with open(filename,'r') as f:
        for line in f:
            mix.append(line.strip())
    return mix

#-------------------------------------------------------------------
#-------------------------------------------------------------------
class Node:
    def __init__(self, units, quantity):
        self.name = name
        self.units = units
        self.ingredients = []


    def add_ingredient(self, units, ingredient):
        self.ingredients.append((units, ingredient))


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def extract_ingredients(ing):
    l = []
    for item in ing:
        if item[0] == " ":
            item = item[1:]
        if item[-1] == " ":
            item = item[:-2]

        unit, name = item.split(" ")
        l.append((int(unit), name))
    return l

#-------------------------------------------------------------------
#-------------------------------------------------------------------
def build_db(il):
    ing_db = dict()
    for row in il:
        ingredients, target = row.split("=>")
        tunits, tname = target[1:].split(" ")
        ing_list = extract_ingredients(ingredients.split(","))
        print(tunits, "of", tname, "requires", ing_list)
        ing_db[tname] = ((tunits, ing_list))
    return ing_db

#-------------------------------------------------------------------
#-------------------------------------------------------------------
def get_ore(r, name):
    print(r[name])


#-------------------------------------------------------------------
# problem1
#-------------------------------------------------------------------
def problem1():
    print("Problem 1")
    my_input = get_input("examples/day14_example1.txt")
    my_db = build_db(my_input)
    get_ore(my_db, "FUEL")
    print("")


#-------------------------------------------------------------------
# problem2
#-------------------------------------------------------------------
def problem2():
    print("Problem 2")
    print("")

#-------------------------------------------------------------------
#-------------------------------------------------------------------
problem1()
problem2()

#=======================================================================
