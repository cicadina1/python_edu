seq = "AACTGAGAC"

def split(sequence):
    return [char for char in seq]
word = 'sequence'
seqlist=(split(word))
print("Task 1: разделена секвенция\n",seqlist)

def revetring (sequence):
    reversed_seq = seqlist[::-1]
    #reversed_seq =  ''.join(reversed_seq)
    return reversed_seq
print("Task 2: обратна секвенция\n",revetring(seq))

def complimentation (sequence):
    compsequence=[]
    for x in range(len(seqlist)):
        if   sequence[x] == "A": compsequence.append("T")
        elif sequence[x] == "T": compsequence.append("A")
        elif sequence[x] == "C": compsequence.append("G")
        else: compsequence.append("C")
    #compsequence = ''.join(compsequence)
    return compsequence
print("Task 3: комплементарна секвенция\n",complimentation(seq))

compl_rev_seq=revetring(seq)
compl_rev_seq=complimentation(compl_rev_seq)

print("Task 4: комплементарна обратна секвенция\n",compl_rev_seq)
