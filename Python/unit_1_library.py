import random

# ------------------------------------------------------------------------------------
def check_answers_l3_ex1(globals_dict):
    if not 'myint' in globals_dict:
        print("You've not created a variable 'myint'. Try again!")
        return
    if not 'myfloat' in globals_dict:
        print("You've not created a variable 'myfloat'. Try again!")
        return
    if not 'mystr1' in globals_dict:
        print("You've not created a variable 'mystr1'. Try again!")
        return
    if not 'mystr2' in globals_dict:
        print("You've not created a variable 'mystr2'. Try again!")
        return
        
    myint = globals_dict['myint']
    myfloat = globals_dict['myfloat']
    mystr1 = globals_dict['mystr1']
    mystr2 = globals_dict['mystr2']
    
    if type(myint) == int:
        print("Well done - you've created an integer!")
    else:
        print("Your myint variable was of type ", type(myint), ". Try again!")
    
    if type(myfloat) == float:
        print("Well done - you've created a float!")
    else:
        print("Your myfloat variable was of type ", type(myfloat), ". Try again!")
    
    if type(mystr1) == str:
        print("Well done - you've created a string!")
    else:
        print("Your mystr1 variable was of type ", type(mystr1), ". Try again!")
    
    if mystr2 == mystr1:
        print("Well done - your mystr2 variable equals the mystr1 variable")
    else:
        print("Your mystr2 does not equal the mystr1 variable. Try again!")

# ------------------------------------------------------------------------------------
def check_answers_l3_ex2(globals_dict):
    if not 'var3' in globals_dict:
        print("You've not created a variable 'var3'. Try again!")
        return
    if not 'var4' in globals_dict:
        print("You've not created a variable 'var4'. Try again!")
        return
    if not 'var5' in globals_dict:
        print("You've not created a variable 'var5'. Try again!")
        return
    
    var3 = globals_dict['var3']
    var4 = globals_dict['var4']
    var5 = globals_dict['var5']

    if var3 == 15:
        print("var3 is correct!")
    else:
        print("var3 equals ", var3, " which is incorrect. try again!")
    
    if var4 == 63:
        print("var4 is correct!")
    else:
        print("var4 equals ", var4, " which is incorrect. try again!")
    
    if var5 == 9/7:
        print("var5 is correct!")
    else:
        print("var5 equals ", var5, " which is incorrect. try again!")
# ------------------------------------------------------------------------------------
def check_answers_l3_ex3(globals_dict):
    if not 'num1' in globals_dict:
        print("You've not created a variable 'num1'. Try again!")
        return
    if not 'num2' in globals_dict:
        print("You've not created a variable 'num2'. Try again!")
        return
    if not 'len1' in globals_dict:
        print("You've not created a variable 'len1'. Try again!")
        return
    if not 'str3' in globals_dict:
        print("You've not created a variable 'str3'. Try again!")
        return
    
    num1 = globals_dict['num1']
    num2 = globals_dict['num2']
    len1 = globals_dict['len1']
    str3 = globals_dict['str3']

    if num1 == 78.2:
        print("num1 is correct!")
    else:
        print("num1 equals ", num1, " which is incorrect. try again!")
    
    if len1 == 14:
        print("len1 is correct!")
    else:
        print("len1 equals ", len1, " which is incorrect. try again!")
    
    if str3 == '78.2':
        print("str3 is correct!")
    elif type(str3) != str:
        print("The *type* of str3 is incorrect. It should be a string and it is a ", type(str3))
    else:
        print("str3 equals ", str3, " which is incorrect. try again!")
    
    if num2 == 78.2:
        print("num2 is correct!")
    elif type(num2) != float:
        print("The *type* of num2 is incorrect. It should be a float and it is a ", type(num2))
    else:
        print("num2 equals ", num2, " which is incorrect. try again!")

# ------------------------------------------------------------------------------------
def check_answers_l3_ex4(globals_dict):
    if not 'myvar1' in globals_dict:
        print("You've not created a variable 'myvar1'. Try again!")
        return
    if not 'myvar2' in globals_dict:
        print("You've not created a variable 'myvar2'. Try again!")
        return
    if not 'myvar3' in globals_dict:
        print("You've not created a variable 'myvar3'. Try again!")
        return
    
    myvar1 = globals_dict['myvar1']
    myvar2 = globals_dict['myvar2']
    myvar3 = globals_dict['myvar3']

    if myvar1 == 3:
        print("myvar1 is correct!")
    else:
        print("myvar1 equals ", myvar1, " which is incorrect. try again!")

    if myvar2 == ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']:
        print("myvar2 is correct!")
    else:
        print("myvar2 equals ", myvar2, " which is incorrect. try again!")
    
    if myvar3 == 'The quick brown duck jumps over the lazy dog':
        print("myvar3 is correct!")
    else:
        print("myvar3 equals ", myvar3, " which is incorrect. try again!")

