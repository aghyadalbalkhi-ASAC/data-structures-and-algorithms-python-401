from data_structures_and_algorithms.data_structures.fifo_animal_shelter.fifo_animal_shelter import AnimalShelter,Cat,Dog

def test_AnimalShelter_Enqueue():
    sherry=Cat('sherry')
    ossccaar=Dog('ossccaar')
    owow=Dog('owow')
    animals=AnimalShelter()
    animals.enqueue(sherry)
    animals.enqueue(ossccaar)
    animals.enqueue(owow)
    assert animals.print_() == 'sherry -> ossccaar -> owow -> '

def test_AnimalShelter_Dequeue_Dog():
    sherry=Cat('sherry')
    ossccaar=Dog('ossccaar')
    owow=Dog('owow')
    animals=AnimalShelter()
    animals.enqueue(sherry)
    animals.enqueue(ossccaar)
    animals.enqueue(owow)
    animals.dequeue('Dog')
    assert animals.print_() == 'sherry -> owow -> '

def test_AnimalShelter_Dequeue_Cat():
    sherry=Cat('sherry')
    ossccaar=Dog('ossccaar')
    owow=Dog('owow')
    animals=AnimalShelter()
    animals.enqueue(sherry)
    animals.enqueue(ossccaar)
    animals.enqueue(owow)
    animals.dequeue('Cat')
    assert animals.print_() == 'ossccaar -> owow -> '