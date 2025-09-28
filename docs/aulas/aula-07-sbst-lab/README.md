---
titulo: "Aula 7: Laboratório de Teste Baseado em Busca (SBST)"
aula_numero: 7
carga_horaria: "4 horas"
foco_principal: "Implementar um gerador de testes automatizado com DEAP para maximizar a cobertura de ramos de uma função complexa."
metodologia: "Laboratório Prático Guiado"
tipo_aula: "Workshop Prático"
objetivos:
  - "Implementar um sistema de instrumentação de código para rastrear a cobertura de ramos."
  - "Configurar um Algoritmo Genético em DEAP onde a fitness é a cobertura de ramos."
  - "Analisar os resultados da busca para validar a eficácia na geração de casos de teste."
pre_requisitos:
  - "Conceitos de SBST (Aula 6)."
  - "Experiência com DEAP (Aula 4)."
---

# Aula 7: Laboratório de Teste Baseado em Busca (SBST)

## Seção 1: Abertura e Engajamento

### 1.1. Problema Motivador

Na aula anterior, discutimos a teoria por trás do Teste Baseado em Busca (SBST) e o desafio de testar funções complexas. Vimos como a cobertura de código, especialmente a de ramos, pode servir como uma excelente função de fitness para guiar um algoritmo de otimização. Agora, é hora de transformar essa teoria em um sistema funcional.

Vamos construir um "caçador de bugs" automatizado. Nosso objetivo é pegar uma função Python com múltiplos caminhos lógicos e, em vez de escrever testes manualmente, fazer com que um algoritmo genético descubra por si só os dados de entrada exatos necessários para exercitar cada `if` e `else` do código. Ao final, teremos um conjunto de testes gerado por IA que nos dará alta confiança sobre o comportamento da nossa função.

### 1.2. Objetivos deste Laboratório

Ao final deste workshop prático, você será capaz de:

*   **Instrumentar Código Python:** Criar um mecanismo para monitorar quais ramos de uma função são executados por um determinado caso de teste.
*   **Implementar um Gerador de Testes com DEAP:** Configurar um algoritmo genético completo onde os indivíduos são casos de teste e a função de fitness mede a cobertura de ramos.
*   **Analisar a Evolução da Cobertura:** Visualizar e interpretar como a busca evolutiva descobre progressivamente os testes necessários para atingir 100% de cobertura.

## Seção 2: Fundamentos Teóricos (Versão Expressa)

Vamos recapitular rapidamente os três pilares do SBST que implementaremos hoje:

1.  **Representação:**
    *   **O que é?** Um caso de teste para a nossa função-alvo.
    *   **Implementação:** Um indivíduo do DEAP será uma lista contendo os argumentos da função. Por exemplo, para `def func(x: int, y: str)`, o indivíduo será `[10, "teste"]`.

2.  **Função de Fitness:**
    *   **O que é?** Uma medida da qualidade de um caso de teste. Nosso objetivo é maximizar a cobertura de ramos.
    *   **Implementação:** A fitness de um indivíduo será o **número de ramos únicos** que ele consegue executar na função-alvo. Um indivíduo que executa um ramo que nenhum outro na população atual executou é altamente valioso.

3.  **Busca:**
    *   **O que é?** O motor que evolui a população de casos de teste.
    *   **Implementação:** Usaremos um algoritmo genético padrão do DEAP (`eaSimple`), com operadores de crossover e mutação que combinam e modificam os dados de entrada para criar novos casos de teste.

O grande desafio técnico é: como saber quais ramos foram executados? Faremos isso através da **instrumentação de código**, um processo onde injetamos "sondas" no código-fonte para nos reportar seu comportamento durante a execução.

## Seção 3: Laboratório Prático Guiado (Google Colab)

### 3.1. Roteiro do Notebook: `workshop.ipynb`

Neste laboratório, vamos construir passo a passo um gerador de testes para uma função chamada `classificador_triangulo_complexo`. Esta função contém vários caminhos lógicos, incluindo casos de borda e condições específicas que são difíceis de encontrar com testes aleatórios. Nosso AG terá a tarefa de descobrir os trios de valores `(a, b, c)` que cobrem todos esses caminhos.

### 3.2. Estrutura do Laboratório

O notebook está dividido em quatro partes principais:

*   **Parte 1: A Função-Alvo e o Desafio da Cobertura:**
    *   Apresentaremos a função `classificador_triangulo_complexo` e seus ramos lógicos.
    *   Mostraremos como uma abordagem de teste aleatório falha em atingir 100% de cobertura de ramos de forma eficiente.