# ------------------------------------------------------------------------------------        
def __generate_dna_sequence(N, seed = 10):
    random.seed(seed)
    bases = ['A', 'C', 'G', 'T']
    dna = ''
    for _ in range (0, N):
        dna += random.choice(bases)

    return dna

def dna1():
    return __generate_dna_sequence(76, 10)

def dna2():
    return __generate_dna_sequence(61, 11)

def dna3():
    return __generate_dna_sequence(98, 12) + dna1() + __generate_dna_sequence(101, 13)


def check_answers_l4_ex1(globals_dict):

    len_dna1 = globals_dict['len_dna1']
    len_dna2 = globals_dict['len_dna2']
    len_dna3 = globals_dict['len_dna3']

    num_A = globals_dict['num_A']
    num_C = globals_dict['num_C']
    num_G = globals_dict['num_G']
    num_T = globals_dict['num_T']

    combined_sequence = globals_dict['combined_sequence']
    base_pos = globals_dict['base_pos']

    if len_dna1 != 76:
        print("len_dna1 isn't correct - try again!")
    else:
        print("len_dna1 is correct - Well Done!")

    if len_dna2 != 61:
        print("len_dna2 isn't correct - try again!")
    else:
        print("len_dna2 is correct - Well Done!")

    if len_dna3 != 275:
        print("len_dna3 isn't correct - try again!")
    else:
        print("len_dna3 is correct - Well Done!")

    if combined_sequence != dna1() + dna2():
        print("combined_sequence isn't correct - try again!")
    else:
        print("combined_sequence is correct - Well Done!")
        
    if num_A != 54:
        print("num_A isn't correct - try again!")
    else:
        print("num_A is correct - Well Done!")

    if num_C != 78:
        print("num_C isn't correct - try again!")
    else:
        print("num_C is correct - Well Done!")

    if num_G != 71:
        print("num_G isn't correct - try again!")
    else:
        print("num_G is correct - Well Done!")

    if num_T != 72:
        print("num_T isn't correct - try again!")
    else:
        print("num_T is correct - Well Done!")

    if base_pos != 98:
        print("base_pos isn't correct - try again!")
    else:
        print("base_pos is correct - Well Done!")
        
# ------------------------------------------------------------------------------------        
def generate_dna_sequence(N):
    bases = ['A', 'C', 'G', 'T']
    dna = ''
    for _ in range (0, N):
        dna += random.choice(bases)

    return dna

def dna_analyser_v1(dna):
    bases = {'A':0, 'C':0, 'G':0, 'T':0}
    total = 0

    for b1 in bases:
        for b2 in dna:
            if not b2 in bases:
                print("Unknown character encountered in DNA sequence:  " + b2 + ". Aborting.")
                return
            if b2 == b1:
                bases[b1] += 1
            
        total += bases[b1]
        
    print("Bases percentage: ")
    print("   A - ",  100 * bases['A']/total, "%")
    print("   C - ",  100 * bases['C']/total, "%")
    print("   G - ",  100 * bases['G']/total, "%")
    print("   T - ",  100 * bases['T']/total, "%")

def dna_analyser_v2(dna):
    total = len(dna)
    print("Bases percentage: ")
    print("   A - ",  100 * dna.count('A')/total, "%")
    print("   C - ",  100 * dna.count('C')/total, "%")
    print("   G - ",  100 * dna.count('G')/total, "%")
    print("   T - ",  100 * dna.count('T')/total, "%")

def check_answers_l4_ex2(globals_dict):

    time_v1 = globals_dict['time_v1']
    time_v2 = globals_dict['time_v2']

    if time_v1 < 1.0 or time_v1 > 3.0:
        print("time_v1 doesn't seem correct (between 1.0 and 3.0) - try again!")
    else:
        print("time_v1 is correct - Well Done!")

    if time_v1 < 0.2:
        print("time_v2 doesn't seem correct (less than 0.2) - try again!")
    else:
        print("time_v2 is correct - Well Done!")

        
# ------------------------------------------------------------------------------------        
def dna_experiment_output():
    dna = ""
    for i in range(0, 30):
        dna += "***:  " + __generate_dna_sequence(50, i) + "\n"

    return dna
        
def get_time():
    import time
    return time.time()
