"""
loop: while [1,2,3] ouput => [1,'@',2,'@',3,'@']
"""

def fn_hack_9():
    result = [1,2,3]
    result_list = []
    
    i = 0
    while i < len(result):
      result_list.append(result[i])
      result_list.append('@')
      i += 1
            
    return result_list