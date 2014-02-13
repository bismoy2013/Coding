import numpy as np
def get_sum(array):
    k=0
    cumsum_array = [0] + np.cumsum(array).tolist()
    key_dict = {}
    for index, cum_sum in enumerate(cumsum_array):
        if cum_sum not in key_dict:
            key_dict[cum_sum] = [index]
            continue
			
        for i,v in enumerate(key_dict[cum_sum]):
            k=k+1
        key_dict[cum_sum].append(index)
    print k

if __name__ == '__main__':
    #array = [2, -2, 6,-6,0]
    array=[]
    test_case=int(input())
    for i in xrange(test_case):
        number=int(input())
        array.append(number)
    get_sum(array)
