import numpy as np

def calculate(list):
  if len(list) != 9: 
    raise ValueError("List must contain nine numbers.")
  else:
    new_arr = np.array(list).reshape(3, 3)
    calculations = dict.fromkeys(['mean', 'variance', 'standard deviation', 'max', 'min', 'sum'])
    calculations['mean'] = [new_arr.mean(0).tolist(), new_arr.mean(1).tolist(), new_arr.mean().tolist()]
    calculations['variance'] = [new_arr.var(0).tolist(), new_arr.var(1).tolist(), new_arr.var().tolist()]
    calculations['standard deviation'] = [new_arr.std(0).tolist(), new_arr.std(1).tolist(), new_arr.std().tolist()]
    calculations['max'] = [new_arr.max(0).tolist(), new_arr.max(1).tolist(), new_arr.max().tolist()]
    calculations['min'] = [new_arr.min(0).tolist(), new_arr.min(1).tolist(), new_arr.min().tolist()]
    calculations['sum'] = [new_arr.sum(0).tolist(), new_arr.sum(1).tolist(), new_arr.sum().tolist()]
    return calculations