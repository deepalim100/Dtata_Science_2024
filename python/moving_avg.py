"""
Q.1 >> Write a Python function to calculate the moving average of a list of numbers.
"""

class moving_avg:
    def average(self, nums, window_size):
        moving_avg = []
        for i in range(len(nums)- window_size + 1):
            window = nums[i:i+window_size]
            average = sum(window)/window_size
            moving_avg.append(average)

        return moving_avg
    
if __name__ == '__main__':
    array = [1,2,3,4,5,6,7,8,9]
    win_size = 3
    result_arrray = moving_avg().average(array, win_size)
    print(f'moving average array : {result_arrray}')
