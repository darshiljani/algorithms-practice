from algo import linear_search

def test():
    foo: list[int] = [1, 3, 4, 69, 71, 81, 90, 99, 420, 1337, 69420];
    assert(linear_search(foo, 69)) == True
    assert(linear_search(foo, 1336)) == False
    assert(linear_search(foo, 69420)) == True
    assert(linear_search(foo, 69421)) == False
    assert(linear_search(foo, 1)) == True
    assert(linear_search(foo, 0)) == False
    
if __name__ == '__main__':
    try:
        test()
        print('\033[1;32;40mAll cases passed! \033[0m')
    except AssertionError as e:
        print(f'\033[1;34;40m{e} \033[0m')