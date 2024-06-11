import random
import json

random.seed(10)


items = [
    {"value": 60, "weight": 10},
    {"value": 100, "weight": 20},
    {"value": 120, "weight": 30},
    {"value": 30, "weight": 5},
    {"value": 90, "weight": 25},
    {"value": 80, "weight": 15},
    {"value": 70, "weight": 10},
    {"value": 50, "weight": 12},
    {"value": 40, "weight": 8},
    {"value": 200, "weight": 35},
    {"value": 110, "weight": 22},
    {"value": 150, "weight": 28},
    {"value": 65, "weight": 14},
    {"value": 95, "weight": 18},
    {"value": 85, "weight": 16},
    {"value": 75, "weight": 13},
    {"value": 55, "weight": 9},
    {"value": 135, "weight": 23},
    {"value": 125, "weight": 21},
    {"value": 145, "weight": 29},
]

max_weight = 100
population_size = 100
generations = 50
mutation_rate = 0.01


# Funkcja oceny osobnika
def fitness(individual):
    value = 0
    weight = 0
    for i in range(len(individual)):
        if individual[i] == 1:
            value += items[i]["value"]
            weight += items[i]["weight"]
    if weight > max_weight:
        return 0
    return value


# Tworzenie początkowej populacji
def create_population(population_size):
    return [[random.randint(0, 1) for i in range(len(items))] for i in range(population_size)]


# Selekcja ruletkowa
def roulette_selection(population):
    max_fitness = sum(fitness(i) for i in population)
    pick = random.uniform(0, max_fitness)
    current = 0
    for i in population:
        current += fitness(i)
        if current > pick:
            return i


# Krzyżowanie dwóch osobników
def crossover(parent1, parent2):
    point = random.randint(1, len(items) - 1)
    return parent1[:point] + parent2[point:]


# Mutacja osobnika
def mutate(individual):
    total_weight = sum(items[i]['weight'] for i in range(len(individual)) if individual[i])
    for i in range(len(individual)):
        if random.random() < mutation_rate:
            individual[i] = 1 - individual[i]
            new_total_weight = total_weight + items[i]['weight'] if individual[i] else total_weight - items[i]['weight']
            if new_total_weight > max_weight:
                individual[i] = 1 - individual[i]
            else:
                total_weight = new_total_weight


# Algorytm genetyczny
def genetic_algorithm():
    population = create_population(population_size)
    best_solution = None

    for g in range(generations):
        new_population = []
        for i in range(population_size // 2):
            parent1 = roulette_selection(population)
            parent2 = roulette_selection(population)
            child1 = crossover(parent1, parent2)
            child2 = crossover(parent2, parent1)
            mutate(child1)
            mutate(child2)
            new_population.extend([child1, child2])

        population = new_population

        best_fitness = 0


        for individual in population:
            current_fitness = fitness(individual)
            if current_fitness > best_fitness:
                best_fitness = current_fitness
                best_solution = individual


    return best_solution


best_solution = genetic_algorithm()


# Zapis najlepszego osobnika do pliku JSON
best_items = [{"value": items[i]["value"], "weight": items[i]["weight"]} for i in range(len(best_solution)) if best_solution[i] == 1]
best_fitness = fitness(best_solution)
best_weight = sum(item["weight"] for item in best_items)

with open('best_solution.json', 'w') as f:
    json.dump({"fitness": best_fitness, "items": best_items}, f, indent=4)

print(f"Fitness: {best_fitness}")
print(f"Weight: {best_weight}")
print(f"Items: {best_items}")
