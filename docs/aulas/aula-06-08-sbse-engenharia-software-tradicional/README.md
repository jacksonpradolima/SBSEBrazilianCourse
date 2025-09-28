---
title: "SBSE Aplicada à Engenharia de Software Tradicional"
number: "06-08"
type: "Workshop Prático"
duration: "6 horas-aula"
objectives:
  - "Implementar um gerador de testes automatizado que busca maximizar a cobertura de código"
  - "Entender e quantificar o conceito de 'dívida técnica' e 'code smells'"
  - "Desenvolver um otimizador que sugira a melhor sequência de refatorações para melhorar a qualidade de um software"
  - "Utilizar LLMs como um oráculo para sugerir possíveis refatorações"
methodology: "Laboratório prático com problemas reais de teste e refatoração de software"
tools: ["Python 3.10+", "DEAP", "Coverage.py", "Pylint", "Radon", "OpenAI API", "AST"]
prerequisites: ["DEAP básico", "Análise estática de código", "Conceitos de qualidade de software"]
keywords: ["Teste baseado em busca", "Cobertura de código", "Refatoração", "Code smells", "Dívida técnica", "SBST"]
author: "Curso SBSE na Era da IA"
date: "2025"
language: "pt-BR"
---

# SBSE Aplicada à Engenharia de Software Tradicional

## Seção 1: Abertura e Engajamento

### 1.1. Problema Motivador

A equipe de desenvolvimento da fintech XYZ enfrenta um dilema crítico. Seu sistema de processamento de pagamentos tem 50.000 linhas de código Python, mas apenas 60% de cobertura de testes. O prazo para a auditoria de segurança é em 2 semanas, e a empresa precisa demonstrar que o sistema foi adequadamente testado. Manualmente, seria impossível criar testes suficientes no prazo disponível.

Simultaneamente, o código acumulou "dívida técnica" ao longo de 3 anos de desenvolvimento acelerado: classes com mais de 1000 linhas, métodos com complexidade ciclomática acima de 20, e acoplamento excessivo entre módulos. A equipe sabe que precisa refatorar, mas como priorizar? Quais refatorações trarão maior benefício? Em que ordem executá-las para minimizar riscos?

Estes são exemplos clássicos de problemas onde **SBSE pode automatizar tarefas tradicionalmente manuais e custosas**: geração inteligente de testes e otimização de sequências de refatoração. Ao invés de depender apenas da experiência humana, podemos usar algoritmos de otimização para explorar sistematicamente o espaço de possibilidades e encontrar soluções que humanos jamais considerariam.

### 1.2. Objetivos deste Laboratório/Capítulo

Ao final deste módulo, você será capaz de:

1. **Automatizar geração de testes**: Implementar um sistema que gera automaticamente dados de entrada para maximizar cobertura de código, descobrindo bugs em caminhos de execução raramente testados manualmente.

2. **Quantificar qualidade de software**: Utilizar métricas objetivas para medir dívida técnica, complexidade e acoplamento, transformando conceitos subjetivos como "código ruim" em números precisos e acionáveis.

3. **Otimizar refatorações**: Desenvolver um otimizador que analisa código existente e sugere a sequência ideal de refatorações para maximizar melhoria de qualidade enquanto minimiza riscos de introdução de bugs.

## Seção 2: Fundamentos Teóricos

### 2.1. Teste Baseado em Busca (SBST): Versão Expressa

**O Problema Fundamental do Teste**

Testar software é fundamentalmente um problema de **exploração inteligente**. Para uma função simples com 3 parâmetros inteiros, cada um variando de 0 a 100, existem $101^3 = 1.030.301$ combinações possíveis de entrada. Para sistemas reais, esse número se torna astronomicamente grande.

O **oráculo de teste** - nossa capacidade de determinar se um resultado está correto - é frequentemente limitado ou custoso. Por isso, focamos em critérios de **cobertura** como proxy para qualidade de teste.

**Tipos de Cobertura**

1. **Cobertura de Sentenças (Statement Coverage)**
   - **Meta**: Executar cada linha de código pelo menos uma vez
   - **Intuição**: Se uma linha nunca executa, bugs nela passam despercebidos
   - **Limitação**: Não garante que todas as condições foram testadas

