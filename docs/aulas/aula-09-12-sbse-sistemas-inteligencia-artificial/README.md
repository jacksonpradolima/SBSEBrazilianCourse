---
title: "SBSE para Sistemas de Inteligência Artificial"
number: "09-12"
type: "Workshop Prático"
duration: "8 horas-aula"
objectives:
  - "Utilizar SBSE para realizar testes de justiça (fairness) em modelos de ML, buscando por vieses"
  - "Aplicar meta-heurísticas para otimização de hiperparâmetros"
  - "Modelar o problema de otimização de prompts como um problema de busca"
  - "Apresentar e detalhar a especificação do Projeto Final"
methodology: "Laboratório prático com foco em sistemas de IA e preparação para projeto final"
tools: ["Python 3.10+", "Scikit-learn", "Pandas", "DEAP", "Pymoo", "OpenAI API", "Transformers", "Fairlearn"]
prerequisites: ["Machine Learning básico", "DEAP avançado", "Conceitos de viés em IA"]
keywords: ["Fairness testing", "Viés em IA", "Otimização de hiperparâmetros", "Prompt engineering", "ML testing"]
author: "Curso SBSE na Era da IA"
date: "2025"
language: "pt-BR"
---

# SBSE para Sistemas de Inteligência Artificial

## Seção 1: Abertura e Engajamento

### 1.1. Problema Motivador

Em 2018, a Amazon descobriu que seu sistema de IA para recrutamento estava discriminando candidatas mulheres, penalizando currículos que continham palavras como "women's" (como em "women's chess club captain"). O modelo havia aprendido com dados históricos de contratação que refletiam vieses de décadas passadas. Como poderíamos ter detectado esse problema antes do sistema entrar em produção? Como testar sistematicamente se um modelo de IA é justo?

Paralelamente, considere o desafio de otimizar um modelo de deep learning: uma rede neural pode ter milhões de parâmetros treináveis e dezenas de hiperparâmetros (learning rate, batch size, arquitetura, etc.). O espaço de configurações possíveis é literalmente infinito. Grid Search testaria algumas centenas de combinações; Random Search, alguns milhares. Mas será que conseguimos fazer melhor? Será que algoritmos de busca inteligente podem navegar esse espaço de forma mais eficiente?

Este módulo explora a **fronteira da pesquisa em SBSE**: aplicar técnicas de otimização aos desafios únicos dos sistemas de Inteligência Artificial. Diferente do software tradicional, sistemas de IA aprendem com dados, são não-determinísticos, e podem perpetuar vieses sociais de formas sutis e perigosas.

### 1.2. Objetivos deste Laboratório/Capítulo

Ao final deste módulo, você será capaz de:

1. **Detectar vieses em modelos de IA**: Implementar sistema de teste automatizado que usa algoritmos genéticos para encontrar cenários onde modelos discriminam indevidamente com base em atributos sensíveis como gênero, raça ou idade.

2. **Otimizar hiperparâmetros inteligentemente**: Aplicar meta-heurísticas para encontrar configurações ótimas de modelos ML, superando Grid Search e Random Search em eficiência e qualidade dos resultados.

3. **Automatizar engenharia de prompts**: Modelar otimização de prompts como problema de busca, desenvolvendo sistema que melhora automaticamente templates de prompts para maximizar qualidade das respostas de LLMs.

## Seção 2: Fundamentos Teóricos

### 2.1. O Novo Paradigma: Testando Sistemas que Aprendem

**Desafios Únicos dos Sistemas de IA**

Sistemas de IA introduzem complexidades ausentes no software tradicional:

1. **Não-determinismo**: O mesmo input pode produzir outputs diferentes
2. **Dependência de dados**: Qualidade e vieses dos dados de treino afetam diretamente o comportamento
3. **Opacidade**: Modelos complexos (deep learning) são "caixas-pretas" 
4. **Aprendizado contínuo**: Comportamento evolui com novos dados
5. **Impacto social**: Decisões automatizadas podem afetar vidas humanas

**O Problema do Oráculo em IA**

No software tradicional, podemos definir outputs corretos para inputs conhecidos. Em IA:
- Não existe "resposta certa" única para muitos problemas
- Avaliação depende de métricas estatísticas e julgamento humano
- Critérios como "fairness" são socialmente construídos, não técnicos

