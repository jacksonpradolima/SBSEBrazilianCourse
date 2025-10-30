## Módulo 5: Tópicos Avançados e Ética em SBSE (Aulas 13-14)

### Objetivo Geral:
Apresentar técnicas avançadas de otimização, como a abordagem multi-objetivo, e promover uma reflexão crítica sobre as implicações éticas do uso de otimização automatizada em software, enriquecendo a análise que poderá ser feita no projeto final.

### Objetivos Específicos:
* Diferenciar otimização mono e multi-objetivo.
* Compreender os conceitos de Dominância de Pareto e Fronteira de Pareto.
* Implementar uma solução multi-objetivo usando a biblioteca Pymoo e o algoritmo NSGA-II.
* Analisar os riscos éticos da otimização e a Lei de Goodhart.

### Conteúdo Programático Detalhado:
* **Aula 13: Laboratório de Otimização Multi-Objetivo com Pymoo**
    * **O Mundo Real é Multi-Objetivo:** Objetivos conflitantes (ex: performance vs. segurança; custo vs. valor).
    * **Teoria Essencial:**
        * **Dominância de Pareto:** Quando uma solução é inegavelmente melhor que outra.
        * **Fronteira de Pareto:** O conjunto de todas as soluções não-dominadas, representando o trade-off ótimo.
    * **O Algoritmo NSGA-II:** Breve explicação de sua estratégia de ordenação não-dominada e distância de aglomeração (crowding distance).
    * **Code-Along com Pymoo:** Resolução do *Next Release Problem* (o problema do projeto final) em uma versão simplificada, mostrando como gerar e visualizar a Fronteira de Pareto.
* **Aula 14: Seminário sobre Ética e o Lado Sombrio da Otimização**
    * **A Lei de Goodhart:** "Quando uma medida se torna uma meta, ela deixa de ser uma boa medida".
    * **Estudos de Caso:**
        * **Redes Sociais:** Otimização para "engajamento" e suas consequências (polarização, desinformação).
        * **Sistemas de Contratação:** Otimização para "fit com a cultura" pode levar à discriminação.
        * **Gig Economy:** Otimização de algoritmos de alocação de tarefas e o impacto no bem-estar dos trabalhadores.
    * **Discussão Guiada:** Qual é a responsabilidade do engenheiro de software? Como podemos projetar funções de fitness mais éticas e robustas?