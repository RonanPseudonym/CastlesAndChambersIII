def leven(a, b):
    a_l = len(a)
    b_l = len(b)
    
    if len(b) > len(a): a, b = b, a
    
    distances = range(len(a)+1)
    
    for i in range(len(b)):
        distances_ = [i+1]
        for j in range(len(a)):
            if a[j] == b[i]: distances_.append(distances[i])
            else: 
                cost_steps = (distances[i], distances[i + 1], distances_[-1])
                distances_.append(1 + min(cost_steps))
        distances = distances_
        
    return distances[-1]
    
print(leven("catophone", "cat"))