2. **Cobertura de Ramos (Branch Coverage)**
   - **Meta**: Executar cada caminho condicional (if/else, loops) pelo menos uma vez  
   - **Intuição**: Bugs frequentemente ocorrem em condições de borda
   - **Vantagem**: Mais rigorosa que cobertura de sentenças

3. **Cobertura de Condições (Condition Coverage)**
   - **Meta**: Testar cada condição booleana individual
   - **Exemplo**: Para `if (A and B)`, testar A=True/False e B=True/False
   - **Aplicação**: Crítica para lógica complexa de negócios

**SBSE para Teste: O Algoritmo**

```python
def gerar_testes_com_sbse(funcao_alvo, criterio_cobertura):
    # Representação: conjunto de parâmetros de entrada
    # Fitness: porcentagem de cobertura alcançada
    # Objetivo: maximizar cobertura
    
    populacao = gerar_populacao_inicial()
    
    for geracao in range(MAX_GERACOES):
        for individuo in populacao:
            cobertura = executar_testes(funcao_alvo, individuo)
            individuo.fitness = cobertura
        
        nova_populacao = aplicar_operadores_geneticos(populacao)
        populacao = selecionar_melhores(nova_populacao)
    
    return melhor_conjunto_testes(populacao)
```

**Vantagens do SBST**

- **Automação**: Reduz drasticamente tempo manual de criação de testes
- **Exploração sistemática**: Encontra casos de teste que humanos não considerariam
- **Otimização contínua**: Melhora progressivamente a qualidade dos testes
- **Adaptabilidade**: Funciona com diferentes linguagens e tipos de sistema

### 2.2. Refatoração Baseada em Busca: A Ciência da Melhoria de Código

**Dívida Técnica: Quantificando o "Código Ruim"**

**Dívida técnica** é uma metáfora criada por Ward Cunningham: assim como dívida financeira, código de baixa qualidade gera "juros" na forma de maior tempo de manutenção, mais bugs e menor produtividade da equipe.

**Code Smells: Sintomas de Problemas Estruturais**

1. **God Class (Classe Deus)**
   - **Sintoma**: Classe com muitas responsabilidades
   - **Métrica**: Linhas de código > 1000, ou alta LCOM
   - **Solução**: Extrair responsabilidades em classes separadas

2. **Long Method (Método Longo)**
   - **Sintoma**: Método fazendo muitas coisas
   - **Métrica**: Linhas > 50, complexidade ciclomática > 15
   - **Solução**: Extrair submétodos, dividir responsabilidades

3. **Feature Envy (Inveja de Feature)**
   - **Sintoma**: Método usando mais atributos de outras classes que da própria
   - **Métrica**: Número de acessos externos vs. internos
   - **Solução**: Mover método para classe mais apropriada

**Métricas de Qualidade de Software**

**1. Coesão - LCOM4 (Lack of Cohesion in Methods)**
```python
def calcular_lcom4(classe):
    # Mede se métodos de uma classe trabalham com 
    # atributos relacionados
    # Valor ideal: próximo de 0
    # Valor alto: classe tem responsabilidades dispersas
    pass
```

**2. Acoplamento - CBO (Coupling Between Objects)**
```python
def calcular_cbo(classe):
    # Conta quantas outras classes esta classe usa
    # Valor ideal: baixo (< 10)
    # Valor alto: classe muito dependente de outras
    pass
```

**3. Complexidade Ciclomática**
```python
def calcular_complexidade_ciclomatica(metodo):
    # Conta número de caminhos independentes através do código
    # Valor ideal: < 10
    # Valor alto: método difícil de testar e manter
    pass
```

**SBSE para Refatoração: O Processo**

```python
def otimizar_refatoracoes(codigo_fonte):
    # Representação: sequência de operações de refatoração
    # Fitness: melhoria nas métricas de qualidade
    # Restrições: não quebrar funcionalidade
    
    operacoes_possiveis = [
        "extrair_metodo", "mover_metodo", "extrair_classe",
        "inline_metodo", "renomear_variavel"
    ]
    
    def fitness(sequencia_refatoracoes):
        codigo_refatorado = aplicar_refatoracoes(codigo_fonte, sequencia)
        
        # Métricas de qualidade
        coesao = calcular_coesao_media(codigo_refatorado)
        acoplamento = calcular_acoplamento_medio(codigo_refatorado)  
        complexidade = calcular_complexidade_media(codigo_refatorado)
        
        # Penalização se quebrar testes
        if quebrou_testes(codigo_refatorado):
            return -1000
            
        return coesao * 0.4 + (1/acoplamento) * 0.3 + (1/complexidade) * 0.3
    
    return otimizar_com_algoritmo_genetico(operacoes_possiveis, fitness)
```

