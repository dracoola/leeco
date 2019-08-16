my_dict = {}

def make_sub_alt(fqdn):
    sub = []
    mystr = ""

    all_subs = fqdn.split('.')
    all_subs_leng = len(all_subs)

    mystr = ""
    for ind1 in range(all_subs_leng ):
        mystr = '.'.join(all_subs[ind1:all_subs_leng])

####        print('MYSTR:',mystr)
        if mystr in my_dict:
            my_dict[mystr] += 1
        else:
            my_dict[mystr] = 1

def make_sub(fqdn):
    sub = []
    #mystr = []
    mystr = ""

    all_subs = fqdn.split('.')

    all_subs_leng = len(all_subs)

####    print(all_subs)
####    print(all_subs_leng)

    # https://stackoverflow.com/questions/19573221/python-lists-join-list-by-index
    for ind1 in range(all_subs_leng):
        mystr = ""
        mystr = all_subs[ind1]
###        print('SUB: ', sub)
        for j in range(ind1+1, all_subs_leng):
            #mystr = mystr + '.' + str(all_subs[j])     # This ALSO works
            mystr = mystr + '.' + all_subs[j]           # This ALSO WORKS
        #    sub.append(all_subs[j])
###            print('SUB SUB:', sub)
####            print('IND1', ind1, 'J:', j,'LENG-1:',all_subs_leng - 1,'LENG:', all_subs_leng)
          #  mystr = '.'.join(all_subs[j:all_subs_leng]) # GREAT! This Works https://www.geeksforgeeks.org/python-merge-list-elements/  # # Python3 merging list elements using join() + list slicing

####            print('MYSTR:',mystr)
####        print('MYSTRMYSTRMYSTR:',mystr)

        if mystr in my_dict:
            my_dict[mystr] += 1
        else:
            my_dict[mystr] = 1

            # print(all_subs[ind1])
        # sub += all_subs[ind1]  #  ['i', 'm', 'a', 'g', 'e', 's', 'g', 'o', 'o', 'g', 'l', 'e', 'c', 'o', 'm']
            # print('.'.join(all_subs))
###            print('^^^^^')
###            print('.'.join(sub))
###            print('vvvvv')
            #print(sub)

#    for ind1 in range(all_subs_leng):
#        sub=str.join(all_subs[ind1])
#        #str.join()

###    print('--->', sub)

def split_domain_name(arr):
    print(my_dict)
    for e in arr:
#        if e in my_dict:
#            my_dict[e] = my_dict[e] + 1
#        else:
#            my_dict[e] = 1
        make_sub(e)
        #make_sub_alt(e)

    print(my_dict)

my_arr = [ 'images.google.com', 'news.google.com', 'www.yahoo.com', 'en.abc.def.yahoo.com']

#              0     1       2                                       0   1   2   3     4
#            ind1                                                   ind1
#                    j                                                   j

split_domain_name(my_arr)

"""  OUTPUT:
{}
{'images.google.com': 1, 'google.com': 2, 'com': 4, 'news.google.com': 1, 'www.yahoo.com': 1, 'yahoo.com': 2, 'en.abc.def.yahoo.com': 1, 'abc.def.yahoo.com': 1, 'def.yahoo.com': 1}

Process finished with exit code 0
"""
