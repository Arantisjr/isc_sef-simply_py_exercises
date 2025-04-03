# A function to get even numbers from a list

def even_numbers(lst):
    
    is_even = list(filter(lambda x: x % 2 == 0, lst))
    print(f'even numbers:\n {is_even}')
    
    count = len(is_even)
    print(f'number of even numbers:\n {count}')
    
   


nums = [1,2,3,4,6,8,9]

even_numbers(nums)