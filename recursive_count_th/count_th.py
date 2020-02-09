'''
Your function should take in a signle parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''

#thhelloth
def count_th(word):
    # word.lower()
    if 'th' in word:
        count = 1
        index_location = word.find('th') + 2
        remaining = word[index_location:]
        return count + count_th(remaining)
    else:
        count = 0
    return count
    
print(count_th("thhellothyath"))