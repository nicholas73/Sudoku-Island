import sudoku
import random
import time
import itertools
import collections

"""
The Sort functions test for valid single solution puzzles per difficulty level,
roughly determined by the number of squares possibly revealed by basic solving techniques.
In addition, they screen for enjoyable puzzles by checking for number of starting
clues, max/min clues per row/column, and number of types of digits initially revealed.
These tests, in addition to conditions set in the puzzle generator, up the chances
that a unique puzzle is produced.  Finally, the puzzled is solved repeatedly in random
order to check for duplicate solutions."""

def easySort(grid):

    values = sudoku.parse_grid(grid)

    if not all(len(values[s]) == 1 for s in values):
        return False

    for i in range(9):
        row_sum = 0
        col_sum = 0
        for j in range(9):
            if grid[i*9 + j] != '.':
                row_sum += 1
            if grid[i + j*9] != '.':
                col_sum += 1
        if row_sum > 7 or row_sum < 2 or col_sum > 7 or col_sum < 2:
            return False

    givens = 0
    for i in range(len(grid)):
        if grid[i] != '.':
            givens += 1
    if givens > 36:
        return False

    initials = set(list(grid))
    initials.remove('.')

    if not len(initials) >= 8:
        return False

    solutions = []
    for i in range(5):
        list_values = []
        dict_values = sudoku.searchMultiple(values)
        for s in sudoku.squares:
            list_values.append(dict_values[s])
        solution = "".join(list_values)
        solutions.append(solution)
    if len(set(solutions)) > 1:
        return False

    return True

def mediumSort(grid):

    values = sudoku.parse_grid(grid)

    for i in range(9):
        row_sum = 0
        col_sum = 0
        for j in range(9):
            if grid[i*9 + j] != '.':
                row_sum += 1
            if grid[i + j*9] != '.':
                col_sum += 1
        if row_sum > 7 or row_sum < 2 or col_sum > 7 or col_sum < 2:
            return False

    givens = 0
    for i in range(len(grid)):
        if grid[i] != '.':
            givens += 1
    if givens > 33:
        return False

    initials = set(list(grid))
    initials.remove('.')

    if not len(initials) >= 8:
        return False

    solved = 0
    for s in values:
        if len(values[s]) == 1:
            solved += 1

    if solved < 81 and solved < 61:
        return False

    solutions = []
    for i in range(30):
        list_values = []
        dict_values = sudoku.searchMultiple(values)
        for s in sudoku.squares:
            list_values.append(dict_values[s])
        solution = "".join(list_values)
        solutions.append(solution)
        if len(set(solutions)) > 1:
            return False

    return True

def hardSort(grid):

    values = sudoku.parse_grid(grid)

    for i in range(9):
        row_sum = 0
        col_sum = 0
        for j in range(9):
            if grid[i*9 + j] != '.':
                row_sum += 1
            if grid[i + j*9] != '.':
                col_sum += 1
        if row_sum > 7 or row_sum < 2 or col_sum > 7 or col_sum < 2:
            return False

    givens = 0
    for i in range(len(grid)):
        if grid[i] != '.':
            givens += 1
    if givens > 33:
        return False

    initials = set(list(grid))
    initials.remove('.')

    if not len(initials) >= 8:
        return False

    solved = 0
    for s in values:
        if len(values[s]) == 1:
            solved += 1

    if solved > 60 or solved < 45:    
        return False

    solutions = []
    for i in range(99):
        list_values = []
        dict_values = sudoku.searchMultiple(values)
        for s in sudoku.squares:
            list_values.append(dict_values[s])
        solution = "".join(list_values)
        solutions.append(solution)
        if len(set(solutions)) > 1:
            return False

    return True

def extremeSort(grid):

    values = sudoku.parse_grid(grid)

    for i in range(9):
        row_sum = 0
        col_sum = 0
        for j in range(9):
            if grid[i*9 + j] != '.':
                row_sum += 1
            if grid[i + j*9] != '.':
                col_sum += 1
        if row_sum > 7 or row_sum < 2 or col_sum > 7 or col_sum < 2:
            return False

    givens = 0
    for i in range(len(grid)):
        if grid[i] != '.':
            givens += 1
    if givens > 33:
        return False

    initials = set(list(grid))
    initials.remove('.')

    if not len(initials) >= 8:
        return False

    solved = 0
    for s in values:
        if len(values[s]) == 1:
            solved += 1

    if solved > 45:    
        return False

    solutions = []
    for i in range(99):
        list_values = []
        dict_values = sudoku.searchMultiple(values)
        for s in sudoku.squares:
            list_values.append(dict_values[s])
        solution = "".join(list_values)
        solutions.append(solution)
        if len(set(solutions)) > 1:
            return False

    return True

