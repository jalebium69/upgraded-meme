def find_min_x(nums, rems):
   # Initialize result
    x = 1 

    while True:
        # Check if remainder of x % nums[j] is rem[j] for all j from 0 to k-1
        for j in range(len(nums)):
            if x % nums[j] != rems[j]:
                break

        # If all remainders matched, we found x
        if j == len(nums) - 1:
            return x

        # Else, try the next number
        x += 1

    return x

# Example Usage
nums = [3,5,7]
rems = [2,3,2]
print("Numbers: ", ', '.join([str(i) for i in nums]))
print("Reminders: ", ', '.join([str(i) for i in rems]))
print("Chinese reminde: ",find_min_x(nums, rems))
