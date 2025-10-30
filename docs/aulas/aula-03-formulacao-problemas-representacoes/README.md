---
title: 'Aula 3: A Arte de Formular Problemas em SBSE'
description: 'Aprenda a traduzir problemas complexos de engenharia de software em representações otimizáveis e a projetar funções de fitness eficazes.'
author: 'GitHub Copilot'
date: '2025-09-28'
tags:
  - SBSE
  - Otimização
  - Representação
  - Função de Fitness
  - Formulação de Problemas
---

# Aula 3: A Arte de Formular Problemas em SBSE

## Seção 1: Abertura e Engajamento

### 1.1. Problema Motivador

Imagine que você é o líder técnico de um grande projeto de e-commerce. A equipe de produto chega com uma lista de 20 novas *features* que gostariam de implementar no próximo trimestre. O orçamento, no entanto, só permite o desenvolvimento de uma fração delas. Cada *feature* tem um valor de negócio estimado (quanto dinheiro ela pode gerar), um custo de implementação (horas de desenvolvimento) e algumas dependem de outras para funcionar.

Como você escolheria o subconjunto de *features* que maximiza o valor de negócio sem estourar o orçamento e respeitando as dependências? Uma escolha manual é complexa, demorada e provavelmente sub-ótima. E se, em vez de escolher, pudéssemos "pedir" a um computador para encontrar a combinação perfeita para nós? É exatamente essa a ponte que a formulação de problemas em SBSE nos permite construir.

### 1.2. Objetivos deste Capítulo

Ao final desta aula, você será capaz de:

1.  **Traduzir um problema de engenharia de software** em seus componentes fundamentais de SBSE: representação e função de fitness.
2.  **Selecionar a representação de solução adequada** (binária, permutação ou numérica) para diferentes tipos de problemas.
3.  **Projetar uma função de fitness** que guie a busca, incorporando objetivos de negócio e restrições técnicas através de funções de penalidade.

## Seção 2: Fundamentos Teóricos

Na aula anterior, vimos o "o quê" e o "porquê" da SBSE. Agora, vamos mergulhar no "como". A mágica de transformar um problema de software em um problema de busca solucionável por um computador reside em duas etapas críticas: **Representação** e **Função de Fitness**.

### 2.1. A Arte da Representação: Ensinando o Computador a "Ver" Soluções

A representação (ou codificação) é a maneira como traduzimos uma solução candidata do mundo real para uma estrutura de dados que um algoritmo de busca possa manipular. A escolha da representação é talvez a decisão mais importante no design de uma solução SBSE.

```{mermaid}
graph TD
    subgraph Problema do Mundo Real
        A["Quais features implementar?"]
        B["Qual a melhor ordem de testes?"]
        C["Quais os melhores parâmetros?"]
    end

    subgraph Representação Computacional
        D["[1, 0, 1, 1, 0, ...] (Binária)"]
        E["[T3, T1, T5, T2, T4] (Permutação)"]
        F["[0.01, 256, 0.9] (Numérica)"]
    end

    A --> D
    B --> E
    C --> F
```

Existem três tipos principais de representação:

1.  **Representação Binária:**
    *   **O quê:** Um vetor de 0s e 1s.
    *   **Quando usar:** Para problemas de **seleção** ou **inclusão/exclusão**. Cada posição no vetor corresponde a um item, e o valor (1 ou 0) indica se ele está presente na solução.
    *   **Exemplo Prático:** O problema das *features* do nosso e-commerce. Um vetor de 20 posições, onde `[1, 0, ..., 1]` significa "implementar a primeira e a última feature, mas não a segunda".

2.  **Representação por Permutação:**
    *   **O quê:** Uma lista ordenada de itens, onde cada item aparece exatamente uma vez.
    *   **Quando usar:** Para problemas de **ordenação** ou **sequenciamento**.
    *   **Exemplo Prático:** Otimizar a ordem de execução de uma suíte de testes de regressão para encontrar falhas o mais rápido possível. A solução `[T3, T1, T5, ...]` define a sequência exata em que os testes serão executados.

