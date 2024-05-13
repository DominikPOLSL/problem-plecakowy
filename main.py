import random
import json

# Parametry algorytmu genetycznego
POP_SIZE = 100  # Rozmiar populacji
GENERATIONS = 100  # Liczba pokoleń
MUTATION_RATE = 0.1  # Prawdopodobieństwo mutacji
CROSSOVER_RATE = 0.8  # Prawdopodobieństwo krzyżowania

# Parametry problemu plecakowego
MAX_WEIGHT = 50  # Maksymalna waga plecaka
ITEMS = [
    {"name": "A", "weight": 10, "value": 60},
    {"name": "B", "weight": 20, "value": 100},
    {"name": "C", "weight": 30, "value": 120},
    {"name": "D", "weight": 15, "value": 80},
    {"name": "E", "weight": 25, "value": 110}
]

def generate_individual():
    return [random.choice([0, 1]) for _ in range(len(ITEMS))]

def fitness(individual):
    total_weight = sum(individual[i] * ITEMS[i]["weight"] for i in range(len(individual)))
    total_value = sum(individual[i] * ITEMS[i]["value"] for i in range(len(individual)))
    if total_weight > MAX_WEIGHT:
        return 0  # Odrzucamy rozwiązanie, jeśli przekracza limit wagowy
    else:
        return total_value

def crossover(parent1, parent2):
    point = random.randint(1, len(parent1) - 1)
    child1 = parent1[:point] + parent2[point:]
    child2 = parent2[:point] + parent1[point:]
    return child1, child2

def mutate(individual):
    index = random.randint(0, len(individual) - 1)
    individual[index] = 1 - individual[index]  # Zamiana 0 na 1 lub 1 na 0
    return individual

def select_parents(population):
    return random.choices(population, weights=[fitness(ind) for ind in population], k=2)

def genetic_algorithm():
    population = [generate_individual() for _ in range(POP_SIZE)]
    for _ in range(GENERATIONS):
        new_population = []
        for _ in range(POP_SIZE // 2):
            parent1, parent2 = select_parents(population)
            if random.random() < CROSSOVER_RATE:
                child1, child2 = crossover(parent1, parent2)
            else:
                child1, child2 = parent1, parent2
            if random.random() < MUTATION_RATE:
                child1 = mutate(child1)
            if random.random() < MUTATION_RATE:
                child2 = mutate(child2)
            new_population.extend([child1, child2])
        population = new_population

    best_individual = max(population, key=fitness)
    best_item_selection = [{"name": ITEMS[i]["name"], "selected": best_individual[i]} for i in range(len(best_individual))]
    best_fitness = fitness(best_individual)

    with open("best_solution.json", "w") as json_file:
        json.dump({"items": best_item_selection, "total_value": best_fitness}, json_file, indent=4)

    return best_item_selection, best_fitness

if __name__ == "__main__":
    random.seed(3)
    best_solution, best_fitness = genetic_algorithm()
    print("Najlepsze rozwiązanie:", best_solution)
    print("Wartość plecaka:", best_fitness)