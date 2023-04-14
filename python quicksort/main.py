import libraries

ARRAY_SIZE = 10



def main():
    array = libraries.generate_random_array(ARRAY_SIZE)
    print(array)
    array = libraries.quicksort(array)
    print(array)

    if libraries.check_if_array_is_sorted(array):
        return True
    else:
        return False