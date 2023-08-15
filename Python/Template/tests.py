from algo import algorithm

def test():
    test_data: any
    assert(algorithm(test_data)) == True
    
if __name__ == '__main__':
    try:
        test()
        print('\033[1;32;40mAll cases passed! \033[0m')
    except AssertionError as e:
        print(f'\033[1;34;40m{e} \033[0m')