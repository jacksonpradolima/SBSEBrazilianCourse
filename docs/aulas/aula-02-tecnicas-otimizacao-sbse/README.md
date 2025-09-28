---
titulo: "Técnicas de Otimização em SBSE"
aula_numero: 2
carga_horaria: "4 horas"
foco_principal: "Dominar algoritmos de otimização e técnicas de representação para transformar problemas de engenharia de software em problemas de busca"
metodologia: "Workshop Prático"
tipo_aula: "Workshop Prático"
objetivos:
  - "Compreender os principais algoritmos de otimização aplicados em SBSE"
  - "Dominar técnicas de representação de problemas de ES como problemas de otimização"
  - "Saber projetar e implementar funções de fitness adequadas para problemas reais"
palavras_chave: ["Algoritmos Genéticos", "Simulated Annealing", "Hill Climbing", "Particle Swarm", "Representação", "Função de Fitness"]
referencias_principais:
  - "Goldberg, D. E. (1989). Genetic algorithms in search, optimization, and machine learning. Addison-Wesley."
  - "Mitchell, M. (1998). An introduction to genetic algorithms. MIT press."
  - "Talbi, E. G. (2009). Metaheuristics: from design to implementation. John Wiley & Sons."
prerequisitos:
  - "Conhecimento básico de algoritmos de busca"
  - "Compreensão dos fundamentos de SBSE (Aula 1)"
  - "Familiaridade com programação Python"
---

# Técnicas de Otimização em SBSE

## Seção 1: Abertura e Engajamento

### 1.1. Problema Motivador

Imagine que você é o arquiteto de software de uma startup fintech que está desenvolvendo um sistema de trading algorítmico. O sistema precisa processar milhões de transações por segundo, mas você tem várias decisões críticas para fazer: Qual estrutura de dados usar para o cache? Como distribuir o processamento entre os microsserviços? Quantos threads alocar para cada componente? Como configurar o garbage collector da JVM para minimizar latência?

Cada uma dessas decisões tem dezenas de opções possíveis, e elas interagem entre si de forma complexa. Testar todas as combinações manualmente levaria anos. Pior ainda: uma configuração ótima para um padrão de carga pode ser terrível para outro. Como um engenheiro de software encontra a "receita" ideal em um espaço de possibilidades que cresce exponencialmente?

Este é exatamente o tipo de problema que as técnicas de otimização em SBSE foram projetadas para resolver. Mas aqui está o desafio: não basta conhecer os algoritmos - você precisa saber **como traduzir** problemas de engenharia de software para a linguagem que estes algoritmos compreendem, e **como avaliar** se uma solução é realmente boa na prática.

### 1.2. Objetivos deste Capítulo

Ao final desta aula, você será capaz de:

- **Selecionar e aplicar** algoritmos de otimização adequados (Genetic Algorithm, Simulated Annealing, Hill Climbing, PSO) para diferentes tipos de problemas de engenharia de software
- **Projetar representações eficazes** que transformem problemas complexos de ES em formatos que algoritmos de busca possam manipular
- **Construir funções de fitness robustas** que capturem objetivos reais de qualidade de software e guiem a busca de forma eficiente

## Seção 2: Fundamentos Teóricos

### 2.1. O Ecossistema de Algoritmos de Otimização em SBSE

**Analogia Inicial:** Pense nos algoritmos de otimização como diferentes "estratégias de exploração" em um território desconhecido. Cada algoritmo é como um explorador com personalidade e habilidades distintas navegando pela paisagem de soluções.

```{mermaid}
mindmap
  root((Algoritmos de Otimização))
    Baseados em População
      Algoritmos Genéticos
        Crossover + Mutação
        Seleção por Fitness
        Diversidade Genética
      Particle Swarm Optimization
        Inteligência de Enxame
        Velocidade + Posição
        Memória Social
      Differential Evolution
        Mutação Diferencial
        Recombinação
    Busca Local
      Hill Climbing
        Greedy Local
        Rápido mas Local Optima
      Simulated Annealing
        Aceita Pioras Temporárias
        "Resfriamento" Gradual
      Tabu Search
        Memória de Movimentos
        Evita Ciclos
    Híbridos
      Memetic Algorithms
        GA + Busca Local
      Multi-Start
        Múltiplas Inicializações
```

