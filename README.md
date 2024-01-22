
Genetic algorithm for traveling salesman problem

```
class Chromosome:
    def __init__(self):
        self.gene_list = self.generate_chromosome()
        self.gene_list += [get_fitness(self.gene_list)]
```

```
class Population:
    def __init__(self, size):
        self.size = size
        self.population = []
        self.population = [Chromosome() for i in range(self.size)]
        self.population = sorted(self.population, key=lambda x: x.gene_list[-1])
```
```
def get_fitness(gene_list):
    fitness = 0
    for ind in range(len(gene_list) - 1):
        fitness += LIST[gene_list[ind]][gene_list[ind + 1]]
    return fitness
```
