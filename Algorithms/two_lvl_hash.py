#############################################
# Louis Falk Knudsen                        #
# Basic hash algorithm and hash dictionary  #
# implementation                            #
#############################################

import os
import random
import copy

# Clears the terminal
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# mod-multiply hash algorithm
# Somewhere amongst the error handling is the actual thing.
def hash(prime, table_width, a, b, key, universe):
    if (a > 0 and a < (prime - 1) and b >= 0 and b < (prime - 1) and
            prime >= universe and table_width < universe):
        hash_result = ((a * key + b) % prime) % table_width
        if (hash_result <= table_width and hash_result >= 0):
            return hash_result
    return -1

# Linked list entry
class hashed_element():
    def __init__(self, key, next):
        self.key = key
        self.next = next

# Loop through linked list, returning the final element. Input is a hashed_element() object.
def final_list_element(element):
    search_element = element
    while (1):
        if (search_element.next == None):
            return search_element
        search_element = search_element.next

# Count the number of elements in a linked list. Input is a hashed_element() object.
def count_list_elements(element):
    if (element == None):
        return 0
    count = 1
    search_element = element
    while (True):
        if (search_element.next == None):
            return count
        else:
            search_element = search_element.next
            count += 1

# Constructs a two-level hash table, outputting the table itself as a list of lists, and the two
# randomly-chosen parametres for the 1st dimension of the table.
def construct_table(input_set, table_width, prime):
    universe_max = 0
    for i in range(0, len(input_set)):
        if (universe_max < input_set[i]):
            universe_max = input_set[i]
    if (table_width > universe_max):
        return None

    # Construct the first level of the hash table.
    while (True):
        # The random numbers which determine, in part, the hash algorithm's output.
        a = random.randint(1, prime - 1)
        b = random.randint(0, prime - 1)

        # Initialise the 1-dimensional hash table of linked lists.
        hash_table_first_loop = []
        for i in range(0, table_width):
            hash_table_first_loop.append(None)

        # Loop through each element of the input, hashing each of them.
        for i in range(0,len(input_set)):
            level_one_index = hash(prime, table_width, a, b, input_set[i], universe_max)
            if (level_one_index == -1):
                return None
            if (hash_table_first_loop[level_one_index] == None):
                hash_table_first_loop[level_one_index] = hashed_element(input_set[i], None)
            else:
                final_list_element(
                    hash_table_first_loop[level_one_index]).next = hashed_element(input_set[i], None)

        # Count C, which must be less than table_width to proceed. Otherwise, try again with new a and b.
        collisions = 0
        for i in range(0,table_width):
            count = count_list_elements(hash_table_first_loop[i])
            collisions += 0.5 * (count - 1) * count

        if collisions < table_width:
            break

    # Construct the second level of the hash table.
    while(True):
        # The random numbers which determine, in part, the hash algorithm's output.
        a_two = random.randint(1, prime - 1)
        b_two = random.randint(0, prime - 1)

        final_hash_table = [] # list of (normal) lists.
        hash_table_second_loop = copy.deepcopy(hash_table_first_loop) # list of linked lists

        retry = False

        # Initialise the 2-dimensional output hash table. Each sublist's size is dependant on the
        # number of elements which have been hashed to the same 1st-dimension index.
        for i in range(0, table_width):
            count = count_list_elements(hash_table_second_loop[i])
            depth = pow(count, 2)
            final_hash_table.append([])
            for j in range(0, depth):
                final_hash_table[i].append(None)

            if (count > 0):
                for j in range(0, count):
                    key = hash_table_second_loop[i].key
                    hash_table_second_loop[i] = hash_table_second_loop[i].next
                    level_two_index = hash(prime, depth, a_two, b_two, key, universe_max)
                    if (level_two_index == -1):
                        return None

                    if (final_hash_table[i] == [] or final_hash_table[i] == None
                            or final_hash_table[i][level_two_index] == None):
                        final_hash_table[i][level_two_index] = key # Place a key in its place.
                    else:
                        retry = True

        if (retry == False):
            break

    return final_hash_table, a, b

# Helper functions to show the above program working:
def print_hash_table(table):
    for i in range(0, len(table)):
        print_string = "|"

        for j in range(0, len(table[i])):
            if (table[i][j] == None):
                print_string += " __ "
            else:
                print_string += " " + str(table[i][j]) + ""

        print(print_string)

def hash_lookup(hash_table, key, a, b, table_width, prime, universe_max):
    index = hash(prime, table_width, a, b, key, universe_max)
    if (index != -1):
        for i in range(0, len(hash_table[index])):
            if (hash_table[index][i] == key):
                return True
    return False

def list_lookup(hash_table, key):
    flat_hash_table = []
    for i in hash_table:
        for j in i:
            flat_hash_table.append(j)
    return (flat_hash_table.count(key) > 0)

# Example of use:
input = [10,15,20,25,30,35,40,45,50,55,60,65,70]
table_width = 10 # Must be less than max(input). Size of the 1st dimension of the hash table.
prime = 89 # Must be greater or equal to max(input), and a prime number.

hash_table, a, b = construct_table(input, table_width, prime)

if (hash_table != None):
    print_hash_table(hash_table)
    print(hash_lookup(hash_table, 10, a, b, table_width, prime, max(input)))
    print(list_lookup(hash_table, 10))