def picknic(*food):
    res = ''
    if len(food) == 1: res += f'You are bringing {food[0]}.'
    elif len(food) == 2:
        res = f'You are bringing {food[0]} and {food[1]}.'
    else:
        firsts = food[0:len(food)-1]
        s =''
        for item in firsts:
            s += item + ', '
        s += f'and {food[-1]}'
        res = f'You are bringing {s}.'
    
    return res