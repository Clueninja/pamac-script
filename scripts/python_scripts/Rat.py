import random
def asort(e):
    return e.weight

class Rat:
    def __init__(self, weight):
        self.weight = weight

class Population:
    def __init__(self):
        self.Male = []
        self.Female = []
        self.population = 0
    
    def get_pop(self):
        self.population = len(self.Male)+len(self.Female)
        return self.population
    
    def get_av_fitness(self, target_weight):
        asum = 0
        for rat in self.Male+self.Female:
            asum+=rat.weight
        return asum/(target_weight*self.get_pop())
    
    def cull(self):
        self.Male.sort( reverse=False, key= asort)
        self.Female.sort(reverse=False, key= asort)
        for _n in range(40):
            self.Male.pop(0)
            self.Female.pop(0)

        
    
    def mutate(self, mutationrate):
        for rat in self.Male:
            if random.randint(0,mutationrate) ==0:
                rat.weight = rat.weight * random.uniform(0.5,1.2)

        for rat in self.Female:
            if random.randint(0,mutationrate) ==0:
                rat.weight = rat.weight * random.uniform(0.5,1.2)
        

    def breed(self):
        random.shuffle(self.Male)
        random.shuffle(self.Female)
        num = 0
        if len(self.Male)< len(self.Female):
            num = len(self.Male)
        else:
            num = len(self.Female)
        
        for n in range(num):
            weight = (self.Male[n].weight +self.Female[n].weight)/2
            if random.randint(0,1) ==0:
                self.Male.append(Rat(weight))
            else:
                self.Female.append(Rat(weight))
                
if __name__ == "__main__":
    pop = Population()
    for _n in range(100):
        pop.Male.append(Rat(random.randint(100,400)))
        pop.Female.append(Rat(random.randint(100,400)))
    
    while True:
        pop.mutate(20)
        pop.breed()
        pop.cull()
        print(pop.get_av_fitness(50000))
        print(pop.get_pop())





