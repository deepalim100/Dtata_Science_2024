"""
What is Normalization?
Normalization is a process that adjusts the values in a dataset to a common scale without distorting differences in the ranges of values. The most common forms of normalization include:

Min-Max Normalization: Rescaling the data to fit within a specific range, typically [0, 1].
Z-score Normalization (Standardization): Rescaling the data so that it has a mean of 0 and a standard deviation of 1.

"""

class min_max_normalization:
    def norm(self, arr):
        if not arr:
            return []
        
        min_val , max_val = min(arr), max(arr)

        if min_val == max_val:
            return [0.5] * len(arr) 

        norm_lst = [(x - min_val)/(max_val - min_val) for x in arr]

        return norm_lst
    
class z_normalization:
    def z_norm(self, arr):
        # mean value
        mean = sum(arr) / len(data)
        std_dev = (sum([(x - mean) ** 2 for x in arr]) / len (data)) ** 0.5

        if std_dev == 0:
            return [0] * len(data)
        
        normalize_lst = [(x - mean)/std_dev for x in arr]
        return normalize_lst
    

if __name__ == '__main__':
    data = [1,2,3,4,5]
    normalize_lst = min_max_normalization().norm(data)
    print(f'Normalize list :{normalize_lst}')
    normalize_lst_z_norm = z_normalization().z_norm(data)
    print(f'z normalization : {normalize_lst_z_norm}')
    
        