### 2.2. Classificação por Características de Problema

Different algorithms excel at different problem characteristics:

| Característica do Problema | Algoritmo Recomendado | Porquê |
|----------------------------|----------------------|---------|
| **Espaço contínuo, suave** | Hill Climbing, Gradient-based | Gradientes bem definidos |
| **Espaço discreto, combinatorial** | Algoritmos Genéticos, Tabu Search | Operadores de combinação |
| **Múltiplos ótimos locais** | Simulated Annealing, PSO | Mecanismos de escape |
| **Avaliação custosa** | Surrogate-based, memetic | Minimiza avaliações |
| **Múltiplos objetivos** | NSGA-II, SPEA2 | Pareto-optimality |
| **Restrições complexas** | Penalty methods, repair | Tratamento de infeasibilidade |

### 2.3. Algoritmos Genéticos: O "Canivete Suíço" da SBSE

**Por que GA domina SBSE?** Algoritmos Genéticos são amplamente usados porque:

1. **Flexibilidade de Representação:** Podem codificar praticamente qualquer estrutura
2. **Robustez:** Funcionam bem mesmo com funções de fitness "ruidosas"  
3. **Paralelização Natural:** População permite processamento paralelo
4. **Interpretabilidade:** Soluções intermediárias são analisáveis

**Componentes Essenciais:**

```{mermaid}
flowchart TD
    A[População Inicial] --> B[Avaliação de Fitness]
    B --> C{Critério de Parada?}
    C -->|Não| D[Seleção de Pais]
    D --> E[Crossover]
    E --> F[Mutação]
    F --> G[Substituição]
    G --> B
    C -->|Sim| H[Melhor Solução]
    
    style A fill:#e1f5fe
    style H fill:#c8e6c9
    style C fill:#fff3e0
```

### 2.4. Simulated Annealing: O "Escalador Inteligente"

**Intuição:** Como um alpinista que ocasionalmente desce para evitar ficar preso em picos menores, buscando a montanha mais alta.

**Vantagens em SBSE:**
- **Simplicidade:** Fácil implementação e debugging
- **Garantias Teóricas:** Convergência assegurada sob condições adequadas  
- **Eficiência:** Apenas uma solução por iteração (baixo overhead)

### 2.5. Particle Swarm Optimization: A "Inteligência Coletiva"

**Analogia:** Como um bando de pássaros procurando comida - cada indivíduo segue sua própria experiência mas também aprende com o grupo.

**Aplicações em SBSE:**
- Otimização de parâmetros de configuração
- Tuning de algoritmos de machine learning
- Alocação de recursos em sistemas distribuídos

## Seção 3: Exemplo Ilustrativo

### 3.1. Problema Prático: Otimização de Configuração de Sistema Web

Vamos resolver um problema real: otimizar a configuração de um servidor web para maximizar throughput e minimizar latência.

**Variáveis de Decisão:**
- `max_connections`: 50-500 (inteiro)
- `thread_pool_size`: 10-100 (inteiro)  
- `cache_size_mb`: 64-1024 (inteiro)
- `timeout_ms`: 1000-30000 (inteiro)

**Representação como Cromossomo:**
```python
# Representação direta (real-valued encoding)
chromosome = [max_connections, thread_pool_size, cache_size_mb, timeout_ms]
# Exemplo: [200, 50, 512, 5000]

# Representação binária (para espaços discretos pequenos)
# max_connections (50-500) precisa de 9 bits: 2^9 = 512 > 450
binary_chromosome = "001100100" + "0110010" + "1000000000" + "0001001110101000"
```

**Função de Fitness Ilustrativa:**

