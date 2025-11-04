---
titulo: "Aula 9: Teste de Justiça em IA - Caçando Vieses com SBSE"
aula_numero: 9
carga_horaria: "4 horas"
foco_principal: "Aplicar SBSE para descobrir automaticamente vieses e discriminação em modelos de Machine Learning, usando algoritmos de busca para gerar casos de teste que maximizem a detecção de comportamentos injustos."
metodologia: "Exposição Teórica e Laboratório Prático"
tipo_aula: "Workshop Prático"
objetivos:
  - "Compreender os desafios únicos de testar sistemas baseados em IA, especialmente o problema do oráculo e não-determinismo."
  - "Formular o problema de detecção de viés como um problema de busca com representação e função de fitness adequadas."
  - "Implementar um sistema de fairness testing usando algoritmos genéticos para encontrar casos de discriminação em modelos pré-treinados."
pre_requisitos:
  - "Conceitos de SBSE e Algoritmos Genéticos (Módulos 1-3)."
  - "Knowledge básico de Machine Learning (modelos supervisionados, métricas de avaliação)."
  - "Experiência com bibliotecas DEAP e scikit-learn."
---

# Aula 9: Teste de Justiça em IA - Caçando Vieses com SBSE

## Seção 1: Abertura e Engajamento

### 1.1. Problema Motivador

Em 2018, a Amazon descobriu que seu sistema de IA para triagem de currículos estava sistematicamente discriminando candidatas mulheres. O algoritmo, treinado em dados históricos de contratação (onde homens eram majoritariamente contratados em áreas técnicas), aprendeu que ser mulher era um "sinal negativo" e penalizava currículos que continham palavras como "capitã do time feminino de xadrez" ou que vinham de universidades exclusivamente femininas.

Este não é um caso isolado. Modelos de aprovação de crédito discriminam contra minorias étnicas, sistemas de reconhecimento facial falham drasticamente para pessoas de pele escura, e algoritmos de recomendação de vagas perpetuam segregação ocupacional. O problema é insidioso: esses vieses são difíceis de detectar porque estão enterrados nas estatísticas complexas de modelos com milhões de parâmetros.

Como podemos testar sistematicamente se um modelo de IA é justo? Como encontrar os casos específicos onde ele discrimina? Testes manuais são impraticáveis – há infinitas combinações de atributos para testar. É aqui que SBSE brilha: podemos usar algoritmos de busca para automaticamente "provocar" um modelo de IA até ele revelar seus vieses ocultos.

### 1.2. Objetivos deste Capítulo

Ao final deste capítulo, você será capaz de:

*   **Adaptar SBSE para IA:** Compreender os desafios únicos de testar sistemas baseados em aprendizado de máquina, incluindo não-determinismo e ausência de oráculos claros.
*   **Detectar Viés Automaticamente:** Formular a detecção de discriminação como um problema de busca, definindo representações e funções de fitness que maximizem a descoberta de comportamentos injustos.
*   **Implementar Fairness Testing:** Construir um sistema completo que usa algoritmos genéticos para gerar casos de teste sintéticos que expõem vieses em modelos pré-treinados.

## Seção 2: Fundamentos Teóricos (Versão Expressa)

O teste de justiça (fairness testing) em IA representa um novo paradigma de teste de software. Diferente do código tradicional, onde sabemos exatamente o que uma função deveria retornar, modelos de IA são "caixas pretas" probabilísticas cujo comportamento correto é definido por princípios éticos, não especificações técnicas.

### O Tripé do Fairness Testing com SBSE

1.  **Representação (O Perfil Individual):** O que é um "caso de teste" para um modelo de IA?
    *   **O que é?** Um caso de teste é um perfil individual sintético – um conjunto de atributos que seria submetido ao modelo.
    *   **Exemplo:** Para um modelo de aprovação de crédito, um indivíduo poderia ser representado como `[idade: 35, salario: 50000, genero: 'F', etnia: 'negra', score_credito: 720]`.

2.  **Função de Fitness (A Detector de Discriminação):** Como medimos se um caso de teste "expõe viés"?
    *   **O que é?** A fitness mede o grau de discriminação que um par de casos de teste revela. Geralmente comparamos dois indivíduos que diferem apenas em um atributo sensível (gênero, etnia, idade).
    *   **Técnica Comum:** **Individual Fairness** – Indivíduos similares devem receber tratamento similar. A fitness é a diferença de probabilidade de aprovação entre dois perfis quase idênticos.

3.  **Busca (O Explorador de Vieses):** Como encontramos os casos mais discriminatórios?
    *   **O que é?** Um algoritmo genético que evolui pares de perfis para maximizar a diferença de tratamento entre eles.
    *   **Insight:** O AG não procura por um resultado "correto", mas pelo caso que mais evidencia inconsistência no modelo.

### Tipos de Fairness e Como Testá-los

```{mermaid}
graph TD
    A[Fairness Testing] --> B[Individual Fairness];
    A --> C[Group Fairness];
    A --> D[Causal Fairness];
    
    B --> B1["Indivíduos similares → tratamento similar"];
    B --> B2["Fitness: diferença entre casos quase idênticos"];
    
    C --> C1["Grupos protegidos → taxas similares"];
    C --> C2["Fitness: diferença de aprovação entre grupos"];
    
    D --> D1["Atributo sensível não deve causar discriminação"];
    D --> D2["Fitness: impacto de mudança de um atributo"];
```

## Seção 3: Exemplo Ilustrativo

Vamos considerar um modelo simples de aprovação de empréstimo e ver como detectar viés de gênero.

**Cenário:** Um banco treinou um modelo que aprova/rejeita empréstimos baseado em `[idade, salário, score_crédito, gênero]`. Suspeitamos que ele discrimina contra mulheres.

**Representação SBSE:**
```python
# Individual = [idade, salario, score_credito, genero]  
# Exemplo: [35, 50000, 720, 'M']
```

**Função de Fitness:**
```python
def fitness_gender_bias(individual):
    # Criar dois perfis idênticos, diferindo apenas no gênero
    profile_male = individual.copy()
    profile_male[3] = 'M'  # Gênero masculino
    
    profile_female = individual.copy()  
    profile_female[3] = 'F'  # Gênero feminino
    
    # Obter probabilidades de aprovação do modelo
    prob_male = model.predict_proba([profile_male])[0][1]
    prob_female = model.predict_proba([profile_female])[0][1]
    
    # Fitness = diferença de probabilidade (queremos maximizar)
    return abs(prob_male - prob_female)
```

**Resultado Esperado:** O AG evoluirá perfis que maximizam essa diferença. Se o modelo for enviesado, encontrará casos como `[45, 75000, 800, _]` onde a probabilidade de aprovação para homens é 90% e para mulheres é 60% – evidência clara de discriminação.

## Seção 4: Análise e Tópicos Avançados

### O Desafio do "Oráculo de Fairness"

Diferente de testes tradicionais, fairness testing não tem um oráculo claro. Não existe uma resposta "correta" para "este perfil deveria ser aprovado?". O que temos são princípios éticos:

*   **Consistência:** Casos similares devem ter resultados similares.
*   **Não-discriminação:** Atributos sensíveis não devem influenciar decisões.
*   **Proporcionalidade:** A representação de grupos deve ser preservada.

Isso torna o SBSE ideal: não precisamos saber a resposta certa, apenas encontrar os casos mais "suspeitos".

### Fairness vs. Accuracy: O Dilema Fundamental

Existe um trade-off inerente entre justiça e acurácia. Um modelo perfeitamente justo (que ignora completamente gênero e etnia) pode ter performance inferior a um modelo que usa essas informações de forma estatisticamente válida. SBSE pode nos ajudar a navegar esse trade-off, encontrando soluções Pareto-ótimas que balanceiam os dois objetivos.

### Limitações e Armadilhas

