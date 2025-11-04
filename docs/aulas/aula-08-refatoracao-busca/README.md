---
titulo: "Aula 8: Refatoração Baseada em Busca - Pagando a Dívida Técnica com Otimização"
aula_numero: 8
carga_horaria: "4 horas"
foco_principal: "Utilizar SBSE para identificar e corrigir 'code smells', otimizando a qualidade estrutural do software com base em métricas e sugestões de LLMs."
metodologia: "Exposição Teórica e Laboratório Prático"
tipo_aula: "Workshop Prático"
objetivos:
  - "Formular o problema de refatoração de software como um problema de busca."
  - "Identificar e quantificar 'code smells' usando métricas de software como Coesão, Acoplamento e Complexidade."
  - "Utilizar um LLM para gerar candidatas a refatoração e um otimizador para escolher a melhor sequência."
pre_requisitos:
  - "Conceitos de SBSE e Algoritmos Genéticos."
  - "Conhecimento básico de métricas de qualidade de software."
  - "Experiência com APIs de LLMs (Aula 5)."
---

# Aula 8: Refatoração Baseada em Busca - Pagando a Dívida Técnica com Otimização

## Seção 1: Abertura e Engajamento

### 1.1. Problema Motivador

Todo engenheiro de software já passou por isso: você herda um projeto e encontra "aquela" classe. Uma classe monstruosa de 3.000 linhas, apelidada de `GerenciadorUtils`, que lida com conexões de banco de dados, formatação de datas, lógica de negócio, envio de e-mails e, por algum motivo, também calcula o seno de um ângulo. Essa é uma "God Class", um dos muitos "code smells" (maus cheiros de código) que indicam profunda dívida técnica.

A decisão de refatorar é fácil. A pergunta difícil é: *como*? Qual o primeiro passo? Extrair uma classe `DatabaseManager`? Ou uma `EmailService`? E se movermos o método A para a nova classe B, isso não aumenta perigosamente o acoplamento com a classe C? A refatoração manual é uma arte delicada, cheia de trade-offs e com alto risco de introduzir novos bugs. E se pudéssemos transformar essa arte em uma ciência? E se um algoritmo pudesse analisar milhares de sequências de refatoração possíveis e nos apresentar a que produz o código mais coeso, menos acoplado e mais simples? Bem-vindo à Refatoração Baseada em Busca.

### 1.2. Objetivos deste Capítulo

Ao final deste capítulo, você será capaz de:

*   **Quantificar a Dívida Técnica:** Traduzir o conceito abstrato de "código ruim" em métricas de software objetivas e calculáveis (Coesão, Acoplamento, Complexidade).
*   **Formular a Refatoração como Busca:** Modelar o problema de encontrar a melhor sequência de refatorações como um problema de otimização.
*   **Integrar IA no Processo:** Utilizar um LLM como um "arquiteto de software assistente" para sugerir possíveis refatorações e, em seguida, usar um algoritmo de busca para avaliar e classificar essas sugestões.

## Seção 2: Fundamentos Teóricos (Versão Expressa)

Refatoração Baseada em Busca (Search-Based Refactoring) trata a melhoria da qualidade do software como um problema de otimização. O objetivo é encontrar uma sequência de transformações no código que otimize um conjunto de métricas de qualidade.

### O Tripé da Refatoração Baseada em Busca

1.  **Representação (O Indivíduo):** O que estamos otimizando?
    *   **O que é?** Um indivíduo representa uma sequência de operações de refatoração.
    *   **Exemplo:** Uma lista de tuplas como `[('move_method', 'metodo_A', 'classe_X', 'classe_Y'), ('extract_class', 'classe_Z', ['metodo_B', 'metodo_C'])]`. Cada tupla é uma operação de refatoração.