3.  **Representação Numérica (Inteira ou Real):**
    *   **O quê:** Um vetor de números inteiros ou de ponto flutuante.
    *   **Quando usar:** Para problemas de **configuração** ou **ajuste de parâmetros**.
    *   **Exemplo Prático:** Encontrar os hiperparâmetros ótimos para um modelo de Machine Learning. A solução `[0.001, 512, 0.5]` poderia representar a taxa de aprendizado, o tamanho do batch e a taxa de dropout.

### 2.2. Projetando a Função de Fitness: A Bússola da Otimização

Se a representação é o mapa, a função de fitness (ou função de avaliação/objetivo) é a bússola. Ela recebe uma solução candidata (na sua forma representada) e retorna um valor numérico que quantifica sua "qualidade". O objetivo do algoritmo de busca é encontrar a solução que **maximiza** (ou minimiza) este valor.

Uma boa função de fitness deve ser:
*   **Precisa:** Refletir o verdadeiro objetivo do problema.
*   **Eficiente:** Ser rápida de calcular, pois será executada milhares ou milhões de vezes.

#### Lidando com Restrições: A Abordagem da Função de Penalidade

Raramente os problemas do mundo real são irrestritos. No nosso exemplo das *features*, temos uma restrição de orçamento. Como ensinamos isso ao algoritmo?

A técnica mais comum é a **função de penalidade**. Modificamos a função de fitness para "punir" soluções que violam as restrições.

**Exemplo (Pseudocódigo):**

```
função calcular_fitness(solucao):
    valor_total = calcular_valor_das_features(solucao)
    custo_total = calcular_custo_das_features(solucao)
    
    penalidade = 0
    if custo_total > ORCAMENTO_MAXIMO:
        excesso = custo_total - ORCAMENTO_MAXIMO
        penalidade = excesso * FATOR_DE_PENALIDADE  // Penalidade proporcional ao excesso
        
    return valor_total - penalidade
```

Uma solução que estoura o orçamento terá seu fitness drasticamente reduzido, tornando-a menos atraente para o algoritmo de busca.

#### Múltiplos Objetivos: A Abordagem da Soma Ponderada

E se quisermos maximizar o valor de negócio E minimizar o risco técnico ao mesmo tempo? Quando temos múltiplos objetivos, uma abordagem inicial (e mais simples) é a **soma ponderada**.

Convertemos múltiplos objetivos em um único valor de fitness, atribuindo um "peso" a cada um.

**Exemplo (Pseudocódigo):**

```
função calcular_fitness_multiobjetivo(solucao):
    valor_negocio = calcular_valor(solucao)      // Objetivo 1: Maximizar
    risco_tecnico = calcular_risco(solucao)      // Objetivo 2: Minimizar
    
    // Normalizar valores para a mesma escala (ex: 0 a 1)
    valor_normalizado = normalizar(valor_negocio)
    risco_normalizado = normalizar(risco_tecnico)
    
    peso_valor = 0.7
    peso_risco = 0.3
    
    fitness_final = (valor_normalizado * peso_valor) - (risco_normalizado * peso_risco)
    
    return fitness_final
```
**Atenção:** A soma ponderada é uma simplificação. A escolha dos pesos é subjetiva e nem sempre captura o *trade-off* real entre os objetivos. Na Aula 13, veremos uma abordagem muito mais poderosa: a otimização multi-objetivo real.

## Seção 3: Exemplo Ilustrativo

Vamos solidificar os conceitos com o problema das *features* do e-commerce.

**Problema:** Escolher um subconjunto de 4 features para maximizar o valor, respeitando um orçamento de 25 "pontos" de custo.

| Feature | Valor (k R$) | Custo (pontos) |
| :--- | :--- | :--- |
| F1: Login Social | 15 | 10 |
| F2: Lista de Desejos | 20 | 8 |
| F3: Pagamento Rápido | 25 | 15 |
| F4: Recomendações | 30 | 20 |

1.  **Representação:** Binária, com um vetor de 4 posições. `[1, 1, 0, 0]` significa "implementar F1 e F2".

