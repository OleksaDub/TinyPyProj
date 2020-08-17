def jump(text):
    res = ''   
    substitute = {'1':'9', '2':'8', '3':'7',
                '4':'6', '5':'0', '6':'4',
                '7':'3', '8':'2', '9':'1', '0':'5'}

    for char in text:
        if char not in '1234567890':
            res += char
        else:
            res += substitute[char]

    return res

print(jump('text0123'))