```python
def evaluate_web_server_config(chromosome):
    max_conn, threads, cache, timeout = chromosome
    
    # Simular throughput (requests/second)
    throughput = min(max_conn * 0.8, threads * 15) * (1 + cache/2048)
    
    # Simular latência média (ms)
    latency = 10 + (max_conn / threads) * 2 + (5000 - timeout) / 1000
    
    # Penalizar configurações inválidas
    if threads > max_conn * 0.3:  # Muitos threads para poucas conexões
        throughput *= 0.7
    
    # Função objetivo composta (maximizar throughput, minimizar latência)
    fitness = throughput / (latency / 100)  # Normalização
    
    return fitness
```

**Operadores Genéticos Especializados:**

```python
def crossover_web_config(parent1, parent2):
    """Crossover uniforme com constraints de domínio"""
    child = []
    for i in range(len(parent1)):
        if random.random() < 0.5:
            child.append(parent1[i])
        else:
            child.append(parent2[i])
    
    # Aplicar constraints
    child[1] = min(child[1], child[0] // 3)  # threads <= connections/3
    
    return child

def mutate_web_config(chromosome, mutation_rate=0.1):
    """Mutação gaussiana com bounds"""
    ranges = [(50, 500), (10, 100), (64, 1024), (1000, 30000)]
    
    for i in range(len(chromosome)):
        if random.random() < mutation_rate:
            # Mutação gaussiana com 10% do range
            std_dev = (ranges[i][1] - ranges[i][0]) * 0.1
            chromosome[i] += random.gauss(0, std_dev)
            
            # Aplicar bounds
            chromosome[i] = max(ranges[i][0], 
                              min(ranges[i][1], int(chromosome[i])))
    
    return chromosome
```

### 3.2. Comparação de Convergência

```python
# Pseudocódigo de comparação
algorithms = {
    'hill_climbing': HillClimbing(neighbor_func=mutate_web_config),
    'simulated_annealing': SimulatedAnnealing(temp_schedule='exponential'),
    'genetic_algorithm': GeneticAlgorithm(pop_size=50, crossover_rate=0.8),
    'particle_swarm': ParticleSwarm(n_particles=30, inertia=0.7)
}

results = {}
for name, algo in algorithms.items():
    best_solution, fitness_history = algo.optimize(
        fitness_func=evaluate_web_server_config,
        max_evaluations=2000
    )
    results[name] = {
        'best_fitness': best_solution.fitness,
        'convergence_speed': generations_to_95_percent(fitness_history),
        'final_config': best_solution.genes
    }
```

## Seção 4: Análise e Tópicos Avançados

### 4.1. Design de Representações Sofisticadas

**Escolha da Representação é Crítica:** A representação define o espaço de busca e determina quais soluções são alcançáveis.

#### 4.1.1. Representações para Problemas de Arquitetura

**Problema:** Design automático de arquitetura de microsserviços

```python
# Representação matricial para decomposição de serviços
class MicroserviceArchitecture:
    def __init__(self, n_classes, max_services):
        # Matrix onde element[i][j] = 1 se classe i está no serviço j
        self.assignment_matrix = np.zeros((n_classes, max_services))
        
    def to_chromosome(self):
        """Converte para cromossomo linear"""
        # Cada gene representa o serviço da classe i
        return [np.argmax(row) for row in self.assignment_matrix]
    
    def from_chromosome(self, chromosome):
        """Reconstrói matriz a partir do cromossomo"""
        self.assignment_matrix.fill(0)
        for class_idx, service_idx in enumerate(chromosome):
            self.assignment_matrix[class_idx][service_idx] = 1
            
    def calculate_cohesion(self):
        """Métrica de coesão intra-serviço"""
        cohesion_sum = 0
        for service_idx in range(self.max_services):
            classes_in_service = np.where(self.assignment_matrix[:, service_idx])[0]
            if len(classes_in_service) > 1:
                # Calcular coesão baseada em dependências
                internal_deps = count_internal_dependencies(classes_in_service)
                possible_deps = len(classes_in_service) * (len(classes_in_service) - 1)
                cohesion_sum += internal_deps / possible_deps if possible_deps > 0 else 0
        return cohesion_sum
```