"""
The Solutions Test function finds the most common sources of multiple solution puzzles
by finding all possible 2x2, 3x3, 2x3, and 3x2 combinations where the numbers can be swapped.
Once the combinations are identified, the individual squares (0-80) are randomly selected
weighted by occurance, and stored in the list must_index[].  A minimum number of squares are
selected as a single revealed square prevents an entire combination from swapping, and by
probability a square that eliminates multiple combinations would be chosen."""

def solutionsTest(solution):
    column_index = [ [[0,9,18,27,36,45,54,63,72], [1,10,19,28,37,46,55,64,73], [2,11,20,29,38,47,56,65,74]], [[3,12,21,30,39,48,57,66,75],
                    [4,13,22,31,40,49,58,67,76], [5,14,23,32,41,50,59,68,77]], [[6,15,24,33,42,51,60,69,78], [7,16,25,34,43,52,61,70,79],
                    [8,17,26,35,44,53,62,71,80]] ]
    row_index = [ [[0,1,2,3,4,5,6,7,8], [9,10,11,12,13,14,15,16,17], [18,19,20,21,22,23,24,25,26]], [[27,28,29,30,31,32,33,34,35],
                 [36,37,38,39,40,41,42,43,44], [45,46,47,48,49,50,51,52,53]], [[54,55,56,57,58,59,60,61,62], [63,64,65,66,67,68,69,70,71],
                 [72,73,74,75,76,77,78,79,80]] ]

    column_combo2 = []
    row_combo2 = []
    must_index = []
    combo_list = []
    found3x3 = []

    # find 2x2
    for i in range(3):
        column_combo2.append(map(list, list(itertools.combinations(column_index[i], 2))))
        row_combo2.append(map(list, list(itertools.combinations(row_index[i], 2))))

        for cc in column_combo2[i]:
            col_pairs = map(list, zip(cc[0], cc[1]))
            cp_combo2 = map(list, list(itertools.combinations(col_pairs, 2)))

            for cp in cp_combo2:
                cp_index = cp[0] + cp[1]
                cp_values = [solution[cp_index[0]], solution[cp_index[1]], solution[cp_index[2]], solution[cp_index[3]]]
                if len(set(cp_values)) == 2:
                    combo_list.append(cp_index)
                del cp_index, cp_values

            del col_pairs, cp_combo2

        for rc in row_combo2[i]:
            row_pairs = map(list, zip(rc[0], rc[1]))
            rp_combo2 = map(list, list(itertools.combinations(row_pairs, 2)))

            for rp in rp_combo2:
                rp_index = rp[0] + rp[1]
                rp_values = [solution[rp_index[0]], solution[rp_index[1]], solution[rp_index[2]], solution[rp_index[3]]]
                if len(set(rp_values)) == 2:
                    must_index.append(random.choice(rp_index))
                del rp_index, rp_values

            del row_pairs, rp_combo2


    # find 3x3
        column_combo3 = column_index[i]
        row_combo3 = row_index[i]

        col_trips = map(list, zip(column_combo3[0], column_combo3[1], column_combo3[2]))
        ct_combo3 = map(list, list(itertools.combinations(col_trips, 3)))

        for ct in ct_combo3:
            ct_index = ct[0] + ct[1] + ct[2]
            ct_values = [solution[ct_index[0]], solution[ct_index[1]], solution[ct_index[2]], solution[ct_index[3]], solution[ct_index[4]],
                         solution[ct_index[5]], solution[ct_index[6]], solution[ct_index[7]], solution[ct_index[8]]]
            if len(set(ct_values)) == 3:
                found3x3.append(ct_index)
                combo_list.append(ct_index)
            del ct_index, ct_values

        del col_trips, ct_combo3

    # find 3x2
        for rc in row_combo2[i]:
            row_pairs = map(list, zip(rc[0], rc[1]))
            rp_combo3 = map(list, list(itertools.combinations(row_pairs, 3)))

            for rp in rp_combo3:
                rp_index = rp[0] + rp[1] + rp[2]
                rp_values = [ solution[rp_index[0]], solution[rp_index[1]], solution[rp_index[2]], solution[rp_index[3]], solution[rp_index[4]],
                             solution[rp_index[5]] ]
                if len(set(rp_values)) == 3:
                    if found3x3:
                        not3x3 = []
                        for f in found3x3:
                            not3x3.append(set(f).intersection(set(rp_index)) != set(rp_index))  # makes sure not already part of 3x3
                        if all(not3x3):      
                            combo_list.append(rp_index)
                    else:
                        combo_list.append(rp_index)
                del rp_index, rp_values

            del row_pairs, rp_combo3

        for rc in column_combo2[i]:
            row_pairs = map(list, zip(rc[0], rc[1]))
            rp_combo3 = map(list, list(itertools.combinations(row_pairs, 3)))

            for rp in rp_combo3:
                rp_index = rp[0] + rp[1] + rp[2]
                rp_values = [ solution[rp_index[0]], solution[rp_index[1]], solution[rp_index[2]], solution[rp_index[3]], solution[rp_index[4]],
                             solution[rp_index[5]] ]
                if len(set(rp_values)) == 3:
                    if found3x3:
                        not3x3 = []
                        for f in found3x3:
                            not3x3.append(set(f).intersection(set(rp_index)) != set(rp_index))  # makes sure not already part of 3x3
                        if all(not3x3):      
                            combo_list.append(rp_index)
                    else:
                        combo_list.append(rp_index)
                del rp_index, rp_values

            del row_pairs, rp_combo3

    # find 2x3
        for cc in column_combo2[i]:
            col_pairs = map(list, zip(cc[0], cc[1]))
            cp_combo3 = map(list, list(itertools.combinations(col_pairs, 3)))

            for cp in cp_combo3:
                cp_index = cp[0] + cp[1] + cp[2]
                cp_values = [ solution[cp_index[0]], solution[cp_index[1]], solution[cp_index[2]], solution[cp_index[3]], solution[cp_index[4]],
                             solution[cp_index[5]] ]
                if len(set(cp_values)) == 3:
                    if found3x3:
                        not3x3 = []
                        for f in found3x3:
                            not3x3.append(set(f).intersection(set(cp_index)) != set(cp_index))  # makes sure not already part of 3x3
                        if all(not3x3):      
                            combo_list.append(cp_index)
                    else:
                        combo_list.append(cp_index)
                del cp_index, cp_values

            del col_pairs, cp_combo3

        for cc in row_combo2[i]:
            col_pairs = map(list, zip(cc[0], cc[1]))
            cp_combo3 = map(list, list(itertools.combinations(col_pairs, 3)))

            for cp in cp_combo3:
                cp_index = cp[0] + cp[1] + cp[2]
                cp_values = [ solution[cp_index[0]], solution[cp_index[1]], solution[cp_index[2]], solution[cp_index[3]], solution[cp_index[4]],
                             solution[cp_index[5]] ]
                if len(set(cp_values)) == 3:
                    if found3x3:
                        not3x3 = []
                        for f in found3x3:
                            not3x3.append(set(f).intersection(set(cp_index)) != set(cp_index))  # makes sure not already part of 3x3
                        if all(not3x3):      
                            combo_list.append(cp_index)
                    else:
                        combo_list.append(cp_index)
                del cp_index, cp_values

            del col_pairs, cp_combo3

    # tally index occurances
    combo_set = []                  # remove duplicates of lists of list, which set() cannot do
    for c in combo_list:
        if c not in combo_set:
            combo_set.append(c)

    tally_index = []

    for cl in combo_set:
        tally_index.extend(cl)

    tally_object = collections.Counter(tally_index)
    tally_results = map(list, tally_object.most_common())
    t_counter = 0
    tallies = len(tally_results)
    segments = []
    shuffled_results = []
    for i in range(tallies-1):
        if tally_results[i][1] == tally_results[i+1][1]:
            if i == tallies-2:
                segments.append(tally_results[i-t_counter:])
            else:
                t_counter += 1
        elif tally_results[i][1] != tally_results[i+1][1]:
            if i == tallies-2:
                segments.append(tally_results[i-t_counter:i+1])
                segments.append(tally_results[i+1:])
            else:
                segments.append(tally_results[i-t_counter:i+1])
                t_counter = 0

    for seg in segments:
        random.shuffle(seg)
        shuffled_results.extend(seg)
        
    while combo_set:
        for index in shuffled_results:
            for cl in combo_set:
                if index[0] in cl: 
                    must_index.append(index[0])
                    combo_set.remove(cl)
                    
    return list(set(must_index))

