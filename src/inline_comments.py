# ------------------------------------------------------------------------------
# Example 1
# Bubble Sort Example
# ------------------------------------------------------------------------------

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


# ------------------------------------------------------------------------------
# Example 2
# Weather Data Processing Example
# ------------------------------------------------------------------------------

import pandas as pd
import numpy as np

if __name__ == "__main__":
    # Load weather data from a CSV file into a DataFrame
    weather_df = pd.read_csv('april2024_station_data.csv')

    # Convert columns to NumPy arrays for speed
    wind_speed = weather_df['wind_speed'].to_numpy()
    wind_direction = weather_df['wind_direction'].to_numpy()

    # Convert wind direction from degrees to radians for trigonometric calculations
wind_direction_rad = np.deg2rad(wind_direction)