"""
YES I FINALLY DID IT EVEN AFTER 3or4 M SESSIONS TODAY
EASY  38. Count and Say   https://leetcode.com/problems/count-and-say/

866   6704   Favorite   Share
The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

6.     312211
7.     13112221
8.     1113213211
9.     31131211131221
10.    13211311123113112211
11.    11131221133112132113212221
       3113112221232112111312211312113211  ????

Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.

Example 1:
    Input: 1
    Output: "1"

Example 2:
    Input: 4
    Output: "1211"

"""

'''
class Solution:
    def countAndSay(self, n: int) -> str:
        

'''


# Python3 program to Split string into characters # Code #2 : Typecasting to list  # https://www.geeksforgeeks.org/python-split-string-into-list-of-characters/
def split(word):
    return list(word)

# Driver code
#word = 'geeks'
#print(split(word))

#def runLengthEncode(some_array):
def runLengthEncode(some_string):
    #some_array = some_string.split('') #   File "/Users/pochen/PycharmProjects/leetc_easy_strings/venv/count_and_say.py", line 49, in runLengthEncode

    #some_array = some_string.split("(?!^)")  # This is JAVA https://stackoverflow.com/questions/5235401/split-string-into-array-of-character-strings
    # some_array = some_string.toCharArray() # this is JAVA

    some_array = split(some_string)
    print(some_array)

    consider_current_int = None
    count_current_int = 0
    run_length_enc_pair = []
    run_length_enc = []

    if not some_array:
        return [] #something

    some_array_length = len(some_array)
    print('some_array_length', some_array_length)

    for i in range(some_array_length):
        print('>>>> vvvvv ======i',i)
        print('     WTF WTF WTF run_length_enc_pair', run_length_enc_pair)
        print('     WTF WTF WTF run_length_enc', run_length_enc)
        if consider_current_int != some_array[i]:
            print('consider_current_int', consider_current_int, 'some_array[i]' , some_array[i])
            #count_current_int = 0

            print(run_length_enc_pair)
            print('BEFORE run_length_enc', run_length_enc)
            run_length_enc.extend(run_length_enc_pair)
            print('AFTER run_length_enc', run_length_enc)

            print('here & consider_current_int BEFORE', consider_current_int, 'count_current_int', count_current_int)
            consider_current_int = some_array[i]
            count_current_int = 1
            #count_current_int += 1
            print('AFTER SET consider_current_int', consider_current_int, 'count_current_int', count_current_int)
#            if consider_current_int == None:
#                print('here NONE')
#                pass
#            else:
            print('here here here')
            run_length_enc_pair = [count_current_int, consider_current_int]
            consider_current_int = some_array[i]
            #count_current_int += 1
        #    print(run_length_enc_pair)
        #    print('BEFORE run_length_enc', run_length_enc)
        #    run_length_enc.extend(run_length_enc_pair)
        #    print('AFTER run_length_enc', run_length_enc)
        else: # consider_current_int == some_array[i]
            print('FUCK')
            count_current_int += 1
            print('WTF', count_current_int)
            run_length_enc_pair = [count_current_int, consider_current_int]
            print('WTF, ', run_length_enc_pair)
            #if i+1 >= some_array_length or consider_current_int != some_array[i+1]:
            #    run_length_enc.extend(run_length_enc_pair)
            #else:
            #    pass


    print('END OF FUNC run_length_enc_pair: ', run_length_enc_pair)
    print('END OF FUNC run_length_enc: ', run_length_enc)
    run_length_enc.extend(run_length_enc_pair)
    print('FINAL EXTENDED run_leng_enc:', run_length_enc)
    #print(''.join(run_length_enc))

    mystring = ""

    for digit in run_length_enc:
        mystring += str(digit)

    print(mystring)
    return mystring