"""    
The Immutable Test searches for longer chains of swappable numbers, by taking any pair of squares
within a cube, and searches for two squares in another cube with identical numbers but also has
either a same row or column.  By finding pairs in different rows/columns that can be swapped, a
single revealed square can cause all of the squares to be unswappable.  The Pair Seeker function
finds all pairs horizontal and vertical, whereas the Test Termination function checks the child
pairs for further swappable pairs.  Once all linked pairs are found, if none of the squares
were in must_index[], one randomly selected square is added to set the squares in place.
"""

def immutableTest(solution, must_index):
    
    cube_index = [ [0,1,2,9,10,11,18,19,20], [3,4,5,12,13,14,21,22,23], [6,7,8,15,16,17,24,25,26], [27,28,29,36,37,38,45,46,47],
                [30,31,32,39,40,41,48,49,50], [33,34,35,42,43,44,51,52,53], [54,55,56,63,64,65,72,73,74],
                [57,58,59,66,67,68,75,76,77], [60,61,62,69,70,71,78,79,80] ]

    pairs_list = []
    index_list = []

    for cube in cube_index:
        masked = []
        for s in cube:
            if s not in must_index:
                masked.append(s)
        pairs_list.extend(map(list, list(itertools.combinations(masked, 2))))

    for p in pairs_list:
        linked_index = testTermination(solution, p)

        if set(linked_index).intersection(set(must_index)):
            for l in linked_index:
                for p in pairs_list:
                    if l in p:
                        pairs_list.remove(p)
        else:

            must_index.extend(random.sample(linked_index, 1))
            for l in linked_index:
                for p in pairs_list:
                    if l in p:
                        pairs_list.remove(p)
                            
