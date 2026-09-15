#IN THE NAME OF GAD


#filter Puncs Fruitful

import string  

def filter_puncs_fruitful(text: str) -> str:
    """
    Example
    --------
    >>> filter_puncs_fruitful(text='ha@)!med37tabriz')
    'hamedtabriz'
    """
    result = ""
    for ch in text:
        if ch in string.punctuation  or ch.isdigit():
            continue
        result += ch
    return result


###Driver Code###
x = filter_puncs_fruitful(text = 'ha@)!med37tabriz')   
print(x)


print('*'*90)

#Clean Text

def clean_text(text: str) -> str:
    """
     1. filter puncs
     2. uppercase and lowercase are same
    """
    resultx = ''
    for sh in text :
        if sh in string.punctuation:
            continue
        resultx += sh.swapcase()
    return resultx    

### Driver Code###
n = clean_text(text = 'aMIRABAS khAJEH' )
print(n)
