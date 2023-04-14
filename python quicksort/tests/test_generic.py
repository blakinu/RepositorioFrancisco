from main import main,ARRAY_SIZE
import libraries

def test_array_size():
    assert int(ARRAY_SIZE)!=None
    assert ARRAY_SIZE>=10
    assert ARRAY_SIZE==len(libraries.generate_random_array(ARRAY_SIZE))

def test_entire_flow():
    assert main()

def test_no_sort_method():
    file1 = open('libraries.py', 'r')
    Lines = file1.readlines()
    sort_method_detected=False
    # Strips the newline character
    i=0
    while (i<len(Lines)) and (sort_method_detected==False):
        if ".sort" in Lines[i]:
            sort_method_detected=True
            print(f"Found .sort in line {i+1}:")
            print(Lines[i])
        i=i+1

    assert not sort_method_detected