def flatten(list_of_lists):
    flat_list = []
    for list in list_of_lists:
        for l in list:
            flat_list.append(l)
    
    return flat_list
        
def testTermination(solution, pair):

    linked_index = []
    linked_index2 = []
    linked_index3 = []
    linked_index4 = []
    
    linked_index = pairSeeker(solution, pair)

    new_index = linked_index[:]

    for lp in new_index:
        linked_index2.extend(pairSeeker(solution, lp))
    
    if set(flatten(linked_index2)) != set(flatten(linked_index)):
        new_index = linked_index2[:]
    else:
        linked_list = list(set(flatten(linked_index)))
        linked_list.extend(pair)
        return linked_list
        
    for lp in new_index:
        linked_index3.extend(pairSeeker(solution, lp))

    if set(flatten(linked_index3)) != set(flatten(linked_index2)):
        new_index = linked_index3[:]
    else:
        linked_list = list(set(flatten(linked_index + linked_index2)))
        linked_list.extend(pair)
        return linked_list

    for lp in new_index:
        linked_index4.extend(pairSeeker(solution, lp))
   
    linked_list = list(set(flatten(linked_index + linked_index2 + linked_index3 + linked_index4))) + pair
    linked_list = list(set(linked_list))
    
    return linked_list
        
def pairSeeker(solution, pair):

    column_index = [ [0,9,18,27,36,45,54,63,72], [1,10,19,28,37,46,55,64,73], [2,11,20,29,38,47,56,65,74], [3,12,21,30,39,48,57,66,75],
                    [4,13,22,31,40,49,58,67,76], [5,14,23,32,41,50,59,68,77], [6,15,24,33,42,51,60,69,78], [7,16,25,34,43,52,61,70,79],
                    [8,17,26,35,44,53,62,71,80] ]

    row_index = [ [0,1,2,3,4,5,6,7,8], [9,10,11,12,13,14,15,16,17], [18,19,20,21,22,23,24,25,26], [27,28,29,30,31,32,33,34,35],
                 [36,37,38,39,40,41,42,43,44], [45,46,47,48,49,50,51,52,53], [54,55,56,57,58,59,60,61,62], [63,64,65,66,67,68,69,70,71],
                 [72,73,74,75,76,77,78,79,80] ]

    cube_index = [ [0,1,2,9,10,11,18,19,20], [3,4,5,12,13,14,21,22,23], [6,7,8,15,16,17,24,25,26], [27,28,29,36,37,38,45,46,47],
                [30,31,32,39,40,41,48,49,50], [33,34,35,42,43,44,51,52,53], [54,55,56,63,64,65,72,73,74],
                [57,58,59,66,67,68,75,76,77], [60,61,62,69,70,71,78,79,80] ]

    linked_index = []

    for i in range(len(column_index)):                                          
        if pair[0] in column_index[i]:                                          # find which column pair[0] is in 
            for j in range(len(column_index[i])):                               # find pair[1] in column[i]
                if solution[pair[1]] == solution[column_index[i][j]]:
                    for k in range(len(cube_index)):                            # find which cube pair[1] is in
                        if pair[1] in cube_index[k]:
                            for l in range(len(cube_index[k])):
                                if solution[pair[0]] == solution[cube_index[k][l]]:
                                    linked_index.append([column_index[i][j], cube_index[k][l]])

        if pair[1] in column_index[i]:                                          # find which column pair[1] is in 
            for j in range(len(column_index[i])):                               # find pair[0] in column[i]
                if solution[pair[0]] == solution[column_index[i][j]]:
                    #linked_index.append(])
                    for k in range(len(cube_index)):                            # find which cube pair[0] is in
                        if pair[0] in cube_index[k]:
                            for l in range(len(cube_index[k])):
                                if solution[pair[1]] == solution[cube_index[k][l]]:
                                    linked_index.append([column_index[i][j], cube_index[k][l]])

    for i in range(len(row_index)):                                          
        if pair[0] in row_index[i]:                                             # find which row pair[0] is in 
            for j in range(len(row_index[i])):                                  # find pair[1] in row[i]
                if solution[pair[1]] == solution[row_index[i][j]]:
                    for k in range(len(cube_index)):                            # find which cube pair[1] is in
                        if pair[1] in cube_index[k]:
                            for l in range(len(cube_index[k])):
                                if solution[pair[0]] == solution[cube_index[k][l]]:
                                    linked_index.append([row_index[i][j], cube_index[k][l]])

        if pair[1] in row_index[i]:                                             # find which row pair[1] is in 
            for j in range(len(row_index[i])):                                  # find pair[0] in row[i]
                if solution[pair[0]] == solution[row_index[i][j]]:
                    #linked_index.append(])
                    for k in range(len(cube_index)):                            # find which cube pair[0] is in
                        if pair[0] in cube_index[k]:
                            for l in range(len(cube_index[k])):
                                if solution[pair[1]] == solution[cube_index[k][l]]:
                                    linked_index.append([row_index[i][j], cube_index[k][l]])

    return linked_index
    