*   **Parte 2: Instrumentação para Rastrear Cobertura:**
    *   Implementaremos uma classe `CoverageInstrumenter` que usa o módulo `sys.settrace` do Python. Esta classe funcionará como uma "sonda" que observa a execução da função-alvo linha por linha e registra quais ramos (`if/else`) foram ativados.

*   **Parte 3: Configurando o Algoritmo Genético com DEAP:**
    *   Definiremos a estrutura do nosso problema no DEAP:
        *   **Indivíduo:** Uma lista de 3 inteiros representando os lados `(a, b, c)` de um triângulo.
        *   **Função de Fitness:** Nossa função `evaluate` que usará o `CoverageInstrumenter` para calcular quantos ramos um indivíduo cobre. A fitness será a contagem de ramos.
        *   **Operadores:** Registraremos na `toolbox` os operadores de geração de indivíduos, crossover, mutação e seleção.

*   **Parte 4: Execução, Análise e Caça aos Bugs:**
    *   Executaremos o algoritmo genético e acompanharemos a evolução da cobertura.
    *   Analisaremos o conjunto final de testes gerado, verificando se ele atinge 100% de cobertura.
    *   Visualizaremos a progressão da cobertura máxima e média da população ao longo das gerações.

## Seção 4: Análise e Discussão dos Resultados

### 4.1. Interpretando os Resultados

O resultado final do nosso notebook será um conjunto de casos de teste e um gráfico de convergência.

*   **O Conjunto de Testes:** Cada indivíduo no conjunto final representa um caso de teste valioso. Por exemplo, o AG pode ter gerado `[10, 10, 20]`, descobrindo o caso de borda onde a desigualdade triangular falha (`a + b = c`). Ele também encontrará trios para "equilátero", "isósceles", "escaleno" e "inválido".
*   **O Gráfico de Convergência:** O gráfico mostrará a cobertura de ramos aumentando a cada geração. É esperado um rápido aumento no início, conforme os casos de teste fáceis são encontrados, seguido por um platô e, em seguida, saltos pontuais, quando a mutação finalmente descobre um caso de teste para um ramo particularmente difícil.

### 4.2. O "Porquê" das Decisões

*   **Por que `sys.settrace`?** Usamos `sys.settrace` porque é uma ferramenta nativa do Python para depuração e profiling, permitindo-nos inspecionar a execução do código sem modificar o código-fonte original da função-alvo. Isso torna nossa abordagem de instrumentação limpa e não invasiva.
*   **Por que a Fitness é a Contagem de Ramos?** Essa é a forma mais simples e direta de guiar a busca. Cada novo ramo coberto é uma "vitória" que aproxima o algoritmo do objetivo final. Em sistemas mais avançados, a fitness poderia ser mais granular, medindo o quão "perto" um caso de teste esteve de virar a condição de um ramo (como vimos na teoria da Aula 6).
*   **Por que não usar uma biblioteca de cobertura como a `coverage.py`?** Embora ferramentas profissionais existam, construir nosso próprio instrumentador do zero é um exercício pedagógico crucial. Ele nos força a entender *como* a cobertura é medida e nos dá controle total sobre a função de fitness, que é o coração do SBST.

## Seção 5: Síntese e Próximos Passos

### 5.1. Resumo do Laboratório

*   Implementamos um sistema de Teste Baseado em Busca (SBST) do início ao fim usando Python e DEAP.
*   A **instrumentação de código** (com `sys.settrace`) é a técnica chave que nos permite observar o comportamento interno de um programa e usá-lo como feedback.
*   A **cobertura de ramos** provou ser uma função de fitness eficaz, guiando o algoritmo genético para descobrir casos de teste que um humano ou uma busca aleatória poderiam facilmente ignorar.
*   SBST automatiza a tarefa tediosa e propensa a erros de criar testes para lógicas complexas, aumentando a qualidade e a robustez do software.

### 5.2. Preparação para o Próximo Bloco

Até agora, aplicamos SBST para garantir que o código se comporte como esperado. Mas e se o próprio código estiver mal estruturado? Na próxima aula, **Aula 8: Refatoração Baseada em Busca**, vamos mudar nosso foco da *verificação* para a *melhoria*. Usaremos SBST não para encontrar bugs, mas para combater a **dívida técnica**, otimizando a estrutura do código para torná-lo mais manutenível, coeso e menos acoplado. As habilidades de formulação de problemas que você praticou hoje serão diretamente aplicáveis.