## Módulo 2: Técnicas de Otimização e a Sinergia com IA (Aulas 3-5)

### Objetivo Geral:
Capacitar os alunos a formular um problema de engenharia de software como um problema de busca e a utilizar LLMs como uma ferramenta assistiva nesse processo. O foco é na habilidade prática de traduzir um requisito vago de "melhorar o software" em uma função de fitness mensurável e em uma representação computacional.

### Objetivos Específicos:
* Implementar soluções de SBSE utilizando uma biblioteca profissional como a DEAP.
* Modelar diferentes problemas de software com representações adequadas (binária, permutação).
* Projetar funções de fitness que lidem com restrições do problema.
* Utilizar Engenharia de Prompt para gerar hipóteses e métricas para as funções de fitness.

### Conteúdo Programático Detalhado:
* **Aula 3: Formulação de Problemas e Representações**
    * **A Arte da Representação:**
        * **Binária:** Para problemas de seleção (ex: "quais features incluir?").
        * **Permutação:** Para problemas de ordenação (ex: "qual a melhor ordem para executar estes testes?").
        * **Numérica (Inteira/Real):** Para problemas de configuração (ex: "quais os melhores valores para estes parâmetros?").
    * **Projetando a Função de Fitness:**
        * Lidando com restrições: A abordagem da função de penalidade.
        * Normalização de múltiplos objetivos em uma única função ponderada (abordagem inicial).