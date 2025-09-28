# Módulo 4: SBSE para Sistemas de Inteligência Artificial (Aulas 9-12)

## Objetivo Geral
Explorar a fronteira da pesquisa em SBSE: a aplicação de técnicas de otimização para validar, testar e melhorar a qualidade de sistemas de Machine Learning e IA. O foco é mover o paradigma da SBSE de "código tradicional" para "sistemas inteligentes", introduzindo o domínio central do projeto final.

## Objetivos Específicos
* Utilizar SBSE para realizar testes de justiça (fairness) em modelos de ML, buscando por vieses.
* Aplicar meta-heurísticas para otimização de hiperparâmetros.
* Modelar o problema de otimização de prompts como um problema de busca.
* Apresentar e detalhar a especificação do Projeto Final.

## Conteúdo Programático Detalhado

### Aulas 9-10: Teste de Justiça (Fairness Testing) em Modelos de ML
* **O Novo Paradigma de Teste:** Testando sistemas que aprendem com dados. O problema do "oráculo" e o não-determinismo.
* **Viés e Discriminação em IA:** Como modelos podem perpetuar e amplificar preconceitos existentes nos dados.
* **SBSE para Encontrar Viés:**
    * **Representação:** Um indivíduo é um perfil de entrada para o modelo (ex: um pedido de empréstimo).
    * **Função de Fitness:** Maximizar a probabilidade de o modelo dar resultados diferentes para dois indivíduos que só diferem em um atributo sensível (ex: gênero, etnia).
* **Laboratório Prático:** Os alunos receberão um modelo de ML pré-treinado (ex: "aprova_credito.pkl"). A tarefa será construir um AG que gera perfis de clientes sintéticos para encontrar o cenário de maior discriminação que o modelo produz.

### Aula 11: Otimização de Hiperparâmetros e Prompts
* **SBSE para Otimização de Hiperparâmetros:**
    * Alternativa a Grid Search e Random Search.
    * **Representação:** O cromossomo contém os valores dos hiperparâmetros (learning rate, nº de camadas, etc.).
    * **Fitness:** Acurácia do modelo no conjunto de validação.
* **SBSE para Otimização de Prompts (Prompt Engineering):**
    * **Representação:** Um prompt como uma sequência de palavras ou tokens.
    * **Operadores:** Mutação (trocar palavra, usar sinônimo), Crossover (combinar partes de dois prompts).
    * **Fitness:** A qualidade da resposta do LLM, avaliada por outro LLM ou por regras heurísticas.

### Aula 12: Apresentação e Discussão do Projeto Final
* Apresentação formal da especificação do projeto, cronograma e critérios de avaliação.
* Sessão de Q&A para esclarecer dúvidas.
* Formação dos grupos e brainstorming inicial de ideias para quem optar por problemas alternativos.