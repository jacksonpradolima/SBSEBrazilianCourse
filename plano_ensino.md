# **Identificação**

**Disciplina:** Engenharia de Software Baseada em Busca na Era da IA

**Carga Horária:** 30 horas-aula

# **Ementa**

* Fundamentos da Engenharia de Software Baseada em Busca (SBSE).
* Algoritmos de Otimização e Meta-heurísticas (Algoritmos Genéticos, Simulated Annealing).
* SBSE aplicada a Teste, Refatoração e Manutenção de Software.
* Integração de SBSE com Inteligência Artificial e Modelos de Linguagem Grandes (LLMs).
* SBSE para teste, validação e otimização de sistemas de IA.
* Otimização de Prompts com técnicas de busca (Prompt Engineering).
* Otimização Multi-objetivo.
* Ética e Justiça (Fairness) em otimização de sistemas inteligentes.

# **Objetivo Geral**

Capacitar o aluno a projetar, implementar e validar soluções de software automatizadas e otimizadas, utilizando técnicas de Engenharia de Software Baseada em Busca (SBSE) em sinergia com Inteligência Artificial. Ao final da disciplina, o estudante será capaz de formular problemas complexos de engenharia de software como problemas de busca, aplicar algoritmos de otimização para encontrar soluções eficientes e inovadoras, e integrar essas técnicas em um fluxo de trabalho moderno que inclui LLMs e Engenharia de Prompt para criar sistemas mais robustos, eficientes e justos.

# **Objetivos Específicos**

* Compreender os conceitos fundamentais, a motivação e as aplicações da SBSE.
* Implementar e aplicar algoritmos de otimização e meta-heurísticas para resolver problemas de software.
* Utilizar SBSE para automatizar a geração de casos de teste, visando maximizar a cobertura e a detecção de falhas.
* Aplicar técnicas de busca para otimizar a refatoração de código e a manutenção de sistemas legados.
* Integrar LLMs e Engenharia de Prompt para auxiliar na formulação de problemas de SBSE e na geração de novas heurísticas.
* Desenvolver soluções de SBSE para testar e validar sistemas baseados em IA, identificando vieses e falhas.
* Aplicar otimização multi-objetivo para encontrar soluções de compromisso entre múltiplos critérios de qualidade (ex: performance vs. consumo de energia).
* Analisar e discutir as implicações éticas da otimização automatizada em sistemas de IA.

# **Metodologia**

* Aulas práticas e expositivas com foco em "code-along" e implementação em laboratório.
* Desenvolvimento de um projeto final que integra os conceitos de todos os módulos.
* Estudo de caso de problemas reais da indústria e artigos científicos recentes da área.
* Utilização de ferramentas modernas de IA, otimização e desenvolvimento em Python.
* Sessões de mentoria e discussão para o desenvolvimento do projeto final.

**Ferramentas e Tecnologias**

* **Linguagem:** Python 3.10+
* **Bibliotecas de SBSE/Otimização:** DEAP, Pymoo
* **Inteligência Artificial:** OpenAI API, Transformers (Hugging Face), LangChain, Ollama (para modelos locais)
* **Ambiente:** Jupyter Notebooks, VS Code, NotebookLM (para documentação e roteiro)
* **Testes:** Pytest
* **Análise de Dados:** Polars

# **Avaliação**

| Componente | Peso |
| :--- | :--- |
| **Projeto Final (Aplicação de SBSE em Sistemas de IA)** | 100% |

**Critérios considerados:**

* Qualidade da formulação do problema de busca.
* Correção na implementação e aplicação do algoritmo de otimização.
* Inovação na integração de técnicas de IA e Engenharia de Prompt.
* Qualidade do código, organização e documentação.
* Análise crítica dos resultados obtidos.
* Qualidade da apresentação em vídeo e demonstração prática.

**O projeto final deve:**

* Resolver um problema de engenharia de software utilizando SBSE.
* Integrar, de alguma forma, um LLM ou técnica de Engenharia de Prompt.
* Ser implementado em Python utilizando as bibliotecas recomendadas.
* Apresentar uma análise clara dos resultados da otimização em um notebook bem documentado.
* Ser acompanhado de um vídeo de apresentação que explique o projeto e os resultados.

