# Author: Justin Huang
# GitHub username: huangjus
# Date: 2/21/23
# Description: This function takes a list of numbers as input
#              and modifies the original list by replacing each value with its square.

def square_list(nums):

    """
    Modifies the input list by squaring each value.

    nums: A list of numbers.
    """
    
    for i in range(len(nums)):
        nums[i] = nums[i] ** 2