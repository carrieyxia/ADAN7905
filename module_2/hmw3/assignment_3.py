# 1. Write a Python program that computes the factorial of an integer using recursive function.
def compute_factorial(x:int):
    """
    This function takes a integer variable x and compute its factorial.
    """
    i = 0 
    factorial = 1
    while i < x :
        factorial *=(x-i)
        # print(f'iteration{i}: factorial = {factorial}')
        i +=1
    return factorial

# 2. Write a program to process file of DNA text (ATGCAATTGCTCGATTAG) - Human coronavirus HKU1.fasta Download Human coronavirus HKU1.fastaand Count the percent of C+G present in the DNA.

def process_file(filename):
    genes = open_file(filename)
    percent_CG = percentCG(genes)
    return(percent_CG)


def percentCG(genes):
    count = 0
    for gene in genes:
        if gene == "C" or gene =="G":
            count +=1
    percent = count/len(genes)
    return percent



def open_file(filename):
    """
    """
    f = open(filename, encoding='UTF8')

    genome_line = f.readlines()[1:]
    for genome in genome_line:
        genome = str(genome)
    
    lst = []
    for gene in genome:
        lst.append(gene)

    return lst
    # for gene in genome_lines:


# 3. Given a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]. Write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it.
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
b = [num for num in a if num%2==0]


def main():

#    print(compute_factorial(4))
#    open_file("human_corona.fasta")
   test = ['A', 'T', 'G', 'C', 'A', 'A', 'T', 'T', 'G', 'C', 'T', 'C', 'G', 'A', 'T', 'T', 'A', 'G']
#    print(percentCG(test))
   print(process_file("human_corona.fasta"))
   print(b)



if __name__ == "__main__":
    main()