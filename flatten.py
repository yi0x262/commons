from copy import deepcopy
def is_scalar(data):
    try:
        float(data)
    except TypeError:
        return False
    return True

def flatten(data,maxcount=10):
    """
    data : list or ndarray (or scalar)
            data[0]...[0] must be convertible to float
    """
    d = deepcopy(data)
    #check data is scalar or flatten
    if is_scalar(d):
        return d
    #flatten
    for _ in range(maxcount):
        if is_scalar(d[0]):
            return d
        d = d[0]
    else:
        raise RuntimeError('in flatten() : over maxcount')

if __name__ == '__main__':
    import numpy as np
    def printflatten(data):
        print('data',data)
        print('flatten',flatten(data))
    a = [1,2,3]
    a = [[1,2,3],[4,5,6]]
    printflatten(a)
    A = np.array(a)
    printflatten(A)
    b = [np.array(a)]
    printflatten(b)