# **Conteúdo Programático**

| Aula | Tema | Entregas / Observações |
| :--- | :--- | :--- |
| **Bloco 1 – Fundamentos da Otimização Inteligente** |
| 1-2 | **Módulo 1:** Fundamentos e a Nova Fronteira da SBSE | • Discussão sobre o impacto da IA na Engenharia de Software. |
| 3-5 | **Módulo 2:** Técnicas de Otimização e a Sinergia com IA | • Laboratório de formulação de problemas com auxílio de LLMs. |
| **Bloco 2 – Aplicações Práticas e Modernas** |
| 6-8 | **Módulo 3:** SBSE Aplicada à Engenharia de Software Tradicional | • Laboratório preparatório para o Projeto Final. |
| 9-12 | **Módulo 4:** SBSE para Sistemas de Inteligência Artificial | • Introdução aos temas centrais do Projeto Final. |
| 13-14 | **Módulo 5:** Tópicos Avançados e Ética em SBSE | • Análise de caso sobre otimização e viés em IA. |
| 15-16 | **Módulo 6:** Período para Desenvolvimento e Entrega do Projeto Final | • **Entrega assíncrona do Projeto Final e do vídeo de apresentação.** |

---

# **Detalhamento das Aulas**
## **Módulo 1: Fundamentos e a Nova Fronteira da SBSE (Aulas 1-2)**

### **Objetivo Geral:**
Introduzir a disciplina de Engenharia de Software Baseada em Busca (SBSE), contextualizando seus fundamentos históricos e sua crescente relevância na era da Inteligência Artificial. O objetivo é estabelecer uma base conceitual sólida para que os alunos compreendam "por que" e "como" a otimização pode ser aplicada aos problemas de engenharia de software.

### **Objetivos Específicos:**
* Diferenciar a SBSE de abordagens tradicionais de engenharia de software.
* Identificar os três componentes essenciais de um problema de SBSE: representação, função de fitness e algoritmo de busca.
* Implementar os componentes de um Algoritmo Genético (AG) do zero para entender seu funcionamento interno.
* Contextualizar o papel da SBSE na validação e otimização de sistemas de software assistidos por IA.

### **Conteúdo Programático Detalhado:**
* **Aula 1: A Crise da Complexidade e a Solução por Otimização**
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
* **Aula 2: Laboratório Prático - Construindo um Algoritmo Genético**
    * **Anatomia de um Algoritmo Genético (AG):**
        * **População:** Conjunto de soluções candidatas.
        * **Indivíduo (Cromossomo):** Uma única solução codificada.
        * **Seleção:** Como escolher os "pais" para a próxima geração (ex: Roleta, Torneio).
        * **Crossover (Recombinação):** Como combinar dois pais para gerar filhos (ex: Ponto Único, Dois Pontos).
        * **Mutação:** Como introduzir diversidade na população para evitar estagnação.
    * **Code-Along:** Implementação de um AG simples em Python para resolver o "Problema da Mochila", um análogo clássico para seleção de recursos.
    * **Conexão com a Era da IA:** Discussão sobre como AGs podem ser usados para otimizar configurações de modelos de IA ou validar código gerado por LLMs.

## **Módulo 2: Técnicas de Otimização e a Sinergia com IA (Aulas 3-5)**

### **Objetivo Geral:**
Capacitar os alunos a formular um problema de engenharia de software como um problema de busca e a utilizar LLMs como uma ferramenta assistiva nesse processo. O foco é na habilidade prática de traduzir um requisito vago de "melhorar o software" em uma função de fitness mensurável e em uma representação computacional.

### **Objetivos Específicos:**
* Implementar soluções de SBSE utilizando uma biblioteca profissional como a DEAP.
* Modelar diferentes problemas de software com representações adequadas (binária, permutação).
* Projetar funções de fitness que lidem com restrições do problema.
* Utilizar Engenharia de Prompt para gerar hipóteses e métricas para as funções de fitness.

