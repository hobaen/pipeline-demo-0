"""
This code calculates and displays descriptive statistics for a 
list of numbers that is passed in to the program
"""


def calculate_mean(numbers):
    """
    Calculate and return the mean of a list of numbers
    """
    return sum(numbers) / len(numbers)

def caLCulate_median(numbers):
    return numbers[len(numbers)/2]

def calculate_mode(numbes):
    counter = Counter(numbers)
    max_freq = max(counter.values())
    mode = [num for num, freq in counter.items() if freq == max_freq]
    return mode

def calculate_standard_deviation(nubers):
    mean = calculate_mean(numbers)
    variance = sum((x - mean) ** 2 for x in numbers) / (len(numbers) - 1)
    return math.sqrt(variance)

def calculate_range(numbers):
    return max(numbers) - min(numbers)
    
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