def myCountAndSayDoesNotQuiteWork(my_int):
    my_array = []
    new_array = []
    run_length_encoding = []
    #for indx in range(1, my_int):
    if my_int == 1:
        new_array = "1"
        my_array = "1"
        return "1"

    for indx in range(my_int):
        print('>>>>>vvvvv ITERATION_INX:', indx, 'N-TH TERM:', indx+1, 'vvvvv<<<<<')
        new_array = [] # maybe need to re-set it to empty array

        if not my_array:

            #my_array.append(indx)
            #my_array.append("1") # let's apprend the integer 1 instead
            my_array.append(1)
            print(my_array)
        else:
            new_array = [] # maybe need to re-set it to empty array ; promising that [1, 2, 1, 2, 2, 1] close to 111221
            count_the_run = 0
            leng_my_array = len(my_array)
            print('LENG',leng_my_array)
            j = 0
            consider_digit = my_array[j]
            while (j <= leng_my_array - 1):

                print('CONSIDER DIGIT:', consider_digit)
                if (my_array[j] == consider_digit):
                    count_the_run += 1
                    print('COUNT_THE_RUN', count_the_run)
                else:

                    run_length_encoding = [count_the_run, consider_digit]
                    print('>>>>>>>>>>>>>>>>>>  RLE:', run_length_encoding)
                    count_the_run = 0
                    consider_digit = my_array[j]
                    count_the_run = 1
                    print('COUNT_THE_RUN', count_the_run)
                j += 1
                print('BEFORE NEW_ARRAY EXTEND:', new_array)
                new_array.extend(run_length_encoding)
                print('AFTER NEW_ARRAY EXTEND:', new_array)


            """
            for j in range(leng_my_array):  # maybe use a simulated do-while kind of loop
                
                print('CONSIDER DIGIT:',consider_digit)
                count_the_run += 1
                print('COUNT_THE_RUN', count_the_run)
            """

            new_array.append(count_the_run)
            #new_array.extend(my_array)
            new_array.append(consider_digit)
            print('NEW ARRAY', new_array)
            print('MY ARRAY BEFORE', my_array)
            my_array = new_array
            print('MY ARRAY AFTER', my_array)
            new_array = []


        print(my_array)


def Alt_CountAndSay(my_int):
    my_array = []
    new_array = []
    run_length_encoding = []
    # for indx in range(1, my_int):
    if my_int == 1:
        new_array = "1"
        my_array = "1"
        return [1]

    for indx in range(my_int):
        print('>>>>>vvvvv ITERATION_INX:', indx, 'N-TH TERM:', indx + 1, 'vvvvv<<<<<')
        new_array = []  # maybe need to re-set it to empty array

        if not my_array:

            # my_array.append(indx)
            # my_array.append("1") # let's apprend the integer 1 instead
            my_array.append(1)
            print(my_array)
        else:
            new_array = []  # maybe need to re-set it to empty array ; promising that [1, 2, 1, 2, 2, 1] close to 111221
            count_the_run = 0
            leng_my_array = len(my_array)
            print('LENG', leng_my_array)
            j = 0
            consider_digit = my_array[j]
            while (j <= leng_my_array - 1):

                print('CONSIDER DIGIT:', consider_digit)
                if (my_array[j] == consider_digit):
                    count_the_run += 1
                    print('COUNT_THE_RUN', count_the_run)
                else:

                    run_length_encoding = [count_the_run, consider_digit]
                    print('>>>>>>>>>>>>>>>>>>  RLE:', run_length_encoding)
                    count_the_run = 0
                    consider_digit = my_array[j]
                    count_the_run = 1
                    print('COUNT_THE_RUN', count_the_run)
                j += 1
                print('BEFORE NEW_ARRAY EXTEND:', new_array)
                new_array.extend(run_length_encoding)
                print('AFTER NEW_ARRAY EXTEND:', new_array)

            """
            for j in range(leng_my_array):  # maybe use a simulated do-while kind of loop

                print('CONSIDER DIGIT:',consider_digit)
                count_the_run += 1
                print('COUNT_THE_RUN', count_the_run)
            """

            new_array.append(count_the_run)
            # new_array.extend(my_array)
            new_array.append(consider_digit)
            print('NEW ARRAY', new_array)
            print('MY ARRAY BEFORE', my_array)
            my_array = new_array
            print('MY ARRAY AFTER', my_array)
            new_array = []

        print(my_array)


def myCountAndSay(my_int):
    result = "1"
    re_feed_in = ""

    if my_int == 1:
        return "1"

    for i in range(1, my_int):
        re_feed_in = result
        result = runLengthEncode(re_feed_in)

#my_nth_term = 1
#print(myCountAndSay(my_nth_term))

#my_nth_term = 4
#print(myCountAndSay(my_nth_term))

#my_nth_term = 5
#print(myCountAndSay(my_nth_term))

#my_nth_term = 6
#print(myCountAndSay(my_nth_term))

#sample_arr = [1, 1]
#print('FINAL RESULT: ',runLengthEncode(sample_arr))

#sample_arr = [1,1,1,2,2,1]
#print('FINAL RESULT: ',runLengthEncode(sample_arr))

#sample_arr = [1,2,1,1]
#print('FINAL RESULT: ',runLengthEncode(sample_arr))


#sample_arr = [1,1,1,2,2,1]
#print('FINAL RESULT: ',runLengthEncode(sample_arr))

#sample_arr = [1]
#print('FINAL RESULT: ',runLengthEncode(sample_arr))

#sample_arr = [3,1,2,2,1,1]
#print('FINAL RESULT: ', runLengthEncode(sample_arr))  # output SHOULD BE 13112221

#my_input_number = 1
#print(myCountAndSay(my_input_number))

#my_input_number = 2
#print(myCountAndSay(my_input_number))

my_input_number = 5
print(myCountAndSay(my_input_number))
