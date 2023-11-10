"""
This code calculates and displays descriptive statistics for a 
list of numbers that is passed in to the program
"""


def calculate_mean(numbers):
    """
    Calculate and return the mean of a list of numbers
    """
    total_sum = sum(numbers)
    mean = total_sum/len(numbers)

    return mean


def caLCulate_median(numbers):
    
    sorted_list = sorted(numbers) "Sort list and divide it by 2 to find the mean."

    middle_index = len(sorted_list) // 2

    if len(sorted_list) % 2 == 1:
        median = numbers[middle_index]
    else:
        median = (sorted_list [middle_index] + sorted_list[middle_index]) / 2

    return median

def calculate_mode(numbers):

    number_counts = Counter(numbers)

    max_frequency = max(number_counts.values())

    mode = [number for number, frequency in number_counts.items() if frequency == max_frequency]

    return mode

def calculate_standard_deviation(numbers):
    
    mean = sum(numbers) / len(numbers)
    
    sum_squared_diff = sum((x - mean) ** 2 for x in numbers)
    
    variance = sum_squared_diff / len(numbers)
    
    standard_deviation = math.sqrt(variance)
    
    return standard_deviation

def calculate_range(numbers):

    datarange = max(numbers) - min(numbers)

    return datarange
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
