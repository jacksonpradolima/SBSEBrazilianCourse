## Módulo 3: SBSE Aplicada à Engenharia de Software Tradicional (Aulas 6-8)

### Objetivo Geral:
Aplicar as técnicas de SBSE para resolver dois dos problemas mais clássicos e custosos da engenharia de software: teste e refatoração. O objetivo é que os alunos desenvolvam soluções práticas que automatizem a geração de dados de teste e a melhoria de código legado, servindo como base técnica para o projeto final.

### Objetivos Específicos:
* Implementar um gerador de testes automatizado que busca maximizar a cobertura de código.
* Entender e quantificar o conceito de "dívida técnica" e "code smells".
* Desenvolver um otimizador que sugira a melhor sequência de refatorações para melhorar a qualidade de um software.
* Utilizar LLMs como um oráculo para sugerir possíveis refatorações.

### Conteúdo Programático Detalhado:
* **Aulas 6-7: Teste Baseado em Busca (Search-Based Software Testing - SBST)**
    * **O Desafio:** Por que testar tudo é impossível? O conceito de "oráculo de teste".
    * **Representação:** O cromossomo representa um conjunto de dados de entrada para uma função ou sistema.
    * **Função de Fitness:** O guia da busca é um critério de cobertura.
        * **Cobertura de Sentenças (Statement Coverage):** Atingir o maior número de linhas de código.
        * **Cobertura de Ramos (Branch Coverage):** Forçar a execução de todos os `if/else`, `case`, etc. (Mais poderoso).
    * **Laboratório Prático:** Dado um código Python com lógica condicional complexa, os alunos irão construir um AG que gera automaticamente os dados de entrada (`(x, y, z)`) necessários para maximizar a cobertura de ramos, encontrando bugs em caminhos obscuros do código.
* **Aula 8: Refatoração Baseada em Busca**
    * **Dívida Técnica e Code Smells:** O que são "God Classes", "Long Methods", "Feature Envy"?
    * **Métricas de Qualidade de Software:**
        * **Coesão:** LCOM4 (Lack of Cohesion in Methods).
        * **Acoplamento:** CBO (Coupling Between Objects).
        * **Complexidade:** Complexidade Ciclomática.
    * **O Problema de Otimização:** Encontrar a sequência de operações de refatoração (ex: "Mover Método", "Extrair Classe") que otimiza um conjunto dessas métricas.
    * **Laboratório Prático:** Análise de um código Java/Python com "smells". Os alunos irão:
        1. Usar um LLM para sugerir 3 possíveis refatorações para uma classe problemática.
        2. Implementar um otimizador simples para avaliar qual das 3 sugestões leva à melhoria mais significativa nas métricas de qualidade.