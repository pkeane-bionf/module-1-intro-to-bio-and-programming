import random

# ------------------------------------------------------------------------------------
def check_answers_l2_ex1(globals_dict):
    if not 'mylist1' in globals_dict:
        print("You've not created a variable 'mylist1'. Try again!")
        return

    if not 'mylist2' in globals_dict:
        print("You've not created a variable 'mylist2'. Try again!")
        return

    if not 'mylist3' in globals_dict:
        print("You've not created a variable 'mylist3'. Try again!")
        return

    if not 'mylist4' in globals_dict:
        print("You've not created a variable 'mylist4'. Try again!")
        return
    
    mylist1 = globals_dict['mylist1']
    mylist2 = globals_dict['mylist2']
    mylist3 = globals_dict['mylist3']
    mylist4 = globals_dict['mylist4']

    if type(mylist1) == list and len(mylist1) == 0:
        print("Well done - you've created an empty list!!")
    else:
        if type(mylist1) != list:
            print("Your mylist1 variable was of type ", type(mylist1), ". Try again!")
        if len(mylist1) != 0:
            print("Your mylist1 variable was not empty and had ", len(mylist1), " entries. Try again!")

    if mylist2 == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
        print("Well done - you've created a list with the numbers 0 -> 9 in it!")
    else:
        print("Your mylist2 variable did not equal [0, 1 ...8, 9]. It was ", mylist2, ". Try again!")

    if mylist3 == [0, 1, 2, 3, 4, 'five', 6, 7, 8, 9]:
        print("Well done - you've created a copy of mylist2 and replaced '5' with 'five'!")
    else:
        print("Your mylist3 variable did not equal mylist2 with 5 -> 'five'. It was ", mylist3, ". Try again!")

    if mylist4 == mylist2 * 2:
        print("Well done - you've created a list with two consecutive copies of mylist2!")
    else:
        print("Your mylist4 variable was not equal to two conseqcutive copies of mylist2. It was ", mylist2, ". Try again!")

# ------------------------------------------------------------------------------------
def check_answers_l2_ex2(globals_dict):
    if not 'sublist1' in globals_dict:
        print("You've not created a variable 'sublist1'. Try again!")
        return
    if not 'sublist2' in globals_dict:
        print("You've not created a variable 'sublist2'. Try again!")
        return
    if not 'sublist3' in globals_dict:
        print("You've not created a variable 'sublist3'. Try again!")
        return

    
    sublist1 = globals_dict['sublist1']
    sublist2 = globals_dict['sublist2']
    sublist3 = globals_dict['sublist3']
    mylist4 = globals_dict['mylist4']

    if sublist1 == mylist4[:5]:
        print("sublist1 is correct!")
    else:
        print("sublist1 equals ", sublist1, " which is incorrect. try again!")

    if sublist2 == mylist4[-5:]:
        print("sublist2 is correct!")
    else:
        print("sublist2 equals ", sublist2, " which is incorrect. try again!")

    if sublist3 == mylist4[2:-2]:
        print("sublist3 is correct!")
    else:
        print("sublist3 equals ", sublist3, " which is incorrect. try again!")

# ------------------------------------------------------------------------------------
def check_answers_l2_ex3(globals_dict):

    mylist4 = globals_dict['mylist4']
    sublist1 = globals_dict['sublist1']
    sublist2 = globals_dict['sublist2']
    
    if mylist4 == [0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9]:
        print("mylist4 is correct!")
    else:
        print("mylist4 equals ", myist4, " which is incorrect. try again!")

    if sublist2 == [5, 6, 7, 8, 9, 0, 1, 2, 3, 4]:
        print("sublist2 is correct!")
    else:
        print("sublist2 equals ", sublist2, " which is incorrect. try again!")

    if sublist1 == [4, 3, 2, 1, 0]:
        print("sublist1 is correct!")
    else:
        print("sublist1 equals ", sublist1, " which is incorrect. try again!")

    
# ------------------------------------------------------------------------------------
def check_answers_l2_ex4(globals_dict):
    if not 'mymat1' in globals_dict:
        print("You've not created a variable 'mymat1'. Try again!")
        return
    
    mymat1 = globals_dict['mymat1']

    if mymat1 == [ [1, 2, 3], [4, 5, 6], [7, 8, 9] ]:
        print("mymat1 is correct!")
    else:
        print("mymat1 equals ", mymat1, " which is incorrect. try again!")


# ------------------------------------------------------------------------------------
def check_answers_l2_ex5(globals_dict):
    if not 'mydict1' in globals_dict:
        print("You've not created a variable 'mydict1'. Try again!")
        return

    if not 'mydict2' in globals_dict:
        print("You've not created a variable 'mydict2'. Try again!")
        return

    if not 'mydict3' in globals_dict:
        print("You've not created a variable 'mydict3'. Try again!")
        return
    
    mydict1 = globals_dict['mydict1']
    mydict2 = globals_dict['mydict2']
    mydict3 = globals_dict['mydict3']


    if type(mydict1) == dict and len(mydict1) == 0:
        print("Well done - you've created an empty dictionary!!")
    else:
        if type(mydict1) != dict:
            print("Your mydict1 variable was of type ", type(mydict1), ". Try again!")
        if len(mydict1) != 0:
            print("Your mydict1 variable was not empty and had ", len(mydict1), " entries. Try again!")

    if mydict2 == {'one':1, 'two':2}:
        print("Well done - mydict2 is correct!")
    else:
        print("mydict2 equals ", mydict2, " which is incorrect. try again!")

    if mydict3 == {'one':1, 'two':2, 'three':3}:
        print("Well done - mydict3 is correct!")
    else:
        print("mydict3 equals ", mydict3, " which is incorrect. try again!")

# ------------------------------------------------------------------------------------
def conditional_values():
    return 56, 3, 1, 89

# ------------------------------------------------------------------------------------
def check_answers_l2_ex6(globals_dict):
    if not 'seven_list' in globals_dict:
        print("You've not created a variable 'seven_list'. Try again!")
        return

    if not 'mymat2' in globals_dict:
        print("You've not created a variable 'my_mat2'. Try again!")
        return

    seven_list = globals_dict['seven_list']
    mymat2 = globals_dict['mymat2']

    seven_list_test = []

    for i in range(0, 11):
        seven_list_test.append(i * 7)
        
    if seven_list == seven_list_test:
        print("Well done - seven_list is correct!")
    else:
        print("seven_list equals ", seven_list, " which is incorrect. try again!")

    mymat2_test = []
    for i in range(0, 10):
        mymat2_test.append([])
        for j in range(1, 11):
            mymat2_test[i].append(i * 10 + j)

    if mymat2 == mymat2_test:
        print("Well done - mymat2 is correct!")
    else:
        print("mymat2 equals ", mymat2, " which is incorrect. try again!")
        
# ------------------------------------------------------------------------------------

def genetic_code():
    return open("genetic_code.tsv").read()

def exon_regions():
    return open("lactase_exon.tsv").read()

def lactase_gene():
    dna = ''
    lactose_file = open("lactase_gene.txt")

    for ln in lactose_file.readlines():
        dna += ln.strip()

    return dna

def population_data():
    return open("pop_data.txt").read()