#### 4.1.2. Representações Variáveis e Estruturais

**Desafio:** Nem todos os problemas têm tamanho fixo.

```python
# Representação de tamanho variável para sequência de refatorações
class RefactoringSequence:
    def __init__(self):
        self.operations = []  # Lista de (tipo_refactoring, target_class, params)
    
    def crossover_variable_length(self, other):
        """Crossover que preserva dependências entre refatorações"""
        # Identificar subsequências válidas
        valid_subseqs_self = self.find_independent_subsequences()
        valid_subseqs_other = other.find_independent_subsequences()
        
        # Combinar subsequências respeitando precedência
        child = RefactoringSequence()
        child.operations = self.merge_preserving_dependencies(
            random.choice(valid_subseqs_self),
            random.choice(valid_subseqs_other)
        )
        return child
    
    def mutate_structure(self):
        """Mutação que pode adicionar, remover ou modificar operações"""
        mutation_type = random.choice(['add', 'remove', 'modify'])
        
        if mutation_type == 'add' and len(self.operations) < MAX_SEQUENCE_LENGTH:
            insertion_point = random.randint(0, len(self.operations))
            new_operation = self.generate_compatible_operation(insertion_point)
            self.operations.insert(insertion_point, new_operation)
            
        elif mutation_type == 'remove' and len(self.operations) > 1:
            removal_point = random.randint(0, len(self.operations) - 1)
            removed = self.operations.pop(removal_point)
            # Verificar e reparar dependências quebradas
            self.repair_broken_dependencies(removed)
```

### 4.2. Funções de Fitness Avançadas

#### 4.2.1. Multi-Objective Fitness Design

**Desafio:** Balancear objetivos conflitantes sem introduzir bias.

```python
class SoftwareQualityFitness:
    def __init__(self, weights=None):
        self.weights = weights or {
            'maintainability': 0.3,
            'performance': 0.3,
            'security': 0.2,
            'testability': 0.2
        }
    
    def evaluate(self, software_design):
        objectives = {
            'maintainability': self.calculate_maintainability(software_design),
            'performance': self.estimate_performance(software_design),
            'security': self.assess_security_risks(software_design), 
            'testability': self.measure_testability(software_design)
        }
        
        # Abordagem 1: Weighted Sum (Single-objective)
        weighted_fitness = sum(
            self.weights[obj] * value 
            for obj, value in objectives.items()
        )
        
        # Abordagem 2: Pareto Ranking (Multi-objective)
        pareto_rank = self.calculate_pareto_rank(objectives)
        
        # Abordagem 3: Constraint-based (penalty)
        penalty = 0
        if objectives['security'] < MINIMUM_SECURITY_THRESHOLD:
            penalty += 1000 * (MINIMUM_SECURITY_THRESHOLD - objectives['security'])
            
        return {
            'weighted': weighted_fitness - penalty,
            'pareto_rank': pareto_rank,
            'objectives': objectives,
            'penalty': penalty
        }
```

#### 4.2.2. Dynamic and Adaptive Fitness

**Problema:** Como lidar com objetivos que mudam durante a evolução?

