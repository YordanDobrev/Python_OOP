from typing import List

from project.animal import Animal
from project.worker import Worker


class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals: List[Animal] = []
        self.workers: List[Worker] = []

    def add_animal(self, animal: Animal, price):
        if self.__budget >= price and self.__animal_capacity > len(self.animals):
            self.animals.append(animal)
            self.__budget -= price
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
        elif self.__animal_capacity > len(self.animals) and self.__budget < price:
            return "Not enough budget"
        return "Not enough space for animal"

    def hire_worker(self, worker: Worker):
        if self.__workers_capacity > len(self.workers):
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self, worker_name):
        try:
            worker = [w for w in self.workers if w.name == worker_name][0]
            self.workers.remove(worker)
            return f"{worker_name} fired successfully"
        except IndexError:
            return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        total_salaries = sum([s.salary for s in self.workers])

        if total_salaries <= self.__budget:
            self.__budget -= total_salaries
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        total_food = sum(food.money_for_care for food in self.animals)
        if total_food <= self.__budget:
            self.__budget -= total_food
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        total_lions = [l for l in self.animals if l.__class__.__name__ == "Lion"]
        total_tigers = [t for t in self.animals if t.__class__.__name__ == "Tiger"]
        total_cheetah = [c for c in self.animals if c.__class__.__name__ == "Cheetah"]

        result = f"You have {len(self.animals)} animals"
        result += f"\n----- {len(total_lions)} Lions:"
        for lion in total_lions:
            result += f"\n{lion}"

        result += f"\n----- {len(total_tigers)} Tigers:"
        for tigers in total_tigers:
            result += f"\n{tigers}"

        result += f"\n----- {len(total_cheetah)} Cheetahs:"
        for cheetah in total_cheetah:
            result += f"\n{cheetah}"

        return result

    def workers_status(self):
        total_keepers = [k for k in self.workers if k.__class__.__name__ == "Keeper"]
        total_caretaker = [c for c in self.workers if c.__class__.__name__ == "Caretaker"]
        total_vet = [v for v in self.workers if v.__class__.__name__ == "Vet"]

        result = f"You have {len(self.workers)} workers"
        result += f"\n----- {len(total_keepers)} Keepers:"
        for keep in total_keepers:
            result += f"\n{keep}"

        result += f"\n----- {len(total_caretaker)} Caretakers:"
        for care in total_caretaker:
            result += f"\n{care}"

        result += f"\n----- {len(total_vet)} Vets:"
        for vet in total_vet:
            result += f"\n{vet}"

        return result