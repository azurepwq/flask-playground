# Example 1
def calculate_area(radius):
    """
    Calculates the area of a circle given its radius.

    Args:
        radius (float): The radius of the circle.

    Returns:
        float: The area of the circle.
    """
    pi = 3.14159
    return pi * radius * radius


# Example 2
def find_max(numbers):
    """
    Returns the maximum value in a list of numbers.

    Args:
        numbers (list): The list of numbers to search. (A Python list is similar to an array in Java/JavaScript.)

    Returns:
        The largest value found in the list.
    """
    max_number = numbers[0]
    for number in numbers:
        if number > max_number:
            max_number = number
    return max_number


# Example 3
def bubble_sort(arr):
    """
    Sorts a list in ascending order using the bubble sort algorithm.

    Args:
        arr (list): The list to sort. (Like an array in Java/JavaScript. Elements must be comparable.)

    Returns:
        list: The sorted list. (Input is modified in place and also returned.)

    Note:
        Bubble sort is not efficient for large datasets. Use Python's built-in sorted() for production code.
    """
    n = len(arr)
    for i in range(n):
        # Each pass moves the largest unsorted element to the end of the list.
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr