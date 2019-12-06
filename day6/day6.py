#!/usr/bin/env python3
#===================================================================
# Solutions to Advent of Code 2019, day 6.
#===================================================================

#-------------------------------------------------------------------
#-------------------------------------------------------------------
def get_input(filename):
    l = []
    with open(filename,'r') as f:
        for line in f:
            m = line.strip().split(')')
            [c, o] = m
            l.append((c, o))
    return l


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def build_tree(orbit_name, depth, orbits):
    direct_orbits = []
    other_orbits = []
    orbit_list = []

    for o in orbits:
        name, orbit = o
        if name == orbit_name:
            direct_orbits.append(orbit)
        else:
            other_orbits.append(o)

    for name in direct_orbits:
        orbit_list.append(build_tree(name, depth + 1, other_orbits))

    return (orbit_name, depth, orbit_list)


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def get_depth(n):
    name, depth, nodes = n
    nd = 0
    for node in nodes:
        nd += get_depth(node)
    return depth + nd

#-------------------------------------------------------------------
#-------------------------------------------------------------------
def get_parents(me, orbits):
    (name, depth, children) = orbits
    parents = []
    # We found the final node.
    if name == me:
        return [name]

    # End of wrong path.
    elif len(children) == 0:
        return []

    else:
        for c in children:
            n = get_parents(me, c)
            if len(n) > 0:
                parents.append(name)
                for l in n:
                    parents.append(l)
        if len(parents) > 0:
            return parents
        else:
            return []


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def get_orbitals(santa, me):
    print("Number of my orbitals: %d" % len(me))
    print("Number of santas orbitals: %d" % len(santa))

    # Find common node.
    i = 0
    while santa[i] == me[i]:
        i += 1
    i -= 1
    print("Index for final common orbital: %d" % (i))

    # Calculate number of orbital transfers to common orbital.
    my_orbits = len(me) - i - 2
    santas_orbits = len(santa) - i - 2

    # Calculate total orbital trasfers.
    total_orbits = my_orbits + santas_orbits
    print("Total orbital transfers: %d" % total_orbits)


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def problem1():
    print("Problem 1")
    my_input = get_input("day6_input.txt")
    my_orbits = build_tree("COM", 0, my_input)

    print("Total number of orbits: %d" % (get_depth(my_orbits)))
    print("")


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def problem2():
    print("Problem 2")
    my_input = get_input("day6_input.txt")
    my_orbits = build_tree("COM", 0, my_input)
    santa_parents = get_parents("SAN", my_orbits)

    my_input = get_input("day6_input.txt")
    my_orbits = build_tree("COM", 0, my_input)
    my_parents = get_parents("YOU", my_orbits)

    get_orbitals(santa_parents, my_parents)

#-------------------------------------------------------------------
#-------------------------------------------------------------------
problem1()
problem2()
#===================================================================
