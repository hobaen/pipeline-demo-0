"""
This code calculates and displays descriptive statistics for a 
list of numbers that is passed in to the program
"""


def calculate_mean(numbers):
    """
    Calculate and return the mean of a list of numbers
    """
    return None



def caLculate_median(numbers):
    # Sort the list of numbers
    sorted_numbers = sorted(numbers)

    # Find the middle index
    middle_index = len(sorted_numbers) // 2

    # Check if the list has an even or odd number of elements
    if len(sorted_numbers) % 2 == 0:
        # If even, take the average of the two middle elements
        median = (sorted_numbers[middle_index - 1] + sorted_numbers[middle_index]) / 2
    else:
        # If odd, take the middle element
        median = sorted_numbers[middle_index]

    return median

def calculate_mode(numbers):
   frequency_table = {}
    for num in numbers:
        if num in frequency_table:
            frequency_table[num] += 1
        else:
            frequency_table[num] = 1
    if not numbers:
        return None

def calculate_standard_deviation(numbers):
     # Calculate the mean
    mean = sum(numbers) / len(numbers)

    # Calculate the squared differences from the mean
    squared_diff = [(x - mean) ** 2 for x in numbers]

    # Calculate the variance
    variance = sum(squared_diff) / len(numbers)

    # Calculate the standard deviation
    std_deviation = math.sqrt(variance)

    return std_deviation
    


def calculate_range(numbers):
    return None
def calculate_statistics(numbers):
    descriptiveStats = {'mean': calculate_mean(numbers), 'median':calculate_median(numbers),'mode':calculate_mode(numbers),'standard_deviation': calculate_standard_deviation(numbers),'range':calculate_range(numbers)
    }
    return descriptiveStats
if __name__ == "__main__":
    data = []
    print("Enter numbers (type 'done' to finish): ")
    while True:
        try:
            line = input()
            if line.strip().lower() == 'done':
                break
            data.append(float(line))
        except ValueError:
            print("Please enter a valid number or type 'done' to finish.")

    stats = calculate_statistics(data)
    for stat, value in stats.items():
        print(f"{stat.capitalize()}: {value}")
