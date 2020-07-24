'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word, count=0):
    if(len(word) < 2): 
        print('weve reached the end of the word!')
        return count
    if word[:2] == 'th': 
        count = count + 1
        print('found 1!: ', count)        
    return count_th(word[1:], count)

count_th('thhthth')