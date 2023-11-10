"""
This code calculates and displays descriptive statistics for a
list of numbers that is passed in to the program
"""
import statistics

def calculate_mean(numbers):
    """
    Calculate and return the mean of a list of numbers
    """
    total = 0

    for num in numbers:
        total += num
    return total / len(numbers)

def calculate_median(numbers):
    """
    Calculate and return the median of a list of numbers
    """
    numbers.sort()
    if not numbers:
        return None
    if len(numbers) % 2 != 0:
        return numbers[len(numbers) // 2]
    return (numbers[len(numbers) // 2] + numbers[len(numbers) // 2 - 1]) / 2

def calculate_mode(numbers):
    """
    Calculate and return the mode of a list of numbers
    """
    return statistics.mode(numbers)

def calculate_standard_deviation(numbers):
    """
    Calculate and return the standard deviation of a list of numbers
    """
    return statistics.stdev(numbers)

def calculate_range(numbers):
    """
    Calculate and return the range of a list of numbers
    """
    return (max(numbers) - min(numbers))

def calculate_statistics(numbers):
    """
    Calculate and return the statistics of a list of numbers
    """
    descriptive_stats = {'mean': calculate_mean(numbers),
    'median':calculate_median(numbers),
    'mode':calculate_mode(numbers),
    'standard_deviation': calculate_standard_deviation(numbers),
    'range':calculate_range(numbers)
    }
    return descriptive_stats
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