2.  **Função de Fitness (com penalidade):**
    ```python
    def calcular_fitness(solucao):
        features = [(15, 10), (20, 8), (25, 15), (30, 20)]
        orcamento_max = 25
        
        valor_total = sum(solucao[i] * features[i][0] for i in range(4))
        custo_total = sum(solucao[i] * features[i][1] for i in range(4))
        
        if custo_total > orcamento_max:
            return 0 # Penalidade severa: fitness zero se estourar o orçamento
        
        return valor_total
    ```

3.  **Avaliando Soluções Candidatas:**
    *   **Solução A: `[1, 1, 0, 0]`**
        *   Custo: 10 + 8 = 18 (<= 25, Válida)
        *   Valor: 15 + 20 = 35
        *   **Fitness = 35**
    *   **Solução B: `[0, 0, 1, 1]`**
        *   Custo: 15 + 20 = 35 (> 25, Inválida)
        *   **Fitness = 0**
    *   **Solução C: `[0, 1, 1, 0]`**
        *   Custo: 8 + 15 = 23 (<= 25, Válida)
        *   Valor: 20 + 25 = 45
        *   **Fitness = 45** (Melhor que a Solução A)

O algoritmo de busca usaria essa função de fitness para navegar pelo espaço de 2⁴ = 16 soluções possíveis e convergir para a solução C (ou outra com fitness igual ou maior).

## Seção 4: Análise e Discussão dos Resultados

A formulação do problema é um ato de modelagem e, como toda modelagem, envolve simplificações.

*   **O "Porquê" da Penalidade Severa:** No nosso exemplo, usamos `return 0` para qualquer solução inválida. Por que não uma penalidade mais branda? Uma penalidade severa força a busca a permanecer **exclusivamente** no espaço de soluções viáveis. Uma penalidade mais branda poderia permitir que a busca explorasse temporariamente soluções inviáveis na esperança de que seus "filhos" (no AG) se tornem viáveis e bons. A escolha depende do problema: se o espaço viável é muito pequeno ou difícil de encontrar, uma penalidade branda pode ser melhor.

*   **O Risco da Soma Ponderada:** Imagine que `valor_negocio` varia de 1.000 a 100.000 e `risco_tecnico` de 1 a 10. Sem **normalização**, o `valor_negocio` dominaria completamente a função de fitness, tornando o `risco_tecnico` irrelevante, independentemente dos pesos. A normalização (colocar todos os objetivos na mesma escala, como [0, 1]) é crucial.

*   **Representação e Operadores de Busca:** A escolha da representação impacta diretamente os operadores de busca (crossover, mutação) que podemos usar. Uma mutação para uma representação binária pode ser simplesmente inverter um bit (`0 -> 1`). Para uma permutação, uma mutação poderia ser trocar a posição de dois itens. Usar operadores inadequados para a representação pode gerar soluções inválidas constantemente, tornando a busca ineficiente.

## Seção 5: Síntese e Próximos Passos

### 5.1. Resumo do Capítulo

*   Formular um problema de SBSE consiste em definir uma **representação** para as soluções e uma **função de fitness** para avaliá-las.
*   A **representação binária** é ideal para problemas de seleção, a de **permutação** para ordenação e a **numérica** para configuração.
*   A **função de fitness** é a bússola da busca; ela deve ser rápida e refletir o objetivo real do problema.
*   **Funções de penalidade** são usadas para guiar a busca para longe de soluções que violam restrições importantes (como orçamento ou dependências).
*   A **soma ponderada** é uma técnica simples para combinar múltiplos objetivos em um único valor de fitness, mas requer cuidado com a normalização e a escolha dos pesos.

### 5.2. Preparação para o Próximo Bloco

Agora que sabemos como *formular* um problema, precisamos de uma ferramenta poderosa para *resolvê-lo*. Na próxima aula, sairemos da teoria e entraremos na prática com a **DEAP (Distributed Evolutionary Algorithms in Python)**, uma biblioteca padrão da indústria para computação evolutiva. Reimplementaremos o "Problema da Mochila" (análogo ao nosso problema de features) usando DEAP, aprendendo como sua estrutura nos permite focar na formulação do problema enquanto a biblioteca cuida dos detalhes do algoritmo genético.
