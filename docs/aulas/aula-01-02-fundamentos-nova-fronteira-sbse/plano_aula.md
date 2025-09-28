# Módulo 1: Fundamentos e a Nova Fronteira da SBSE (Aulas 1-2)

## Objetivo Geral
Introduzir a disciplina de Engenharia de Software Baseada em Busca (SBSE), contextualizando seus fundamentos históricos e sua crescente relevância na era da Inteligência Artificial. O objetivo é estabelecer uma base conceitual sólida para que os alunos compreendam "por que" e "como" a otimização pode ser aplicada aos problemas de engenharia de software.

## Objetivos Específicos
* Diferenciar a SBSE de abordagens tradicionais de engenharia de software.
* Identificar os três componentes essenciais de um problema de SBSE: representação, função de fitness e algoritmo de busca.
* Implementar os componentes de um Algoritmo Genético (AG) do zero para entender seu funcionamento interno.
* Contextualizar o papel da SBSE na validação e otimização de sistemas de software assistidos por IA.

## Conteúdo Programático Detalhado

### Aula 1: A Crise da Complexidade e a Solução por Otimização
* **Introdução:** Apresentação da disciplina, cronograma e do projeto final.
* **O Problema Fundamental da Eng. de Software:** Explosão de complexidade, múltiplos stakeholders, objetivos conflitantes (custo, tempo, qualidade).
* **O que é SBSE?**
    * Mapeando problemas de software para problemas de busca.
    * O "espaço de busca": O universo de todas as soluções possíveis.
    * A "função de fitness": A bússola que guia a busca, medindo a "qualidade" de uma solução.
    * A "representação": Como codificar uma solução de software para que o computador a entenda (ex: um array binário).
* **Visão Geral do Cenário de Otimização:**
    * Buscas locais (Hill Climbing) vs. Buscas globais (Meta-heurísticas).
    * O problema do "ótimo local" e como as meta-heurísticas tentam escapar dele.

### Aula 2: Laboratório Prático - Construindo um Algoritmo Genético
* **Anatomia de um Algoritmo Genético (AG):**
    * **População:** Conjunto de soluções candidatas.
    * **Indivíduo (Cromossomo):** Uma única solução codificada.
    * **Seleção:** Como escolher os "pais" para a próxima geração (ex: Roleta, Torneio).
    * **Crossover (Recombinação):** Como combinar dois pais para gerar filhos (ex: Ponto Único, Dois Pontos).
    * **Mutação:** Como introduzir diversidade na população para evitar estagnação.
* **Code-Along:** Implementação de um AG simples em Python para resolver o "Problema da Mochila", um análogo clássico para seleção de recursos.
* **Conexão com a Era da IA:** Discussão sobre como AGs podem ser usados para otimizar configurações de modelos de IA ou validar código gerado por LLMs.