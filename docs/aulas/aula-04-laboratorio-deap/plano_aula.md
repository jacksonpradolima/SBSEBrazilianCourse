## Módulo 2: Técnicas de Otimização e a Sinergia com IA (Aulas 3-5)

### Objetivo Geral:
Capacitar os alunos a formular um problema de engenharia de software como um problema de busca e a utilizar LLMs como uma ferramenta assistiva nesse processo. O foco é na habilidade prática de traduzir um requisito vago de "melhorar o software" em uma função de fitness mensurável e em uma representação computacional.

### Objetivos Específicos:
* Implementar soluções de SBSE utilizando uma biblioteca profissional como a DEAP.
* Modelar diferentes problemas de software com representações adequadas (binária, permutação).
* Projetar funções de fitness que lidem com restrições do problema.
* Utilizar Engenharia de Prompt para gerar hipóteses e métricas para as funções de fitness.

### Conteúdo Programático Detalhado:
* **Aula 4: Laboratório com a Biblioteca DEAP**
    * **Introdução ao DEAP:** O framework padrão da indústria para computação evolutiva em Python.
    * **Estrutura do DEAP:** `creator`, `toolbox`, `tools`, `algorithms`.
    * **Code-Along:** Reimplementação do Problema da Mochila com DEAP, mostrando a abstração e o poder da biblioteca.
    * **Aplicação:** Resolução de um problema de alocação de tarefas a desenvolvedores, visando minimizar o tempo total e balancear a carga de trabalho.