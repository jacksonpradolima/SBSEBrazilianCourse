## Aula 17: Projeto Final de Recuperação

**Carga Horária:** Trabalho assíncrono (prazo a definir pelo professor)

**Tópicos:**
- Aplicação prática de SBSE em um dos três problemas pré-definidos
- Formulação do problema como instância de busca (representação + fitness)
- Implementação de algoritmo de otimização com DEAP ou Pymoo
- Análise experimental comparativa com linha de base (baseline aleatório)
- Documentação técnica e apresentação em vídeo curto

**Objetivos de Aprendizagem:**
- Aplicar de forma autônoma os conceitos fundamentais de SBSE (representação, fitness, seleção, crossover, mutação)
- Implementar corretamente um algoritmo evolutivo usando as bibliotecas do curso para resolver um problema concreto
- Analisar e interpretar os resultados da otimização de forma crítica e comparativa

**Metodologia:** Desenvolvimento autônomo a partir de template guiado (notebook estruturado)

**Tipo de Aula:** Projeto de Recuperação Individual

**Pré-requisitos:**
- Ter cursado a disciplina e entregado (ou tentado entregar) o Projeto Final original
- Conhecimento dos módulos 1 a 5 da disciplina
- Familiaridade com Python, DEAP e Jupyter Notebooks

---

## Regras e Elegibilidade

| Critério | Valor |
| :--- | :--- |
| **Quem pode fazer** | Qualquer aluno matriculado na disciplina |
| **Objetivo** | Substituir ou melhorar a nota do Projeto Final original |
| **Nota Máxima** | **7,0 pontos** (independente da qualidade da entrega) |
| **Trabalho** | **Individual** (grupos não são permitidos) |
| **Prazo** | Conforme comunicado pelo professor após as Aulas 15-16 |

> **Atenção:** A nota da recuperação **substitui** a nota do Projeto Final original caso seja superior. Se a nota da recuperação for inferior à nota original, a nota original é mantida. Nota máxima possível: **7,0**.

---

## Os Três Problemas Disponíveis

O aluno deve escolher **exatamente um** dos três problemas abaixo:

### Problema A — Teste Baseado em Busca (SBST)
**Tema:** Maximizar cobertura de ramos em uma função Python fornecida  
**Base curricular:** Módulos 1, 2 e 3 (Aulas 1-7)  
**Técnica obrigatória:** Algoritmo Genético com DEAP  
**Complexidade:** ★★★☆☆

### Problema B — Fairness Testing em Modelos de ML
**Tema:** Encontrar instâncias de discriminação em modelo de crédito pré-treinado  
**Base curricular:** Módulo 4 (Aulas 9-10)  
**Técnica obrigatória:** Algoritmo Genético com DEAP  
**Complexidade:** ★★★☆☆

### Problema C — Otimização de Hiperparâmetros
**Tema:** Otimizar hiperparâmetros de classificador via evolução diferencial  
**Base curricular:** Módulo 4 (Aula 11)  
**Técnica obrigatória:** Evolução Diferencial (DEAP) ou NSGA-II (Pymoo)  
**Complexidade:** ★★★★☆

---

## Entregáveis Obrigatórios

| # | Entregável | Detalhe |
| :--- | :--- | :--- |
| 1 | `project_metadata.json` | Preenchido conforme template |
| 2 | `notebook_recuperacao.ipynb` | Notebook baseado no template, executado sem erros |
| 3 | `requirements.txt` | Dependências listadas |
| 4 | `video_apresentacao.mp4` | 3 a 5 minutos, máximo 50 MB |
| 5 | `/results/` | Gráficos de convergência e CSV com métricas finais |

**Formato de entrega:** Arquivo `.zip` único enviado por email com assunto:  
`[SBSE-Recuperacao] [SeuNome] - Problema [A/B/C]`

---

## Rubrica de Avaliação (Total: 7,0 pontos)

| Critério | Peso | Descrição |
| :--- | :---: | :--- |
| Formulação do problema (representação + fitness) | 1,5 | A codificação está correta e a fitness avalia o que se deseja? |
| Implementação correta do algoritmo | 2,0 | O AG/DE roda sem erros e os operadores estão adequados ao problema? |
| Análise comparativa com baseline aleatório | 1,5 | Existe comparação justa com Random Search? Há gráfico de convergência? |
| Qualidade do notebook (narrativa + código limpo) | 1,0 | O notebook conta uma história? O código segue PEP 8 com comentários? |
| Vídeo de apresentação | 1,0 | O aluno demonstra entendimento e mostra o sistema funcionando? |
| **Bônus: integração com LLM** | +0,5 | LLM usado de forma relevante (geração de indivíduos, avaliação de fitness, análise de resultados) — não conta para além de 7,0 |

---

## Contato e Suporte

- **Email:** `jacksonpradolima@gmail.com`
- **Assunto para dúvidas:** `[SBSE-Recuperacao-Duvida] Sua dúvida aqui`
- **Prazo de resposta:** Até 48 horas em dias úteis