### **Conteúdo Programático Detalhado:**
* **Aula 3: Formulação de Problemas e Representações**
    * **A Arte da Representação:**
        * **Binária:** Para problemas de seleção (ex: "quais features incluir?").
        * **Permutação:** Para problemas de ordenação (ex: "qual a melhor ordem para executar estes testes?").
        * **Numérica (Inteira/Real):** Para problemas de configuração (ex: "quais os melhores valores para estes parâmetros?").
    * **Projetando a Função de Fitness:**
        * Lidando com restrições: A abordagem da função de penalidade.
        * Normalização de múltiplos objetivos em uma única função ponderada (abordagem inicial).
* **Aula 4: Laboratório com a Biblioteca DEAP**
    * **Introdução ao DEAP:** O framework padrão da indústria para computação evolutiva em Python.
    * **Estrutura do DEAP:** `creator`, `toolbox`, `tools`, `algorithms`.
    * **Code-Along:** Reimplementação do Problema da Mochila com DEAP, mostrando a abstração e o poder da biblioteca.
    * **Aplicação:** Resolução de um problema de alocação de tarefas a desenvolvedores, visando minimizar o tempo total e balancear a carga de trabalho.
* **Aula 5: Laboratório de Sinergia com IA**
    * **Engenharia de Prompt para Definição de Fitness:**
        * **Técnica:** "Persona Prompting" ("Aja como um gerente de produto sênior...").
        * **Objetivo:** Dado um requisito de qualidade vago (ex: "o código deve ser mais manutenível"), usar um LLM para sugerir métricas concretas e quantificáveis (ex: Complexidade Ciclomática, Índice de Manutenibilidade, Coesão de Classes).
    * **Engenharia de Prompt para Geração de Heurísticas:**
        * **Técnica:** "Chain-of-Thought Prompting".
        * **Objetivo:** Pedir a um LLM para sugerir operadores de mutação ou crossover específicos para um problema (ex: "Para um problema de otimização de rotas, sugira um operador de mutação que seja mais inteligente do que uma simples troca aleatória de duas cidades").

## **Módulo 3: SBSE Aplicada à Engenharia de Software Tradicional (Aulas 6-8)**

### **Objetivo Geral:**
Aplicar as técnicas de SBSE para resolver dois dos problemas mais clássicos e custosos da engenharia de software: teste e refatoração. O objetivo é que os alunos desenvolvam soluções práticas que automatizem a geração de dados de teste e a melhoria de código legado, servindo como base técnica para o projeto final.

### **Objetivos Específicos:**
* Implementar um gerador de testes automatizado que busca maximizar a cobertura de código.
* Entender e quantificar o conceito de "dívida técnica" e "code smells".
* Desenvolver um otimizador que sugira a melhor sequência de refatorações para melhorar a qualidade de um software.
* Utilizar LLMs como um oráculo para sugerir possíveis refatorações.

### **Conteúdo Programático Detalhado:**
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

## **Módulo 4: SBSE para Sistemas de Inteligência Artificial (Aulas 9-12)**

### **Objetivo Geral:**
Explorar a fronteira da pesquisa em SBSE: a aplicação de técnicas de otimização para validar, testar e melhorar a qualidade de sistemas de Machine Learning e IA. O foco é mover o paradigma da SBSE de "código tradicional" para "sistemas inteligentes", introduzindo o domínio central do projeto final.

### **Objetivos Específicos:**
* Utilizar SBSE para realizar testes de justiça (fairness) em modelos de ML, buscando por vieses.
* Aplicar meta-heurísticas para otimização de hiperparâmetros.
* Modelar o problema de otimização de prompts como um problema de busca.
* Apresentar e detalhar a especificação do Projeto Final.

### **Conteúdo Programático Detalhado:**
* **Aulas 9-10: Teste de Justiça (Fairness Testing) em Modelos de ML**
    * **O Novo Paradigma de Teste:** Testando sistemas que aprendem com dados. O problema do "oráculo" e o não-determinismo.
    * **Viés e Discriminação em IA:** Como modelos podem perpetuar e amplificar preconceitos existentes nos dados.
    * **SBSE para Encontrar Viés:**
        * **Representação:** Um indivíduo é um perfil de entrada para o modelo (ex: um pedido de empréstimo).
        * **Função de Fitness:** Maximizar a probabilidade de o modelo dar resultados diferentes para dois indivíduos que só diferem em um atributo sensível (ex: gênero, etnia).
    * **Laboratório Prático:** Os alunos receberão um modelo de ML pré-treinado (ex: "aprova_credito.pkl"). A tarefa será construir um AG que gera perfis de clientes sintéticos para encontrar o cenário de maior discriminação que o modelo produz.
