# GLOBAL VARIABLES
import random
global_debug = False
global_base = 6
global_array_size = 8

# ======================================================================
def instanciate_new_array(p_random):
    new_arr = []
    for x in range(0, global_array_size):
        if p_random:
            new_arr.append(random.randint(1, global_base))
        else:
            new_arr.append(0)
    return new_arr

# ======================================================================
def compose_number_from_array(p_array):
    composed_number = 0

    print("Composing from array:")
    print("Original array:", p_array)
    for x in p_array:
        composed_number = composed_number * global_base + x
        if global_debug:
            print("DEBUG:", composed_number)

    print("Composed number =", composed_number)
    return composed_number

# ======================================================================
def decompose_number_into_array(p_composed_number):
    result_arr = instanciate_new_array(False)

    print("Decomposing from number:")
    print("Composed number =", p_composed_number)
    for i in range(1, global_array_size+1):
        p_composed_number, result_arr[global_array_size-i] = divmod(p_composed_number, global_base)
        if result_arr[global_array_size-i] == 0:
            result_arr[global_array_size-i] = global_base
            p_composed_number -= 1
        if global_debug:
            print("DEBUG: i =", i, "result_arr =", result_arr[global_array_size-i], "p_composed_number =", p_composed_number)

    print("Decomposed array =", result_arr)
    return result_arr

# =====================================================================
# MAIN TEST CODE
# =====================================================================
in_arr = instanciate_new_array(True)

compose_result = compose_number_from_array(in_arr)
out_arr = decompose_number_into_array(compose_result)
if in_arr == out_arr:
    print("It works! :D")
else:
    print("Didn't work! :'(")
