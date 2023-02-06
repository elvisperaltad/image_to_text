import numpy as np
hash = {{"name":"carlos", "age":25} ,{"name":"miguel", "age": 25}}
print(hash)
def function_result(hash):
    new_list = list(hash.items())
    result = np.array(new_list)
    return result

rs = function_result(hash)
print(rs)