* **Aula 11: Otimização de Hiperparâmetros e Prompts**
    * **SBSE para Otimização de Hiperparâmetros:**
        * Alternativa a Grid Search e Random Search.
        * **Representação:** O cromossomo contém os valores dos hiperparâmetros (learning rate, nº de camadas, etc.).
        * **Fitness:** Acurácia do modelo no conjunto de validação.
    * **SBSE para Otimização de Prompts (Prompt Engineering):**
        * **Representação:** Um prompt como uma sequência de palavras ou tokens.
        * **Operadores:** Mutação (trocar palavra, usar sinônimo), Crossover (combinar partes de dois prompts).
        * **Fitness:** A qualidade da resposta do LLM, avaliada por outro LLM ou por regras heurísticas.
* **Aula 12: Apresentação e Discussão do Projeto Final**
    * Apresentação formal da especificação do projeto, cronograma e critérios de avaliação.
    * Sessão de Q&A para esclarecer dúvidas.
    * Formação dos grupos e brainstorming inicial de ideias para quem optar por problemas alternativos.

## **Módulo 5: Tópicos Avançados e Ética em SBSE (Aulas 13-14)**

### **Objetivo Geral:**
Apresentar técnicas avançadas de otimização, como a abordagem multi-objetivo, e promover uma reflexão crítica sobre as implicações éticas do uso de otimização automatizada em software, enriquecendo a análise que poderá ser feita no projeto final.

### **Objetivos Específicos:**
* Diferenciar otimização mono e multi-objetivo.
* Compreender os conceitos de Dominância de Pareto e Fronteira de Pareto.
* Implementar uma solução multi-objetivo usando a biblioteca Pymoo e o algoritmo NSGA-II.
* Analisar os riscos éticos da otimização e a Lei de Goodhart.

### **Conteúdo Programático Detalhado:**
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


## **Módulo 6: Período para Desenvolvimento e Entrega do Projeto Final (Aulas 15-16)**

### **Objetivo Geral:**
Oferecer um período focado para que os alunos possam consolidar e aplicar de forma autônoma todo o conhecimento adquirido, culminando na entrega de um projeto completo que demonstre maestria nas técnicas de SBSE e sua integração com IA.

### **Metodologia:**
Este período final do curso é dedicado exclusivamente ao desenvolvimento assíncrono do projeto. **Não haverá aulas expositivas, encontros síncronos ou apresentações formais.** A conclusão da disciplina se dá pela submissão do trabalho.

* **Desenvolvimento Autônomo:** Os alunos utilizarão o período correspondente às aulas finais para finalizar seus projetos de forma independente.
* **Suporte Assíncrono:** O professor estará disponível para dúvidas pontuais através dos canais de comunicação oficiais da disciplina (ex: email, fórum) durante este período.
* **Entrega Final:** A avaliação da disciplina é composta integralmente pela submissão do projeto final, que deve ser enviado por email até a data estipulada no documento de especificação do projeto.
* **Artefatos Obrigatórios:**
    1.  Um **Jupyter Notebook** (`.ipynb`) completo, bem documentado, com código limpo e células executadas para garantir a reprodutibilidade.
    2.  Um **vídeo de apresentação** (máximo 15 minutos), gravado de forma assíncrona, onde o aluno(a) ou grupo explica o problema, a solução, a análise dos resultados e as conclusões.
* **Ferramentas de Apoio:** Recomenda-se o uso de ferramentas como o **NotebookLM** para auxiliar na pesquisa, na criação do roteiro do vídeo e na documentação do projeto, demonstrando a aplicação de IA no próprio processo de desenvolvimento.
* **Avaliação e Feedback:** A nota será atribuída com base nos critérios detalhados no documento de especificação do projeto. O feedback detalhado será enviado individualmente pelo professor após o período de correção.