2.  **Função de Fitness (A Bússola da Qualidade):** Como medimos se uma refatoração foi "boa"?
    *   **O que é?** Uma função que calcula um score de qualidade do código *após* a aplicação da sequência de refatoração. Geralmente é uma combinação de várias métricas.
    *   **Métricas Chave:**
        *   **Coesão (Maximizar):** Mede o quão focada e relacionada é a responsabilidade de uma classe. Uma classe coesa faz uma coisa só e a faz bem. Métrica comum: **LCOM4 (Lack of Cohesion in Methods)**. Queremos minimizar o LCOM4.
        *   **Acoplamento (Minimizar):** Mede o grau de dependência entre as classes. Baixo acoplamento é desejável, pois torna o sistema mais modular e fácil de manter. Métrica comum: **CBO (Coupling Between Objects)**.
        *   **Complexidade (Minimizar):** Mede a complexidade lógica de um método. Métodos complexos são difíceis de entender e testar. Métrica comum: **Complexidade Ciclomática (WMC - Weighted Methods per Class)**.

3.  **Busca (O Motor da Refatoração):**
    *   **O que é?** Um algoritmo (geralmente um Algoritmo Genético) que explora o vasto espaço de possíveis sequências de refatoração para encontrar aquela que produz o melhor score de fitness.

### O Papel do LLM: O Oráculo de Sugestões

O espaço de busca para refatoração é infinito. Um AG pode aplicar uma sequência aleatória de "Mover Método", mas isso é ineficiente. Aqui, o LLM atua como um "oráculo" que poda a árvore de busca, sugerindo apenas as refatorações que fazem sentido semanticamente.

```{mermaid}
graph TD
    A[Código com "Code Smells"] --> B{LLM: "Aja como um arquiteto de software..."};
    B --> C["Sugestão 1: Extrair Classe 'DB'"];
    B --> D["Sugestão 2: Mover método 'send'"];
    B --> E["Sugestão 3: Renomear método 'proc'"];
    C --> F[Otimizador SBSE];
    D --> F;
    E --> F;
    F -- Avalia Fitness (Coesão, Acoplamento) de cada sugestão --> G[Ranking: Sugestão 1 é a melhor];
    G --> H[Código Refatorado];
```

## Seção 3: Exemplo Ilustrativo: Antes e Depois

Vamos analisar uma "God Class" e o efeito de uma refatoração na coesão.

**Antes: Baixa Coesão (LCOM4 alto)**
```python
class DataProcessor:
    def read_from_db(self, query):
        # ... código de banco de dados ...
        return data

    def write_to_file(self, data, filename):
        # ... código de I/O de arquivo ...

    def calculate_stats(self, data):
        # ... código de estatística ...
        return stats

    def send_report_email(self, report):
        # ... código de envio de email ...
```
Nesta classe, `read_from_db` e `write_to_file` não compartilham nenhum atributo de instância com `calculate_stats` ou `send_report_email`. Eles são grupos de métodos desconexos, indicando baixa coesão.

**Depois: Alta Coesão (LCOM4 baixo)**
```python
class DatabaseReader:
    def __init__(self, connection_string):
        self.conn = ...
    def read(self, query): ...

class ReportGenerator:
    def calculate_stats(self, data): ...
    def format_report(self, stats): ...

class EmailService:
    def __init__(self, smtp_server):
        self.server = ...
    def send(self, report): ...
```
Após a refatoração "Extrair Classe", cada classe tem uma responsabilidade única e seus métodos são altamente relacionados. A qualidade do código, medida pelas métricas, melhorou objetivamente.

## Seção 4: Análise e Tópicos Avançados

### O Desafio da Refatoração Semântica

Uma grande limitação da refatoração puramente baseada em métricas é que ela não entende o *significado* do código. Um algoritmo pode sugerir mover um método que melhora a coesão, mas que quebra a lógica de negócio de uma forma sutil. É por isso que a sinergia com LLMs é tão promissora: o LLM entende a semântica e sugere refatorações que fazem sentido, enquanto o SBSE avalia objetivamente o impacto estrutural dessas sugestões.