### 2.2. Fairness Testing: Detectando Discriminação Automaticamente

**Definições de Fairness**

1. **Demographic Parity (Paridade Demográfica)**
   - Todos os grupos têm a mesma taxa de predições positivas
   - $P(\hat{Y} = 1 | A = 0) = P(\hat{Y} = 1 | A = 1)$
   - Onde $A$ é atributo sensível (ex: gênero)

2. **Equalized Odds (Odds Equalizadas)**
   - Taxa de verdadeiros positivos igual para todos os grupos
   - $P(\hat{Y} = 1 | Y = 1, A = 0) = P(\hat{Y} = 1 | Y = 1, A = 1)$

3. **Individual Fairness (Fairness Individual)**
   - Indivíduos similares recebem predições similares
   - Mais complexa de operacionalizar

**SBSE para Fairness Testing**

**Representação**: Um indivíduo no AG representa um perfil de entrada para o modelo
```python
# Exemplo para modelo de aprovação de crédito
individuo = {
    'idade': 35,
    'salario': 50000,
    'genero': 'F',  # Atributo sensível
    'educacao': 'superior',
    'tempo_emprego': 5
}
```

**Função de Fitness**: Maximizar diferença de tratamento
```python
def fitness_fairness(individuo_base):
    # Criar versão alternativa mudando apenas atributo sensível
    individuo_alt = individuo_base.copy()
    individuo_alt['genero'] = 'M' if individuo_base['genero'] == 'F' else 'F'
    
    # Obter predições do modelo
    pred_base = modelo.predict([individuo_base])[0]
    pred_alt = modelo.predict([individuo_alt])[0]
    
    # Maximizar diferença (encontrar maior discriminação)
    return abs(pred_base - pred_alt)
```

**Algoritmo Completo**:
```python
def encontrar_casos_discriminacao(modelo, atributo_sensivel):
    # População inicial: perfis diversos
    populacao = gerar_perfis_diversos()
    
    for geracao in range(MAX_GERACOES):
        # Avaliar cada perfil
        for individuo in populacao:
            individuo.fitness = fitness_fairness(individuo)
        
        # Evoluir para encontrar casos de maior discriminação
        populacao = aplicar_operadores_geneticos(populacao)
    
    # Retornar casos mais problemáticos
    return sorted(populacao, key=lambda x: x.fitness, reverse=True)[:10]
```

### 2.3. Otimização de Hiperparâmetros com SBSE

**Limitações das Abordagens Tradicionais**

1. **Grid Search**: 
   - Explora apenas combinações pré-definidas
   - Crescimento exponencial com número de parâmetros
   - Não considera interações entre parâmetros

2. **Random Search**:
   - Mais eficiente que Grid Search para espaços grandes
   - Mas ainda é "cega" - não aprende com tentativas anteriores

**SBSE para Hiperparâmetros**

**Representação Mista**: Diferentes tipos de parâmetros
```python
# Representação para rede neural
cromossomo = {
    'learning_rate': 0.001,      # Float contínuo
    'batch_size': 64,            # Inteiro discreto  
    'num_layers': 3,             # Inteiro discreto
    'activation': 'relu',        # Categórico
    'dropout_rate': 0.2          # Float contínuo
}
```

**Função de Fitness**: Performance no conjunto de validação
```python
def fitness_hiperparametros(cromossomo):
    # Construir modelo com hiperparâmetros do cromossomo
    modelo = construir_modelo(cromossomo)
    
    # Treinar com validação cruzada
    scores = cross_val_score(modelo, X_train, y_train, cv=5)
    
    # Penalizar modelos muito complexos (regularização)
    complexidade = estimar_complexidade(cromossomo)
    penalizacao = complexidade * 0.01
    
    return scores.mean() - penalizacao
```

**Operadores Especializados**:
```python
def mutacao_hiperparametros(cromossomo):
    cromossomo_mutado = cromossomo.copy()
    
    # Mutação específica por tipo de parâmetro
    if random.random() < 0.3:
        # Mutação gaussiana para parâmetros contínuos
        cromossomo_mutado['learning_rate'] *= random.gauss(1.0, 0.1)
        
    if random.random() < 0.3:
        # Mutação discreta para inteiros
        cromossomo_mutado['batch_size'] = random.choice([16, 32, 64, 128, 256])
    
    return cromossomo_mutado
```

