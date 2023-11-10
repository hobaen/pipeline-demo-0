"""
This code calculates and displays descriptive statistics for a 
list of numbers that is passed in to the program
"""
import numpy as np

def calculate_mean(numbers):
    """
    Calculate and return the mean of a list of numbers
    """
    total = 0

    for num in numbers:
        total += num
    
    
    return total / len(numbers)



def calculate_median(numbers):
    medIndex = (len(numbers) // 2)
  
    return numbers[medIndex]

def calculate_mode(numbers):
    frequency_table = {}
    for num in numbers:
        if num in frequency_table:
            frequency_table[num] += 1
        else:
            frequency_table[num] = 1

        max_frequency = max(frequency_table.values())

    if max_frequency > 1:
        return max(frequency_table.keys())
    else:
        return None
    

def calculate_standard_deviation(numbers):
    
    mean = calculate_mean(numbers)

    squared_deviations = [(x - mean)**2 for x in numbers]

    variance = calculate_mean(squared_deviations)

    standard_deviation = np.sqrt(variance)

    return standard_deviation
    

def calculate_range(numbers):

    
    return (max(numbers) - min(numbers))

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