### Refatoração Multi-Objetivo

Raramente otimizamos para uma única métrica. Muitas vezes, queremos **maximizar a coesão** e **minimizar o acoplamento** ao mesmo tempo. Esses objetivos podem ser conflitantes. Uma refatoração que melhora a coesão de uma classe pode acidentalmente aumentar seu acoplamento com outras. Este é um problema de otimização multi-objetivo, onde a solução não é um único valor, mas uma **Fronteira de Pareto** de soluções de trade-off, exatamente como vimos na Aula 13.

## Seção 5: Síntese e Próximos Passos

### 5.1. Resumo do Capítulo

*   A Refatoração Baseada em Busca (SBSE) transforma a melhoria da qualidade do código em um problema de otimização.
*   "Code smells" como "God Class" podem ser quantificados através de métricas de software como **Coesão (LCOM4)**, **Acoplamento (CBO)** e **Complexidade (WMC)**.
*   A função de fitness em um problema de refatoração é um score de qualidade derivado dessas métricas.
*   LLMs podem atuar como "oráculos de sugestão", propondo refatorações semanticamente coerentes, que são então avaliadas e classificadas por um otimizador SBSE.
*   A refatoração é frequentemente um problema multi-objetivo, buscando um equilíbrio (trade-off) entre diferentes métricas de qualidade.

### 5.2. Ponte e Briefing para o Workshop Prático (`.ipynb`)

**Teaser para o Aluno:** Chega de falar sobre dívida técnica, é hora de pagá-la! No workshop prático, você será o arquiteto de software encarregado de limpar um código problemático. Você usará o poder de um LLM para obter conselhos de refatoração e implementará um otimizador para provar, com números, qual conselho é o melhor.

**Briefing para o Agente de Prática (Geração do `workshop.ipynb`):**

O notebook deve implementar um sistema que usa um LLM para sugerir refatorações e as avalia com base em métricas de qualidade.

1.  **Código-Alvo:** Forneça uma classe Python `GodClass.py` que exiba múltiplos "code smells". Ela deve ter métodos que lidam com responsabilidades distintas (ex: manipulação de strings, cálculos matemáticos, formatação de dados) e baixa coesão.

2.  **Cálculo de Métricas:**
    *   Implemente funções para calcular métricas de qualidade de software em um arquivo Python. Use uma biblioteca como `radon` para calcular a **Complexidade Ciclomática** e o **Índice de Manutenibilidade**.
    *   Crie uma função para calcular uma aproximação da **Coesão (LCOM4)**.

3.  **Interação com LLM:**
    *   Crie uma célula que lê o código da `GodClass.py`.
    *   Use um prompt de "Persona" ("Aja como um Arquiteto de Software Sênior...") para pedir ao LLM que analise a classe e sugira **três operações de refatoração específicas** (ex: "Extraia os métodos X e Y para uma nova classe chamada 'StringUtil'"). As sugestões devem ser retornadas em um formato estruturado (ex: JSON).

4.  **Simulação e Avaliação:**
    *   Para cada uma das três sugestões do LLM:
        *   **Simule a refatoração:** Crie uma representação em memória do código como ele seria *após* a refatoração (não precisa modificar os arquivos em disco, pode ser uma manipulação de strings ou AST).
        *   **Calcule as métricas:** Execute as funções de cálculo de métricas no código refatorado simulado.
        *   **Calcule o Fitness:** Crie uma função de fitness que combine as métricas (ex: `score = (w1 * coesao) - (w2 * acoplamento) - (w3 * complexidade)`).

5.  **Análise e Conclusão:**
    *   Apresente uma tabela comparando o score de fitness do código "Antes" com o score de cada uma das três sugestões de refatoração "Depois".
    *   Declare qual sugestão do LLM foi a vencedora com base na melhoria objetiva das métricas.