### 2.4. Otimização de Prompts: Engenharia Automatizada

**Prompts como Estruturas Evoluíveis**

Um prompt pode ser decomposto em elementos otimizáveis:

```python
template_prompt = {
    'contexto': "Você é um {papel} especializado em {dominio}",
    'instrucao': "Sua tarefa é {acao} considerando {restricoes}",
    'formato': "Responda usando {formato} e seja {tom}",
    'exemplo': "Exemplo: {exemplo_input} -> {exemplo_output}"
}
```

**Representação para SBSE**:

1. **Abordagem por Tokens**:
   - Cromossomo = sequência de IDs de tokens
   - Mutação = substituir token por sinônimo
   - Crossover = combinar segmentos de prompts

2. **Abordagem por Templates**:
   - Cromossomo = valores para slots do template
   - Mutação = alterar valores específicos
   - Mais estruturada e interpretável

**Função de Fitness para Prompts**:
```python
def fitness_prompt(cromossomo_prompt):
    prompt = gerar_prompt_do_cromossomo(cromossomo_prompt)
    
    pontuacao_total = 0
    for caso_teste in casos_teste:
        resposta = llm.generate(prompt + caso_teste.input)
        
        # Avaliação automática
        relevancia = avaliar_relevancia(resposta, caso_teste.output_esperado)
        clareza = avaliar_clareza(resposta)
        correcao = avaliar_correcao(resposta, caso_teste.contexto)
        
        pontuacao_total += (relevancia * 0.5 + clareza * 0.2 + correcao * 0.3)
    
    return pontuacao_total / len(casos_teste)
```

**Avaliação Automática de Qualidade**:
```python
def avaliar_qualidade_resposta(resposta, contexto):
    # Usar LLM como juiz de outro LLM
    prompt_avaliacao = f"""
    Avalie a qualidade da seguinte resposta numa escala de 1-10:
    
    Contexto: {contexto}
    Resposta: {resposta}
    
    Critérios:
    - Relevância ao contexto
    - Clareza e organização  
    - Correção factual
    - Completude
    
    Responda apenas com um número de 1 a 10.
    """
    
    avaliacao = llm_juiz.generate(prompt_avaliacao)
    return extrair_pontuacao(avaliacao)
```

## Seção 3: Laboratório Prático Guiado (Google Colab)

### 3.1. Roteiro do Notebook

**Arquivo**: `modulo4_sbse_sistemas_ia.ipynb`

Este laboratório representa o estado da arte em SBSE, aplicando técnicas de otimização aos desafios únicos dos sistemas de Inteligência Artificial. Trabalharemos com três problemas progressivamente complexos que preparam diretamente para o projeto final.

### 3.2. Estrutura do Laboratório

**Parte 1: Preparação do Ambiente de IA**
- Configuração de bibliotecas (Scikit-learn, Transformers, OpenAI API)
- Carregamento de datasets com vieses conhecidos
- Configuração de modelos de exemplo (classificador de crédito, sistema de recomendação)

**Parte 2: Fairness Testing Automatizado**
- Implementação de detector de viés usando algoritmos genéticos
- Geração de perfis sintéticos para testar modelo de aprovação de crédito
- Identificação automática de casos de maior discriminação
- Análise dos padrões de viés descobertos

**Parte 3: Otimização de Hiperparâmetros**
- Comparação: Grid Search vs Random Search vs Algoritmo Genético
- Otimização de rede neural para classificação de imagens
- Implementação de operadores especializados para tipos mistos de parâmetros
- Análise de convergência e qualidade das soluções encontradas

**Parte 4: Otimização Automática de Prompts**
- Definição de template de prompt otimizável
- Implementação de função de fitness baseada em avaliação automática
- Evolução de prompts para tarefas específicas (summarização, Q&A)
- Comparação de prompts otimizados vs. criados manualmente

**Parte 5: Integração e Projeto Final**
- Apresentação detalhada da especificação do projeto final
- Discussão de problemas elegíveis e critérios de avaliação
- Sessão de brainstorming para ideias de projeto
- Planejamento inicial e formação de grupos

## Seção 4: Análise e Discussão dos Resultados

### 4.1. Interpretando os Resultados

**Eficácia do Fairness Testing**

Examine os casos de discriminação descobertos:

