import random

# ------------------------------------------------------------------------------------
def check_answers_l2_ex1(globals_dict):
    if not 'file_contents1' in globals_dict:
        print("You've not created a variable 'file_contents1'. Try again!")
        return

    if not 'file_contents2' in globals_dict:
        print("You've not created a variable 'file_contents2'. Try again!")
        return

    if not 'file_contents3' in globals_dict:
        print("You've not created a variable 'file_contents3'. Try again!")
        return
    
    file_contents1 = globals_dict['file_contents1']
    file_contents2 = globals_dict['file_contents2']
    file_contents3 = globals_dict['file_contents3']

    my_file_contents1 = open("TheRaven.txt").read()

    my_file_contents2 = []
    for ln in open("TheRaven.txt").readlines():
        my_file_contents2.append(ln.strip())
    
    my_file_contents3 = open("TheRaven.txt").read(50)

    if my_file_contents1 == file_contents1:
        print("Well done - file_contents1 contains the whole file!")
    else:
        print("Your file_contents1 variable does not contain the whole file. Try again!")

    if my_file_contents2 == file_contents2:
        print("Well done - file_contents2 contains the whole file with lines separated into a list!")
    else:
        print("Your file_contents2 variable does not contain a list of the file contents without newlines. Try again!")

    if my_file_contents3 == file_contents3:
        print("Well done - file_contents3 contains the first 50 bytes of the file!")
    else:
        print("Your file_contents3 variable does not contain the first 50 bytes of the file. Try again!")


def check_answers_l2_ex2(globals_dict):

    my_file_contents2 = []
    for ln in open("TheRaven.txt").readlines():
        my_file_contents2.append(ln.strip())
        
    out_str = ""
    num = 1
    for ln in my_file_contents2:
        out_str += str(num) + " " + ln + '\n'
        num += 1

    try:
        file_contents1 = open("TheRavenCopy.txt").read()
    except FileNotFoundError:
        print("Could not find a file called 'TheRavenCopy.txt' in the current directory. Please try again!")
        return

    if out_str == file_contents1 or out_str.strip() == file_contents1.strip():
        print("Well done - Your TheRavenCopy.txt file has the line numbers added at the start of each line!")
    else:
        print("Your TheRavenCopy.txt file doesn't contain the correct line numbers at the start of each line - Have another go!")


def check_answers_l2_ex3(globals_dict):
    my_list = [1, 5, 8, 9]
    my_mult = 5

    if not "list_multiply1" in globals_dict:
        print("Could not find a function called 'list_multiply1' - Make sure you've defined it properly!")
        return

    if not "list_multiply2" in globals_dict:
        print("Could not find a function called 'list_multiply2' - Make sure you've defined it properly!")
        return

    list_multiply1 = globals_dict['list_multiply1']
    list_multiply1(my_list, my_mult)

    if my_list == [5, 25, 40, 45]:
        print("Your 'list_multiply1' function multiplied the elements of the list by the given numerical argument. Well done!")
    else:
        print("Your 'list_multiply1' function didn't seem to multiply the incoming list by the numerical argument. Try Again!")

    my_list = [1, 5, 8, 9]
    list_multiply2 = globals_dict['list_multiply2']
    try:
        my_list2 = list_multiply2(my_list)
    except TypeError:
        print("Your 'list_multiply2' function doesn't have a default numerical argument - have another go!")
        return

    if my_list2 == [9, 45, 72, 81] and my_list == [1, 5, 8, 9]:
        print("Your 'list_multiply2' function multiplied the elements of the list by a given numerical argument and returned the result. Well done!")
    elif my_list2 == [9, 45, 72, 81] and my_list != [1, 5, 8, 9]:
        print("Though your 'list_multiply2' function multiplied the list by a given numerical argument it also altered the incoming list - try again!")
    elif my_list2 != [9, 45, 72, 81] and my_list == [1, 5, 8, 9]:
        print("Though your 'list_multiply2' function didn't alter the incoming list it also didn't multiply the list correctly = have another go!")
    else:
        print("Your function didn't mulitply the incoming list correctly and it altered the incoming list - try again!")
        
def check_answers_l4_ex1(globals_dict):
    
    if not 'load_dna' in globals_dict:
        print("You've not created a function 'load_dna'. Try again!")
        return

    load_dna = globals_dict['load_dna']

    dna = load_dna('gene.fna')

    my_dna = ''
    for ln in open('gene.fna').readlines():
        if ln[0] == '>':
            continue

        my_dna += ln.strip()

    if dna == my_dna:
        print("Well done - Your load_dna function loads in the DNA string from the .fna file as expected!")
    else:
        print("Calling your load_dna doesn't return the correct DNA sequence from gene.fna. Try again!")


def check_answers_l4_ex2(globals_dict):
    if not 'load_exon_sequences' in globals_dict:
        print("You've not created a function 'load_exon_sequences'. Try again!")
        return

    load_exon_sequences = globals_dict['load_exon_sequences']

    exons = load_exon_sequences('exons.fa')
    
    myfile = open('exons.fa')
    exon_string = ''
    for ln in myfile.readlines():
        if ln[0] == '>':
            exon_string += ","
        else:
            exon_string += ln
            
    myexons =  exon_string.replace('\n', '').split(',')[1:]

    if myexons == exons:
        print("Well done - Your load_exon_sequences function loads in the exon sequences as expected!")
    else:
        print("Calling your load_exon_sequences function doesn't return the expected exon regions. Try again!")
        
def check_answers_l4_ex3(globals_dict):
    if not 'load_exon_regions' in globals_dict:
        print("You've not created a function 'load_exon_regions'. Try again!")
        return

    load_exon_regions = globals_dict['load_exon_regions']
    load_dna = globals_dict['load_dna']

    exon_list = load_exon_regions('exons.fa', load_dna('gene.fna'))

    my_exon_list = [{'start': 0, 'end': 142}, {'start': 272, 'end': 495},  {'start': 1345, 'end': 1608}]
    if my_exon_list == exon_list:
        print("Well done - Your load_exon_regions correctly identifies the exon regions and returns them as expected!")
    else:
        print("Calling your load_exon_regions function didn't return the exon regions list correctly. Try again!")


def check_answers_l4_ex4(protein):
    if protein == "MVHLTPEEKSAVTALWGKVNVDEVGGEALGRLLVVYPWTQRFFESFGDLSTPDAVMGNPKVKAHGKKVLGAFSDGLAHLDNLKGTFATLSELHCDKLHVDPENFRLLGNVLVCVLAHHFGKEFTPPVQAAYQKVVAGVANALAHKYH":
        print("Well done - Your protein string is correct!")
    else:
        print("Your protein string was not correct - Try again!")

def check_answers_l4_ex5(protein):
    if protein == "MVHLTPVEKSAVTALWGKVNVDEVGGEALGRLLVVYPWTQRFFESFGDLSTPDAVMGNPKVKAHGKKVLGAFSDGLAHLDNLKGTFATLSELHCDKLHVDPENFRLLGNVLVCVLAHHFGKEFTPPVQAAYQKVVAGVANALAHKYH":
        print("Well done - Your protein string contains the correct mutation!")
    else:
        print("Your mutated protein string was not correct - Try again!")
