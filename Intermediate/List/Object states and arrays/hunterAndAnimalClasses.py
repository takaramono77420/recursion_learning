class Animal:

    def __init__(self, species, weightKg, heightM, predator):
        self.species = species
        self.weightKg = weightKg
        self.heightM = heightM
        self.predator = predator
    
    def domesticate(self):
        self.predator = False
    
class Hunter:

    def __init__(self, name, weightKg, heightM, strength, cageCubicMeters):
        self.name = name
        self.weightKg = weightKg
        self.heightM = heightM
        self.strength = strength
        self.cageCubicMeters = cageCubicMeters
    
    def strengthKg(self):
        return self.strength * self.weightKg
    
    def canCaptureAnimal(self, animal):
        if self.strengthKg() >= animal.weightKg and self.cageCubicMeters >= animal.heightM and not animal.predator:
            return True
    
    def attemptToDomesticate(self, animal):

        if self.strengthKg() > animal.weightKg * 2:
            animal.domesticate()
            return True
        
        return False

def capturedAnimals(hunter, animals):

    array = []

    for animal in animals:

        if hunter.canCaptureAnimal(animal):
            array.append(animal)
    
    return array

def domesticateTheAnimals(hunter, animals):

    array = []

    for animal in animals:
        if animal.predator == False:
            array.append(animal)
        else:
            if hunter.attemptToDomesticate(animal):
                array.append(animal)
    
    return array


tiger = Animal("Tiger", 290, 2.6, True)

cow = Animal("Cow", 1134, 1.5, False)

snake = Animal("Snake", 100, 1.2, True)

cat = Animal("Cat", 10, 0.5, False)

hunternator = Hunter("Hunternator", 124.73, 1.85, 15, 3)

animals = [tiger, cow, snake, cat]

list_a = capturedAnimals(hunternator, animals)

for animal in list_a:
    print(animal.species)

list_b = domesticateTheAnimals(hunternator, animals)

for animal in list_b:
    print(animal.species)