*   **Proxies e Correlações:** Mesmo removendo atributos sensíveis, o modelo pode usar proxies (ex: CEP como indicador de etnia). SBSE pode descobrir essas correlações indiretas.
*   **Fairness Washing:** Organizações podem "otimizar para as métricas" sem resolver problemas fundamentais. É crucial testar além das métricas oficiais.
*   **Contexto Cultural:** Definições de "justiça" variam entre culturas e contextos. O que é justo em um país pode não ser em outro.

## Seção 5: Síntese e Próximos Passos

### 5.1. Resumo do Capítulo

*   **Novo Paradigma:** Fairness testing em IA representa uma evolução do teste de software tradicional, focando em princípios éticos ao invés de especificações técnicas.
*   **SBSE como Ferramenta:** Algoritmos de busca são ideais para detectar viés porque podem explorar sistematicamente o espaço de casos de teste, encontrando os exemplos mais discriminatórios.
*   **Representação e Fitness:** O sucesso do fairness testing depende de modelar adequadamente os perfis individuais e definir métricas que capturem diferentes tipos de discriminação.
*   **Complexidade Ética:** Fairness não é binária – existe um espectro de trade-offs entre justiça e performance que devem ser navegados conscientemente.

### 5.2. Ponte e Briefing para o Workshop Prático (`.ipynb`)

**Teaser para o Aluno:** Teoria é importante, mas agora você vai colocar a mão na massa! No laboratório prático, você receberá um modelo de aprovação de crédito "contaminado" com viés de gênero. Sua missão será construir um detector de discriminação automatizado usando DEAP. Você verá como pequenas variações nos atributos podem revelar padrões preocupantes de discriminação que passariam despercebidos em testes manuais.

**Briefing para o Agente de Prática (Geração do `workshop.ipynb`):**

O notebook deve implementar um sistema completo de **fairness testing usando SBSE** com as seguintes especificações técnicas:

1.  **Modelo-Alvo:** Crie um modelo de classificação pré-treinado (usando scikit-learn) que simula aprovação de crédito. O modelo deve ser intencionalmente enviesado contra um grupo protegido (ex: mulheres ou uma etnia específica). Use um dataset sintético com atributos como `[idade, salario, score_credito, anos_experiencia, genero, etnia]`.

2.  **Representação SBSE:**
    *   Use o `creator` do DEAP para definir um `Individual` que representa um perfil de solicitante.
    *   Cada gene do cromossomo corresponde a um atributo (alguns numéricos, outros categóricos).
    *   Implemente geradores adequados para cada tipo de atributo (ex: `randint` para idade, `choice` para gênero).

3.  **Função de Fitness:**
    *   Implemente múltiplas funções de fitness para detectar diferentes tipos de viés:
        *   **Individual Fairness:** Compara pares de perfis que diferem apenas no atributo sensível.
        *   **Group Fairness:** Mede disparidade nas taxas de aprovação entre grupos.
    *   A fitness deve retornar a magnitude da discriminação detectada (maior = mais discriminatório).

4.  **Estrutura com DEAP:**
    *   Configure a `toolbox` com operadores adequados para dados mistos (numéricos + categóricos).
    *   Use operadores de crossover e mutação que preservem a validade dos perfis gerados.
    *   Execute o algoritmo `eaSimple` para evoluir casos de teste discriminatórios.

5.  **Análise e Visualização:**
    *   Apresente os casos de teste mais discriminatórios encontrados pelo AG.
    *   Compare os resultados com uma busca aleatória para demonstrar a eficácia do SBSE.
    *   Crie visualizações que mostrem as diferenças de probabilidade entre grupos.
    *   Calcule métricas de fairness padrão (Equalized Odds, Demographic Parity) nos casos encontrados.

6.  **Discussão Ética:**
    *   Inclua uma seção final que discuta os achados e suas implicações.
    *   Analise se os vieses encontrados são justificáveis ou problemáticos.
    *   Proponha estratégias de mitigação baseadas nos resultados.