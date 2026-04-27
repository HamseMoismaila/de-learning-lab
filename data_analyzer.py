# # Thursday Apr 17 — Functions, Loops & Control Flow


# def count(numbers):
#     return len(numbers)

# def total_all(numbers):
#     total_sum = 0
#     i  = 0
#     while i < len(numbers):
#         total_sum += numbers[i]
#         i += 1
#     return total_sum


# def mean(numbers):
#     if not numbers:
#         raise ValueError("Empty list")
    
#     return total_all(numbers) / count(numbers)

# def minimum(numbers):
#     if not numbers:
#         raise ValueError("Empty list")
    
#     min_value = numbers[0]
#     for num in numbers:
#         if num < min_value:
#             min_value = num
#     return min_value

# def maximum(numbers):
#     if not numbers:
#         raise ValueError("Empty list")
    
#     max_value = numbers[0]
#     for num in numbers:
#         if num > max_value:
#             max_value = num
#     return max_value

# def squared(  numbers):
#     squared = [x**2 for x in numbers]
#     return squared

# def median(numbers):
#     if not numbers:
#         raise ValueError("Empty list")
    
#     sorted_nums = sorted(numbers)
#     n = count(sorted_nums)
#     mid = n // 2 

#     if n % 2 == 0:
#         return (sorted_nums[mid - 1] + sorted_nums[mid] ) / 2
#     else:
#         return sorted_nums[mid]
    
# def clean_numbers(numbers):
#     cleaned = []
#     for num in numbers:
#         try:
#             cleaned.append(float(num))
#         except:
#             continue
#     return cleaned
    
# def main():
#     numbers =  [10 , 5, 8, 12, 3, 7, 9, 15, 6, 2]

#     if not numbers:
#       raise ValueError("List is emty. Cannot perform analysis")




#     print("Count:", count(numbers))
#     print("Total:", total_all(numbers))
#     print("Mean:", mean(numbers))
#     print("Min:", minimum(numbers))
#     print("Max:", maximum(numbers))
#     print("Median:", median(numbers))
#     print("Double numbers: ", squared(numbers))
#     print("Cleaned data: ", clean_numbers(numbers))

# if __name__ == "__main__":
#     try: 
#         main()
#     except Exception as e:
#         print("Error: ", e)


# Upgrade thinking (important for data engineering)

# Your flow should be:

# raw data → validate/clean → process → output



def clean_data(data):
    cleaned = []
    for x in data:
        try:
            cleaned.append(float(x))
        except:
            continue
    return cleaned

def process_data(data):
    total = sum(data)
    mean = total / len(data)
    return total, mean

def output_result(total, mean):
    print("total: ", total)
    print("Mean: ", mean)


def main():
    raw_data = ["10", "5.5", "abc", "", None, "20"]

    cleaned = clean_data(raw_data)
    total, mean = process_data(cleaned)
    output_result(total, mean)



if __name__ == " __main__":
    main()



## Raw materials → cleaning → manufacturing → packaging