```python
class AdaptiveFitnessFunction:
    def __init__(self):
        self.evaluation_history = []
        self.diversity_pressure = 0.1
        self.difficulty_adjustment = 1.0
        
    def evaluate_with_context(self, solution, generation, population):
        # Fitness base
        base_fitness = self.base_evaluation(solution)
        
        # Pressure por diversidade (penalizar soluções muito similares)
        diversity_bonus = self.calculate_diversity_bonus(solution, population)
        
        # Adaptive difficulty (aumentar standards ao longo do tempo)
        adjusted_fitness = base_fitness * self.difficulty_adjustment
        
        # Novelty search component (recompensar soluções diferentes)
        novelty_score = self.calculate_novelty(solution, self.evaluation_history)
        
        final_fitness = (
            adjusted_fitness + 
            self.diversity_pressure * diversity_bonus +
            0.1 * novelty_score
        )
        
        # Update history e adaptive parameters
        self.evaluation_history.append(solution)
        if generation % 10 == 0:
            self.update_difficulty_adjustment(population)
            
        return final_fitness
    
    def update_difficulty_adjustment(self, population):
        """Aumenta difficulty se população está convergindo muito rápido"""
        avg_fitness = np.mean([ind.fitness for ind in population])
        fitness_std = np.std([ind.fitness for ind in population])
        
        if fitness_std < 0.05 * avg_fitness:  # Baixa diversidade
            self.difficulty_adjustment *= 1.1
        elif fitness_std > 0.2 * avg_fitness:  # Alta diversidade
            self.difficulty_adjustment *= 0.95
```

### 4.3. Hibridização e Técnicas Avançadas

#### 4.3.1. Memetic Algorithms: GA + Local Search

```python
class MemeticAlgorithm:
    def __init__(self, ga_params, local_search_params):
        self.genetic_algorithm = GeneticAlgorithm(**ga_params)
        self.local_search = LocalSearch(**local_search_params)
        self.local_search_frequency = 0.2  # 20% dos indivíduos
        
    def evolve_generation(self, population):
        # Fase 1: Evolução genética padrão
        new_population = self.genetic_algorithm.evolve_generation(population)
        
        # Fase 2: Busca local em indivíduos selecionados
        for individual in new_population:
            if random.random() < self.local_search_frequency:
                improved = self.local_search.improve(individual)
                if improved.fitness > individual.fitness:
                    individual = improved
                    
        return new_population
```

#### 4.3.2. Multi-Population e Island Models

```python
class IslandGeneticAlgorithm:
    def __init__(self, n_islands, migration_rate=0.05):
        self.islands = [GeneticAlgorithm() for _ in range(n_islands)]
        self.migration_rate = migration_rate
        self.migration_topology = 'ring'  # ring, star, fully_connected
        
    def run_evolution(self, generations):
        for generation in range(generations):
            # Evolve each island independently
            for island in self.islands:
                island.evolve_generation()
                
            # Migration every 10 generations
            if generation % 10 == 0:
                self.perform_migration()
                
    def perform_migration(self):
        """Exchange best individuals between islands"""
        if self.migration_topology == 'ring':
            for i in range(len(self.islands)):
                next_island = (i + 1) % len(self.islands)
                migrants = self.islands[i].select_migrants(
                    int(len(self.islands[i].population) * self.migration_rate)
                )
                self.islands[next_island].accept_migrants(migrants)
```

### 4.4. Análise de Performance e Debugging

#### 4.4.1. Métricas de Convergência

```python
def analyze_algorithm_performance(fitness_history):
    """Analisa características de convergência do algoritmo"""
    
    # 1. Convergence Speed
    target_fitness = max(fitness_history) * 0.95
    convergence_generation = next(
        (i for i, f in enumerate(fitness_history) if f >= target_fitness),
        len(fitness_history)
    )
    
    # 2. Diversity Loss Rate  
    diversity_over_time = [
        calculate_population_diversity(generation) 
        for generation in fitness_history
    ]
    diversity_slope = np.polyfit(range(len(diversity_over_time)), diversity_over_time, 1)[0]
    
    # 3. Exploration vs Exploitation Balance
    improvement_frequency = [
        1 if fitness_history[i] > fitness_history[i-1] else 0
        for i in range(1, len(fitness_history))
    ]
    exploration_ratio = np.mean(improvement_frequency)
    
    # 4. Premature Convergence Detection
    plateau_threshold = 50  # gerações sem melhoria significativa
    current_plateau = 0
    max_plateau = 0
    
    for i in range(1, len(fitness_history)):
        if abs(fitness_history[i] - fitness_history[i-1]) < 0.001:
            current_plateau += 1
            max_plateau = max(max_plateau, current_plateau)
        else:
            current_plateau = 0
    
    return {
        'convergence_speed': convergence_generation / len(fitness_history),
        'diversity_retention': abs(diversity_slope),
        'exploration_ratio': exploration_ratio,
        'max_plateau_length': max_plateau,
        'premature_convergence': max_plateau > plateau_threshold
    }
```