"""
The Generate function pulls a completed puzzle, and determines the starting squares to be revealed.
It first determines which squares have the highest probability of removing multiple solutions.  It
also uses the Cube Number function to guide the number of revealed squares per cube, to produce an
even puzzle.  It also mirrors the revealed squares to produce a symmetric puzzle.
"""

def generate(level):

    initial = []
    
    new_puzzle = sudoku.random_puzzle(81)       # get completed puzzle
    init_puzzle = list(new_puzzle)              # put in list form

    cube_list = [ [0,1,2,9,10,11,18,19,20], [3,4,5,12,13,14,21,22,23], [6,7,8,15,16,17,24,25,26], [27,28,29,36,37,38,45,46,47],
                [30,31,32,39,40,41,48,49,50], [33,34,35,42,43,44,51,52,53], [54,55,56,63,64,65,72,73,74],
                [57,58,59,66,67,68,75,76,77], [60,61,62,69,70,71,78,79,80] ]

    must_index = solutionsTest(new_puzzle)                                  # get 2x2, 2x3, 3x2, 3x3 combinations that must have squares revealed
    immutableTest(new_puzzle, must_index)                                     # find longer combinations
    mirror_index = []                                                       # get symmetric squares
    for index in must_index:
        mirror_index.append(80-index)

    must_index = must_index + list(set(mirror_index))
    initial.extend(must_index)

    init_m = []                                                             # List in reverse order to store mirror
    for i in range(4):
        cube_must = set(must_index).intersection(set(cube_list[i]))         # squares that must be revealed
        cube_init = []
        if cube_must:                                                       # Cubes 0-3
            chosen = list(set(cube_must).intersection(set(cube_list[i])))   # process squares to remove from random selection
            copy = cube_list[i]
            for c in chosen:
                copy.remove(c)
            sample_size = cubeNumber(level)-len(chosen)
            if sample_size < 0:
                sample_size = 0
            cube_init = random.sample(copy, sample_size)      
            initial.extend(cube_init)                                       # Add cubes 0-3 to initial list
            for c in cube_init:
                initial.append(80-c)
        else:     
            cube_init = random.sample(cube_list[i], cubeNumber(level))      # Cubes 0-3
            initial.extend(cube_init)                                       # Add cubes 0-3 to initial list
            for c in cube_init:
                initial.append(80-c)
    cube_must4 = set(must_index).intersection(set(cube_list[4]))
    size = cubeNumber(level)                                                # Cube 4, determine number of boxes shown
    if cube_must4:
        if size > len(cube_must4):
            size = size - len(cube_must4)
        else: size = 0
        chosen = list(set(cube_must4).intersection(set(cube_list[4][:4])))  # process squares to remove from random selection
        copy = cube_list[4][:4]
        for c in chosen:
            copy.remove(c)
        cube4_03 = random.sample(copy, size/2)                              # First 4 boxes
    else:
        cube4_03 = random.sample(cube_list[4][:4], size/2)                  # First 4 boxes
    index4 = []
    for s in cube4_03:
        index4.append(cube_list[4].index(s))                                # Find index and add to list
    if size % 2 == 1:
        cube4_4 = cube_list[4][4]                                           # Fill center box if size is odd
    else:
        cube4_4 = ""
    cube4_58 = []
    for n in index4:
        cube4_58.append(cube_list[4][8-n])                                  # Mirror first 4 boxes
    cube4 = cube4_03
    cube4.append(cube4_4)
    cube4.extend(cube4_58)                                                  # Glue together middle box initials
    initial.extend(cube4)                                                   # Add cube 4 to initials
        
    for i in range(len(init_puzzle)):
         if i not in initial:
            init_puzzle[i] = '.'
    
    init_puzzle = "".join(init_puzzle)

    return init_puzzle, new_puzzle

