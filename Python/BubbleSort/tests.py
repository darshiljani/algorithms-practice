from algo import bubble_sort

def test():
    test_arr = [9, 3, 7, 4, 69, 420, 42] 
    assert(bubble_sort(test_arr)) == [3, 4, 7, 9, 42, 69, 420]
 
if __name__ == '__main__':
    try:
        test()
        print('\033[1;32;40mAll cases passed! \033[0m')
    except AssertionError as e:
        print(f'\033[1;34;40m{e} \033[0m')