### 2.3. Sinergia com IA: LLMs como Oráculos de Refatoração

**Limitações dos Humanos vs. Potencial da IA**

Humanos são excelentes em:
- Entender contexto de negócio
- Avaliar impacto em stakeholders
- Tomar decisões considerando fatores não-técnicos

IA é excelente em:
- Analisar código em escala
- Identificar patterns sutis
- Sugerir alternativas não óbvias
- Processar múltiplas métricas simultaneamente

**Engenharia de Prompt para Análise de Código**

```python
def analisar_codigo_com_llm(codigo, contexto):
    prompt = f"""
    Você é um arquiteto de software sênior. Analise o código abaixo:

    ```python
    {codigo}
    ```
    
    Contexto: {contexto}
    
    Identifique:
    1. 3 code smells mais críticos
    2. Sequência recomendada de refatorações
    3. Riscos de cada refatoração proposta
    4. Métricas que deveriam ser monitoradas
    
    Seja específico e prático.
    """
    
    return chamar_llm(prompt)
```

**Validação das Sugestões de IA**

```python
def validar_sugestoes_ia(codigo_original, sugestoes_llm):
    for sugestao in sugestoes_llm:
        # Aplicar refatoração sugerida
        codigo_refatorado = aplicar_refatoracao(codigo_original, sugestao)
        
        # Validar com testes automatizados
        if not testes_passam(codigo_refatorado):
            sugestao.viabilidade = "Baixa - quebra funcionalidade"
            continue
            
        # Calcular melhoria nas métricas
        melhoria = calcular_melhoria_metricas(codigo_original, codigo_refatorado)
        sugestao.impacto_quantitativo = melhoria
        
        # Estimar esforço de implementação
        sugestao.esforco_estimado = estimar_esforco(sugestao)
    
    return ordenar_por_custo_beneficio(sugestoes_llm)
```

## Seção 3: Laboratório Prático Guiado (Google Colab)

### 3.1. Roteiro do Notebook

**Arquivo**: `modulo3_teste_refatoracao_sbse.ipynb`

Este laboratório aplica SBSE a dois problemas fundamentais da engenharia de software: automatização de testes e otimização de refatorações. Trabalharemos com código Python real, utilizando tanto técnicas clássicas quanto sinergia com IA.

**Cenário Principal**: Sistema de processamento de pedidos de e-commerce com lógica complexa de cálculo de frete, aplicação de descontos, e validação de estoque.

### 3.2. Estrutura do Laboratório

**Parte 1: Análise do Código Base**
- Carregamento do sistema de exemplo (código com bugs intencionais)
- Análise inicial de métricas de qualidade
- Identificação manual de code smells
- Medição da cobertura de testes existente

**Parte 2: Geração Automática de Testes (SBST)**
- Implementação de gerador de testes usando DEAP
- Definição de função de fitness baseada em cobertura de ramos
- Execução do algoritmo genético para maximizar cobertura
- Análise dos casos de teste gerados vs. testes manuais

**Parte 3: Descoberta de Bugs com Testes Gerados**
- Execução dos testes gerados no código com bugs
- Identificação de falhas encontradas automaticamente
- Comparação com bugs que testes manuais não detectaram
- Análise da eficácia do SBST para descoberta de bugs

**Parte 4: Otimização de Refatorações**
- Quantificação das métricas de qualidade do código original
- Definição de operações de refatoração disponíveis
- Implementação de otimizador para sequência de refatorações
- Aplicação das refatorações e medição de melhorias

**Parte 5: Sinergia com IA - Análise Assistida por LLM**
- Uso de LLM para analisar code smells
- Geração de sugestões de refatoração
- Validação automática das sugestões
- Comparação entre sugestões humanas, IA e SBSE

## Seção 4: Análise e Discussão dos Resultados

### 4.1. Interpretando os Resultados

**Eficácia da Geração Automática de Testes**

Analise os seguintes aspectos dos testes gerados:

- **Cobertura alcançada**: Compare cobertura antes e depois da SBST
- **Qualidade dos casos de teste**: Examine se os testes fazem sentido semanticamente
- **Bugs descobertos**: Identifique quantos e que tipos de bugs foram encontrados
- **Casos extremos**: Observe se o algoritmo descobriu casos de borda não óbvios

**Métricas de Qualidade Pós-Refatoração**

Compare métricas antes e depois da otimização:

- **LCOM4**: Melhoria na coesão das classes
- **CBO**: Redução no acoplamento entre objetos
- **Complexidade Ciclomática**: Simplificação da lógica
- **Linhas de código**: Impacto no tamanho do código

**Comparação: Humano vs. IA vs. SBSE**

| Aspecto | Análise Humana | Sugestões LLM | Otimização SBSE |
|---------|----------------|---------------|-----------------|
| **Velocidade** | Lenta | Muito rápida | Rápida |
| **Contexto de negócio** | Excelente | Boa | Limitada |
| **Exploração de alternativas** | Limitada | Boa | Excelente |
| **Quantificação de benefícios** | Subjetiva | Qualitativa | Objetiva |
| **Reprodutibilidade** | Baixa | Média | Alta |

### 4.2. O "Porquê" das Decisões

**Escolha de Cobertura de Ramos como Fitness**

Priorizamos cobertura de ramos porque:
- **Mais rigorosa**: Garante que condicionais foram adequadamente testadas
- **Detecta mais bugs**: Bugs frequentemente ocorrem em caminhos condicionais
- **Balanceada**: Não trivial como cobertura de sentenças, nem complexa demais como cobertura de caminhos

**Estratégia de Penalização para Refatorações**

Implementamos penalização severa para refatorações que quebram testes porque:
- **Preservação da funcionalidade**: Requisito não-negociável em sistemas produtivos
- **Gradiente informativo**: Direciona busca para refatorações seguras
- **Realismo**: Reflete restrições do mundo real onde funcionalidade não pode ser comprometida

**Integração com LLM para Validação**

Usamos IA para validar e enriquecer resultados porque:
- **Contextualização**: LLMs entendem intenção semântica do código
- **Explicabilidade**: Fornecem justificativas compreensíveis para sugestões
- **Descoberta de patterns**: Identificam problemas que métricas numéricas podem não capturar

## Seção 5: Síntese e Próximos Passos

### 5.1. Resumo do Laboratório/Capítulo

- **Automação de Teste Revolucionária**: Implementamos sistema que gera automaticamente casos de teste para maximizar cobertura, descobrindo bugs que testes manuais não encontrariam.

- **Quantificação da Qualidade**: Transformamos conceitos subjetivos como "código ruim" em métricas objetivas e processos automatizados de melhoria.

- **Otimização de Refatorações**: Desenvolvemos otimizador que encontra sequências ótimas de refatorações, balanceando melhoria de qualidade com minimização de riscos.

- **Sinergia IA-SBSE**: Demonstramos como LLMs podem enriquecer e validar resultados de otimização, combinando análise quantitativa com compreensão semântica.

- **Aplicação Prática Imediata**: Todas as técnicas são diretamente aplicáveis a projetos reais, oferecendo retorno imediato em produtividade e qualidade.

### 5.2. Preparação para o Próximo Bloco

O Módulo 4 elevará nossa aplicação de SBSE para a fronteira da pesquisa: **sistemas de Inteligência Artificial**. Prepararemos para:

**Teste de Sistemas de IA**
- Desafios únicos: não-determinismo, aprendizado a partir de dados, "caixas-pretas"
- Teste de fairness e detecção de vieses
- Validação de modelos de Machine Learning

**Otimização de Hiperparâmetros**
- Alternativas inteligentes a Grid Search e Random Search
- Otimização de arquiteturas de redes neurais
- Balanceamento entre performance e recursos computacionais

**Otimização de Prompts**
- Engenharia de prompts como problema de busca
- Otimização automática de templates de prompts
- Avaliação automática de qualidade de respostas

**Introdução ao Projeto Final**
- Escolha de problema para desenvolvimento
- Integração de todas as técnicas aprendidas
- Planejamento de cronograma de desenvolvimento

As habilidades sólidas de SBSE aplicada a problemas tradicionais de software serão a base para enfrentar os desafios únicos dos sistemas inteligentes no próximo módulo.