- **Magnitude do viés**: Quão grande é a diferença de tratamento encontrada?
- **Padrões emergentes**: Existem combinações de atributos que amplificam o viés?
- **Casos extremos**: O algoritmo encontrou cenários não óbvios de discriminação?
- **Validade dos casos**: Os perfis gerados são realistas ou artificiais?

**Performance da Otimização de Hiperparâmetros**

Compare as três abordagens:

| Métrica | Grid Search | Random Search | Algoritmo Genético |
|---------|-------------|---------------|-------------------|
| **Melhor acurácia** | ? | ? | ? |
| **Tempo de convergência** | ? | ? | ? |
| **Número de avaliações** | ? | ? | ? |
| **Estabilidade** | ? | ? | ? |

**Qualidade dos Prompts Otimizados**

Analise melhorias obtidas:

- **Pontuação de fitness**: Aumento quantitativo na qualidade
- **Interpretabilidade**: Os prompts otimizados fazem sentido semântico?
- **Generalização**: Funcionam bem em casos não vistos durante otimização?
- **Robustez**: Mantêm qualidade com pequenas variações?

### 4.2. O "Porquê" das Decisões

**Escolha de Algorithmos Genéticos para Fairness**

AGs são ideais para fairness testing porque:
- **Exploração diversificada**: Encontram casos em regiões inesperadas do espaço
- **Otimização sem gradiente**: Não precisam de derivadas (modelos são caixas-pretas)
- **Flexibilidade**: Lidam com atributos categóricos e numéricos simultaneamente
- **Interpretabilidade**: Casos encontrados são diretamente analisáveis por humanos

**Integração de Penalização por Complexidade**

Na otimização de hiperparâmetros, penalizamos modelos complexos porque:
- **Prevenção de overfitting**: Modelos simples generalizam melhor
- **Eficiência computacional**: Modelos menores são mais práticos em produção
- **Interpretabilidade**: Simplicidade facilita explicação e auditoria
- **Robustez**: Modelos simples são menos sensíveis a variações nos dados

**Avaliação Automática vs. Humana para Prompts**

Optamos por avaliação automática porque:
- **Escalabilidade**: Permite testar milhares de variações de prompt
- **Consistência**: Elimina variabilidade subjetiva de avaliadores humanos
- **Velocidade**: Feedback imediato para o processo de otimização
- **Objetividade**: Reduz vieses pessoais na avaliação

## Seção 5: Síntese e Próximos Passos

### 5.1. Resumo do Laboratório/Capítulo

- **Fairness Testing Revolucionário**: Desenvolvemos sistema automatizado que encontra casos de discriminação em modelos de IA, detectando vieses que passariam despercebidos em testes manuais.

- **Otimização Inteligente de Hiperparâmetros**: Superamos abordagens tradicionais usando algoritmos genéticos, encontrando configurações superiores com menor esforço computacional.

- **Engenharia de Prompts Automatizada**: Automatizamos processo tradicionalmente manual de criação de prompts, usando SBSE para otimizar sistematicamente a qualidade das interações com LLMs.

- **Integração de Técnicas**: Combinamos SBSE com avaliação automática usando IA, criando sistemas que se otimizam de forma autônoma.

- **Preparação para Projeto Final**: Estabelecemos base técnica e conceitual necessária para desenvolver projetos inovadores que integrem SBSE com sistemas de IA.

### 5.2. Preparação para o Próximo Bloco

O Módulo 5 introduzirá técnicas avançadas e considerações éticas que enriquecerão significativamente seus projetos finais:

**Otimização Multi-Objetivo**
- Quando temos objetivos conflitantes (performance vs. fairness)
- Fronteira de Pareto e soluções de compromisso
- Algoritmo NSGA-II e biblioteca Pymoo

**Ética e Responsabilidade**
- Lei de Goodhart: "Quando uma medida se torna meta, deixa de ser boa medida"
- Casos de otimização que geraram consequências não intencionais
- Como projetar funções de fitness éticas e robustas

**Reflexão Crítica**
- Limitações da automação em decisões que afetam pessoas
- Balanceamento entre eficiência e transparência
- Responsabilidade do engenheiro de software na era da IA

As técnicas de SBSE para sistemas de IA aprendidas neste módulo representam a fronteira atual da pesquisa. No projeto final, você terá oportunidade de contribuir para essa fronteira, desenvolvendo soluções inovadoras que combinem otimização inteligente com responsabilidade social.