## Seção 5: Síntese e Próximos Passos

### 5.1. Resumo do Capítulo

- **Diferentes algoritmos servem diferentes necessidades**: Algoritmos Genéticos para problemas combinatoriais complexos, Simulated Annealing para escape de ótimos locais, PSO para espaços contínuos, e técnicas híbridas para maximizar pontos fortes
- **A representação determina o sucesso**: A escolha de como codificar soluções impacta diretamente a eficácia do algoritmo - representações bem projetadas facilitam a busca e respeitam constraints do domínio
- **Funções de fitness são arte e ciência**: Devem capturar objetivos reais, balancear trade-offs, evitar bias, e potencialmente adaptar-se durante a evolução para guiar efetivamente a busca
- **Hibridização multiplica capacidades**: Combinar diferentes técnicas (GA + busca local, multi-population, adaptive parameters) frequentemente supera abordagens "puras"
- **Análise e debugging são essenciais**: Métricas de convergência, diversidade e performance revelam comportamentos algoritmos e direcionam ajustes para problemas específicos

### 5.2. Ponte e Briefing para o Workshop Prático (`.ipynb`)

**Teaser para o Aluno:** Chegou a hora de colocar a teoria em prática! No laboratório, você implementará e comparará diferentes algoritmos de otimização resolvendo um problema real: **otimização automatizada da arquitetura de microsserviços**. Você verá como pequenas mudanças na representação ou função de fitness podem levar a soluções drasticamente diferentes, e experimentará firsthand o trade-off entre exploration e exploitation.

**Briefing para o Agente de Prática:**

O notebook deve implementar um **sistema completo de otimização de arquitetura de microsserviços** com as seguintes especificações técnicas:

1. **Problema-alvo:** Dado um conjunto de classes Java (representado como grafo de dependências), encontrar a melhor decomposição em microsserviços que maximize coesão interna e minimize acoplamento entre serviços

2. **Implementações obrigatórias:**
   - **Representação:** Classe `MicroserviceArchitecture` com encoding por assignment vector (cada gene = serviço da classe i)
   - **Função de fitness multi-objetivo:** Calcular coesão, acoplamento, e balanceamento de carga entre serviços
   - **Algoritmos:** Implementar do zero Genetic Algorithm, Simulated Annealing, e Hill Climbing
   - **Operadores especializados:** Crossover que preserva constraints de dependência, mutação com repair de soluções inválidas

3. **Estrutura do laboratório:**
   - **Parte 1:** Implementação da representação e função de fitness com dataset sintético  
   - **Parte 2:** Desenvolvimento dos 3 algoritmos de otimização step-by-step
   - **Parte 3:** Experimentos comparativos variando parâmetros (population size, mutation rate, temperature schedule)
   - **Parte 4:** Análise de convergência e visualização da evolução das soluções
   - **Parte 5:** Extensão com hibridização (Memetic Algorithm = GA + busca local)

4. **Dataset:** Criar um sistema exemplo com 15-20 classes Java e matriz de dependências conhecida, permitindo validação manual dos resultados

5. **Visualizações esperadas:** Gráficos de convergência, heatmaps de assignment matrix, network graphs da arquitetura resultante, e comparações side-by-side dos algoritmos

6. **Elementos pedagógicos:** Incluir células interativas para modificação de parâmetros, debugging step-by-step da função de fitness, e seções de análise crítica dos trade-offs observados

O foco deve ser na **experiência hands-on completa** - desde a implementação de representações até a interpretação de resultados - demonstrando como teoria de otimização resolve problemas práticos de arquitetura de software de forma automatizada e eficiente.