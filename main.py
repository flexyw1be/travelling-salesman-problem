from random import shuffle, randint

LIST = {0: [0, 3, 6, 4, 5], 1: [3, 0, 7, 11, 8], 2: [6, 7, 0, 6, 11], 3: [4, 9, 6, 0, 2], 4: [5, 8, 11, 2, 0]}


def get_fitness(gene_list):
    fitness = 0
    for ind in range(len(gene_list) - 1):
        fitness += LIST[gene_list[ind]][gene_list[ind + 1]]
    return fitness


class Chromosome:
    def __init__(self):
        self.gene_list = self.generate_chromosome()
        self.gene_list += [get_fitness(self.gene_list)]

    def generate_chromosome(self):
        gene_list = [0, 1, 2, 3, 4]
        shuffle(gene_list)
        return gene_list + [gene_list[0]]

    def __str__(self):
        s = ' '.join(list(map(str, self.gene_list)))
        return s


class Population:
    def __init__(self, size):
        self.size = size
        self.population = []
        self.population = [Chromosome() for i in range(self.size)]
        self.population = sorted(self.population, key=lambda x: x.gene_list[-1])

    def __str__(self):
        s = ''
        for i in self.population:
            s += f'{i.gene_list}\n'
        return s


p = Population(10)
print(p)

# TODO:
# funcs: merge and choice
# make good print with count of epoch`s
