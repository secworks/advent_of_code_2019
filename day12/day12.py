#!/usr/bin/env python3
#=======================================================================
# Solutions to Advent of Code 2019, day 12.
#=======================================================================

DEBUG = False


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def cmp_pos(p1, p2):
    if p1 < p2:
        return (1, -1)
    elif p1 > p2:
        return (-1, 1)
    else:
        return (0, 0)


#-------------------------------------------------------------------
# calc_velo()
# Calculate new velocities for the given planets.
#-------------------------------------------------------------------
def calc_vel(planet1, planet2):
    (pos1, vel1) = planet1
    (pos2, vel2) = planet2

    (dx1, dx2) = cmp_pos(pos1[0], pos2[0])
    vel1[0] += dx1
    vel2[0] += dx2

    (dy1, dy2) = cmp_pos(pos1[1], pos2[1])
    vel1[1] += dy1
    vel2[1] += dy2

    (dz1, dz2) = cmp_pos(pos1[2], pos2[2])
    vel1[2] += dz1
    vel2[2] += dz2

    return ((pos1, vel1), (pos2, vel2))


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def update_vel(i, j, planets):
    pi = planets[i]
    pj = planets[j]

    (dpi, dpj) = calc_vel(pi, pj)

    planets[i] = dpi
    planets[j] = dpj

    return planets

#-------------------------------------------------------------------
#-------------------------------------------------------------------
def update_pos(planet):
    (pos, vel) = planet

    pos[0] += vel[0]
    pos[1] += vel[1]
    pos[2] += vel[2]

    return (pos, vel)


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def update_planets(planets):
    planets = update_vel(0, 1, planets)
    planets = update_vel(0, 2, planets)
    planets = update_vel(0, 3, planets)
    planets = update_vel(1, 2, planets)
    planets = update_vel(1, 3, planets)
    planets = update_vel(2, 3, planets)

    for i in range(4):
        planets[i] = update_pos(planets[i])

    return planets


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def print_planets(planets):
    for i in range(4):
        (pos, vel) = planets[i]
        print("Planet %d: x = %03d, y = %03d, z = %03d, dx = %03d, dy = %03d, dz = %03d" %\
              (i, pos[0], pos[1], pos[2], vel[0], vel[1], vel[2]))
    print("")


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def get_energy(planet):
    (pos, vel) = planet

    pe = abs(pos[0]) + abs(pos[1]) + abs(pos[2])
    ke = abs(vel[0]) + abs(vel[1]) + abs(vel[2])
    return pe * ke

#-------------------------------------------------------------------
#-------------------------------------------------------------------
def get_total_energy(planets):
    esum = 0
    for i in range(4):
        e = get_energy(planets[i])
        esum += e
    return esum


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def run_system(system, iterations):
    print("System at start:")
    print_planets(system)

    for i in range(iterations):
        system = update_planets(system)

    print("System after %d steps:" % iterations)
    print_planets(system)

    esum =  get_total_energy(system)
    print("Total energy: %d" % esum)


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def prob1_test1():

    test_planets1 = [([-1,   0,  2], [0, 0, 0]),
                     ([ 2, -10, -7], [0, 0, 0]),
                     ([ 4,  -8,  8], [0, 0, 0]),
                     ([ 3,   5, -1], [0, 0, 0])]

    print("Test1 for problem 1.")
    run_system(test_planets1, 10)
    print("")


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def prob1_test2():

    test_planets2 = [([-8, -10,  0], [0, 0, 0]),
                     ([ 5,   5, 10], [0, 0, 0]),
                     ([ 2,  -7,  3], [0, 0, 0]),
                     ([ 9,  -8, -3], [0, 0, 0])]

    print("Test2 for problem 1.")
    run_system(test_planets2, 100)
    print("")


#-------------------------------------------------------------------
# problem1
#-------------------------------------------------------------------
def problem1():
    print("Problem 1")

    my_planets = [([14,  4,   5], [0, 0, 0]),
                  ([12, 10,   8], [0, 0, 0]),
                  ([ 1,  7, -10], [0, 0, 0]),
                  ([16, -5,   3], [0, 0, 0])]

    prob1_test1()
    prob1_test2()

    print("Result for problem 1.")
    run_system(my_planets, 1000)
    print("")
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
