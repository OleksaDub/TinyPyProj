def crowsnest(word):
    article = 'a'
    if word[0] in 'aeiou':
        article = 'an'
    
    return f'Ahoy, Captain, {article} {word} off the larboard bow!'
