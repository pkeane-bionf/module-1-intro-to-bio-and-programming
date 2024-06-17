def load_amino_acid_map(fname):
    acids = {}
    for ln in open(fname).readlines():
        # split each line and create the dictionary entry
        tokens = ln.split()
        acids[tokens[0]] = {'1-letter':tokens[1], '3-letter':tokens[2], 'amino acid': tokens[3]}
        
    return acids

def create_protein_string(dna):

    exon_list = [{'start': 0, 'end': 142}, {'start': 272, 'end': 495}, {'start': 1345, 'end': 1608}]
    acids = load_amino_acid_map("genetic_code.tsv")
    
    # pick out and concatenate the exon regions from the original sequence to produce the mRNA
    mrna = ""
    for exon in exon_list:
        mrna += dna[exon['start']:exon['end']]

    mrna = mrna.replace('T', 'U')

    # Loop over triplets and create protein string
    protein = ""
    i = mrna.find('AUG')
    
    while i < len(mrna):
        triplet = mrna[i:i+3]

        if not triplet:
            break
        
        # is the triplet an X codon? If so break out of loop
        if acids[triplet]['1-letter'] == 'X':
            break

        # record in protein string
        protein += acids[triplet]['1-letter']

        # increment counter
        i += 3
        
    return protein

def check_answers_task1(fn1, fn2):
    if not callable(fn1):
        print("WARNING - dna_comparison not a function!")
        return
    
    if not callable(fn2):
        print("WARNING - protein_comparison not a function!")
        return

    print("Both dna_comparison and protein_comparison exist and are callable")

def check_answers_task2(fn1, fn2):
    if not callable(fn1):
        print("WARNING - mutation_dna not a function!")
        return
    
    if not callable(fn2):
        print("WARNING - generate_mutations not a function!")
        return


    print("Both mutation_dna and generate_mutations exist and are callable")
    
