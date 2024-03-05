from Animal import Animal
from Pisica import Pisica

pisica=Pisica()
caine=Animal()
sarpe=Animal()

listOfAnimals=list()
listOfAnimals.append(pisica)
listOfAnimals.append(caine)
listOfAnimals.append(sarpe)

for animal in listOfAnimals:
    animal.mananca()
