def evaluate_position(position):
    return -1 * ((position - 7) ** 2) + 49

def locate_maximum_point(arrSize: int) -> int:
    position = arrSize // 2
    
    while True:
        curr = evaluate_position(position)
        
        if position > 0:
            valueL = evaluate_position(position - 1)
        else:
            valueL = float('-inf')
            
        if position < arrSize:
            valueR = evaluate_position(position + 1)
        else:
            valueR = float('-inf')
        
        if curr >= valueL and curr >= valueR:
            return position
        
        if valueR > curr:
            position += 1
        else:
            position -= 1

size = 11
result = locate_maximum_point(size)
print(result)