"""
The Cube Number function is a probability distribution function that determines the number
of squares to reveal per cube, depending on difficulty level.  It is not the only factor that
determines difficulty, but evenness influences the human solvability of the puzzle.
"""
def cubeNumber(level):

    weights = {}

    weights["Easy"] = {"1" : 0, "2" : 15, "3" : 35, "4" : 35, "5" : 15}          # avg 31.5
    weights["Medium"] = {"1" : 0, "2" : 20, "3" : 35, "4" : 30, "5" : 15}       # avg 30.6
    weights["Hard"] = {"1" : 5, "2" : 20, "3" : 30, "4" : 30, "5" : 15}          # avg 29.7
    weights["Extreme"] = {"1" : 5, "2" : 25, "3" : 30, "4" : 25,  "5" : 15}     # avg 28.8

    distribution = []

    for x in weights[level].keys():
        distribution += weights[level][x] * x

    number = int(random.choice(distribution))

    return number

"""
Time Sampler is a rough gauge of puzzle difficulty by measuring how long it takes for
a brute force solver to finish.
"""
def timeSampler():

    timeE = []
    timeM = []
    timeH = []
    timeX = []
    
    for i in range(100):
        puzzle, solution = generate("Easy")
        start_time = time.clock()
        dict_values = sudoku.solve(puzzle)
        timeE.append(time.clock() - start_time)

        puzzle, solution = generate("Medium")
        start_time = time.clock()
        dict_values = sudoku.solve(puzzle)
        timeM.append(time.clock() - start_time)

        puzzle, solution = generate("Hard")
        start_time = time.clock()
        dict_values = sudoku.solve(puzzle)
        timeH.append(time.clock() - start_time)

        puzzle, solution = generate("Extreme")
        start_time = time.clock()
        dict_values = sudoku.solve(puzzle)
        timeX.append(time.clock() - start_time)

    times = {'Easy' : timeE, 'Medium' : timeM, 'Hard' : timeH, 'Extreme' : timeX}

    return times



