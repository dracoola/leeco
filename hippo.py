my_dict = {}

def make_sub_alt(fqdn):
    sub = []
    mystr = ""

    all_subs = fqdn.split('.')
    all_subs_leng = len(all_subs)

    mystr = ""
    for ind1 in range(all_subs_leng ):
        mystr = '.'.join(all_subs[ind1:all_subs_leng])

        if mystr in my_dict:
            my_dict[mystr] += 1
        else:
            my_dict[mystr] = 1

def make_sub(fqdn):
    all_subs = fqdn.split('.')
    all_subs_leng = len(all_subs)

    # https://stackoverflow.com/questions/19573221/python-lists-join-list-by-index
    for ind1 in range(all_subs_leng):
        mystr = ""
        mystr = all_subs[ind1]
        for j in range(ind1+1, all_subs_leng):
            #mystr = mystr + '.' + str(all_subs[j])     # This ALSO works
            mystr = mystr + '.' + all_subs[j]           # This ALSO WORKS

        if mystr in my_dict:
            my_dict[mystr] += 1
        else:
            my_dict[mystr] = 1

def split_domain_name(arr):
    print(my_dict)
    for e in arr:
        make_sub(e)
        #make_sub_alt(e)

    print(my_dict)

my_arr = [ 'images.google.com', 'news.google.com', 'www.yahoo.com', 'en.abc.def.yahoo.com']

split_domain_name(my_arr)

"""  OUTPUT:
{}
{'images.google.com': 1, 'google.com': 2, 'com': 4, 'news.google.com': 1, 'www.yahoo.com': 1, 'yahoo.com': 2, 'en.abc.def.yahoo.com': 1, 'abc.def.yahoo.com': 1, 'def.yahoo.com': 1}

Process finished with exit code 0
"""
