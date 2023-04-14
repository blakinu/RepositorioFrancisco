from random import randint

def generate_random_array(size):
    # Variable declaration example
    array = []
    # For example
    for i in range(size):
        n = randint(0,1000)
        array.append(n)
    return array

def check_if_array_is_sorted(array):
    flag = 0
    i = 1
    while (i < len(array)) and flag==0:
        if(array[i] < array[i - 1]):
            flag = 1
        i += 1

    if flag==0:
        return True
    else:
        return False


def quicksort(array):
    # Escribid aqui vuestro código
    return array

