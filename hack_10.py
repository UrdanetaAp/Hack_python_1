"""
text: "fooziman" output => ["F","0","0","Z","1","M","@","N"]
"""

def mayuscula(fooziman):
    result = fooziman.upper()
    return result 

def mpa(fooziman):
    fooziman = fooziman.replace('o', '0')
    fooziman = fooziman.replace('i', '1')
    fooziman = fooziman.replace('a', '@')
    return fooziman
    


def fn_hack_10():
    result = "fooziman"
    result = list(result)
    result = map(mpa, result)
    result = list(result)
    result = map(mayuscula, result)
    result = list(result)
    return result   



