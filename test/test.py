from mypackage import recursion,sorting

def test_sum_array():
    """
    make sure sum_array works correctly
    """

    assert recursion.sum_array([8, 3, 2, 7, 4]) == [2,3,4,7,8], 'incorrect'
    assert recursion.sum_array([10, 1, 12, 9, 2]) == [1,2,9,10,12], 'incorrect'
    assert recursion.sum_array([2, 6, 1, 4, 5]) == [1,2,4,5,6], 'incorrect'
#Test fibonnacci
def test_fibonacci():
    """
    Make sure fibonacci works properly

    """

        assert recursion.fibonacci(8) == 21, 'incorrect'
        assert recursion.fibonnacci(0) == 1, 'incorrect'
        assert recursion.fibonacci(4) == 3, 'incorrect'
def test_factorial():
    """
    Test factorial works properly
    """
    assert recursion.factorial(3) == 6, 'incorrect'
    assert recursion.factorial(2) == 2, 'incorrect'
    assert recursion.factorial(5) == 120, 'incorrect'

def test_reverse():
    assert recursion.reverse('Thabz') == 'zbahT', 'incorrect'
    assert recursion.reverse('Amen') == 'nemA', 'incorrect'
    assert recursion.reverse('Data') == 'ataD
    ', 'incorrect'

def test_bubble_sort():
            assert sorting.bubble_sort([8, 3, 2, 7, 4]) == [2,3,4,7,8], 'incorrect'
            assert sorting.bubble_sort([10, 1, 12, 9, 2]) == [1,2,9,10,12], 'incorrect'
            assert sorting.bubble_sort([2, 6, 1, 4, 5]) == [1,2,4,5,6], 'incorrect'

def test_merge_sort():
        assert sorting.merge_sort([8, 3, 2, 7, 4]) == [2,3,4,7,8], 'incorrect'
        assert sorting.merge_sort([10, 1, 12, 9, 2]) == [1,2,9,10,12], 'incorrect'
        assert sorting.merge_sort([2, 6, 1, 4, 5]) == [1,2,4,5,6], 'incorrect'
def test_quick_sort():
    assert sorting.quick_sort([8, 3, 2, 7, 4]) == [2,3,4,7,8], 'incorrect'
    assert sorting.quick_sort([10, 1, 12, 9, 2]) == [1,2,9,10,12], 'incorrect'
    assert sorting.quick_sort([2, 6, 1, 4, 5]) == [1,2,4,5,6], 'incorrect'
    
