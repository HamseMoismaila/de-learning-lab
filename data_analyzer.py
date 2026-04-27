# Thursday Apr 17 — Functions, Loops & Control Flow


def count(numbers):
    return len(numbers)

def total_all(numbers):
    total_sum = 0
    i  = 0
    while i < len(numbers):
        total_sum += numbers[i]
        i += 1
    return total_sum


def mean(numbers):
    return total_all(numbers) / count(numbers)

def minimum(numbers):
    min_value = numbers[0]
    for num in numbers:
        if num < min_value:
            min_value = num
    return min_value

def maximum(numbers):
    max_value = numbers[0]
    for num in numbers:
        if num > max_value:
            num = max_value
    return max_value

def double(  numbers):
    squared = [x**2 for x in numbers]
    return squared

def median(numbers):
    sorted_nums = sorted(numbers)
    n = count(sorted_nums)
    mid = n // 2 

    if n % 2 == 0:
        return (sorted_nums[mid - 1] + sorted_nums[mid] ) / 2
    else:
        return sorted_nums[mid]
    
def clean_numbers(numbers):
    cleaned = []
    for num in numbers:
        try:
            cleaned.append(float(num))
        except:
            continue
        return cleaned
    

numbers =  [10 , 5, 8, 12, 3, 7, 9, 15, 6, 2]

if not numbers:
    raise ValueError("List is emty. Cannot perform analysis")

try:

    print("Count:", count(numbers))
    print("Total:", total_all(numbers))
    print("Mean:", mean(numbers))
    print("Min:", minimum(numbers))
    print("Max:", maximum(numbers))
    print("Median:", median(numbers))
    print("Double numbers: ", double(numbers))


except Exception as e:
    print("Error: ", e)




# def mean(numbers):
#   print(sum(numbers) / len(numbers))   #  I do not why this is bad usage
# def minimum([numbers])    this will through some synthaxError



