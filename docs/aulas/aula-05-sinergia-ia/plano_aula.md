## Módulo 2: Técnicas de Otimização e a Sinergia com IA (Aulas 3-5)

### Objetivo Geral:
Capacitar os alunos a formular um problema de engenharia de software como um problema de busca e a utilizar LLMs como uma ferramenta assistiva nesse processo. O foco é na habilidade prática de traduzir um requisito vago de "melhorar o software" em uma função de fitness mensurável e em uma representação computacional.

### Objetivos Específicos:
* Implementar soluções de SBSE utilizando uma biblioteca profissional como a DEAP.
* Modelar diferentes problemas de software com representações adequadas (binária, permutação).
* Projetar funções de fitness que lidem com restrições do problema.
* Utilizar Engenharia de Prompt para gerar hipóteses e métricas para as funções de fitness.

### Conteúdo Programático Detalhado:
* **Aula 5: Laboratório de Sinergia com IA**
    * **Engenharia de Prompt para Definição de Fitness:**
        * **Técnica:** "Persona Prompting" ("Aja como um gerente de produto sênior...").
        * **Objetivo:** Dado um requisito de qualidade vago (ex: "o código deve ser mais manutenível"), usar um LLM para sugerir métricas concretas e quantificáveis (ex: Complexidade Ciclomática, Índice de Manutenibilidade, Coesão de Classes).
    * **Engenharia de Prompt para Geração de Heurísticas:**
        * **Técnica:** "Chain-of-Thought Prompting".
        * **Objetivo:** Pedir a um LLM para sugerir operadores de mutação ou crossover específicos para um problema (ex: "Para um problema de otimização de rotas, sugira um operador de mutação que seja mais inteligente do que uma simples troca aleatória de duas cidades").