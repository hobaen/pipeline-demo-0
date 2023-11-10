"""
This code calculates and displays descriptive statistics for a 
list of numbers that is passed in to the program
"""

from statistics import mean, median

def calculate_mean(numbers):
    """
    Calculate and return the mean of a list of numbers
    """
    return mean(numbers)

def calculate_median(numbers):

    return median(numbers)

def calculate_mode(numbes):
    return None

def calculate_standard_deviation(nubers):
    return None


def calculate_range(numbers):
    return None
def calculate_statistics(umbers):
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
