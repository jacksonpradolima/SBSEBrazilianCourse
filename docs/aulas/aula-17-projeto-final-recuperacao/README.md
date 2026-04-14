---
titulo: "Projeto Final de Recuperação - SBSE Aplicada a um Problema Concreto"
aula_numero: 17
carga_horaria: "Assíncrono (prazo definido pelo professor)"
foco_principal: "Permitir que o aluno demonstre, de forma individual e guiada, domínio prático dos conceitos fundamentais de SBSE ao resolver um dos três problemas pré-definidos, com nota máxima de 7,0."
metodologia: "Desenvolvimento Autônomo com Template Guiado"
tipo_aula: "Projeto de Recuperação Individual"
objetivos:
  - "Aplicar de forma autônoma os três componentes essenciais de SBSE (representação, fitness, algoritmo) em um problema concreto."
  - "Produzir código Python funcional e bem documentado usando DEAP ou Pymoo."
  - "Comparar a solução evolutiva com um baseline aleatório e interpretar os resultados."
pre_requisitos:
  - "Ter cursado a disciplina (Módulos 1-5)."
  - "Noções de Python, Jupyter Notebooks e manipulação de dados com pandas/numpy."
---

# Projeto Final de Recuperação — SBSE Aplicada a um Problema Concreto

## Seção 1: Abertura e Engajamento

### 1.1. Para Quem é Esta Oportunidade?

Esta avaliação de recuperação é uma segunda chance para qualquer aluno que deseje melhorar sua nota no Projeto Final da disciplina. Ela foi projetada para ser mais **focada e guiada** do que o projeto original, com três problemas pré-definidos e um template de notebook estruturado — mas sem abrir mão do rigor técnico.

A diferença fundamental em relação ao projeto original é simples: aqui você escolhe **um caminho já mapeado** em vez de abrir a própria trilha. O destino — demonstrar domínio de SBSE — é o mesmo.

> **Regra de ouro:** A nota desta recuperação **substitui** a nota do Projeto Final original somente se for **superior**. A nota máxima alcançável nesta avaliação é **7,0 pontos**.

### 1.2. Objetivos desta Avaliação

Ao final deste projeto, você será capaz de:

- **Formular um problema de SBSE** a partir de um enunciado dado, identificando representação, fitness e operadores adequados.
- **Implementar um algoritmo evolutivo** funcional com DEAP ou Pymoo para resolver o problema escolhido.
- **Validar experimentalmente** sua solução comparando-a com uma linha de base aleatória (Random Search).
- **Comunicar resultados** de forma técnica e objetiva em notebook e vídeo curto.

---

## Seção 2: Regras, Formato de Entrega e Rubrica

### 2.1. Regras Gerais

| Critério | Valor |
| :--- | :--- |
| **Modalidade** | **Individual** (trabalhos em grupo não serão aceitos) |
| **Nota máxima** | **7,0 pontos** |
| **Nota do projeto original** | Mantida se for superior à nota desta recuperação |
| **Elegibilidade** | Qualquer aluno matriculado na disciplina |

### 2.2. O Arquivo de Metadados (`project_metadata.json`)

Todo projeto deve conter obrigatoriamente um arquivo `project_metadata.json` na raiz da pasta. Ele serve como "identidade" do projeto para avaliação.

```json
{
  "titulo_projeto": "Recuperação — Problema [A/B/C]: Título Descritivo",
  "aluno": "Seu Nome Completo",
  "problema_escolhido": "A | B | C",
  "tecnica_sbse": "ex: Algoritmo Genético (tournSel + cxTwoPoint + mutUniformInt)",
  "resumo_executivo": "Uma descrição concisa de até 3 linhas sobre o problema e a abordagem adotada.",
  "metricas_chave": {
    "metrica_principal": "ex: 87.5% de cobertura de ramos",
    "melhoria_vs_baseline": "ex: +34 p.p. acima do Random Search com 100 avaliações"
  },
  "link_video_backup": "Cole aqui o link (YouTube Não-Listado ou Drive Público)"
}
```

### 2.3. Estrutura do ZIP de Entrega

```text
/ (Raiz do ZIP)
├── project_metadata.json         ← Obrigatório
├── README.md                     ← Instruções de execução e dependências
├── requirements.txt              ← Bibliotecas Python utilizadas
├── notebook_recuperacao.ipynb    ← Notebook principal (baseado no template)
├── video_apresentacao.mp4        ← Obrigatório: 3-5 min, máx. 50 MB, codec H.264
└── /results                      ← Gráficos de convergência + CSV de métricas
```

**Formato de envio por email:**
- **Para:** `jacksonpradolima@gmail.com`
- **Assunto:** `[SBSE-Recuperacao] SeuNome - Problema [A/B/C]`
- **Prazo:** Conforme comunicado pelo professor

### 2.4. Rubrica de Avaliação

| # | Critério | Peso | O que será avaliado |
| :---: | :--- | :---: | :--- |
| 1 | **Formulação do Problema** | 1,5 | A representação codifica o espaço de busca corretamente? A função de fitness mede o objetivo desejado? Os operadores são coerentes com a representação? |
| 2 | **Implementação do Algoritmo** | 2,0 | O código roda sem erros? Os parâmetros do AG/DE são justificados? Os operadores genéticos foram aplicados corretamente? |
| 3 | **Análise Comparativa (vs. Baseline)** | 1,5 | Existe comparação justa com Random Search com o mesmo orçamento de avaliações? O gráfico de convergência foi incluído? Os resultados são reproduzíveis (seed fixa)? |
| 4 | **Qualidade do Notebook** | 1,0 | O notebook conta uma história coerente? O código segue PEP 8? Há comentários explicando decisões-chave? O notebook executa do início ao fim? |
| 5 | **Vídeo de Apresentação** | 1,0 | O aluno demonstra entendimento do problema? O sistema é mostrado funcionando? A comunicação é clara? |
| | **BÔNUS: Integração com LLM** | +0,5 | LLM usado de forma relevante e não cosmética (máx. 7,0 — o bônus não ultrapassa esse teto) |

---

## Seção 3: Os Três Problemas Disponíveis

Escolha **exatamente um** dos problemas abaixo. Cada um está mapeado para um módulo do curso e inclui todos os dados/modelos necessários (disponíveis no notebook template `workshop.ipynb`).

---

### Problema A — Teste Baseado em Busca: Maximizando Cobertura de Ramos

**Módulo de referência:** 3 (Aulas 6–7) | **Complexidade:** ★★★☆☆

#### Contexto

Você recebeu a seguinte função Python que classifica operações financeiras:

```python
def classificar_operacao(valor: float, tipo: int, risco: int) -> str:
    """
    Classifica uma operação financeira.
    valor: valor em reais (0 a 100000)
    tipo:  0=transferência, 1=saque, 2=investimento
    risco: 0=baixo, 1=médio, 2=alto
    """
    if valor <= 0:
        return "INVALIDA"
    
    if tipo == 1:  # saque
        if valor > 10000:
            if risco >= 2:
                return "BLOQUEADO"
            else:
                return "APROVADO_MONITORADO"
        else:
            return "APROVADO"
    elif tipo == 2:  # investimento
        if risco == 0 and valor >= 5000:
            return "PERFIL_CONSERVADOR_OK"
        elif risco >= 1:
            return "REQUER_ANALISE"
        else:
            return "APROVADO"
    else:  # transferência
        if valor > 50000:
            return "REQUER_AUTORIZACAO"
        return "APROVADO"
```

Esta função possui **10 ramos** (branches). Um testador manual conseguiu cobrir apenas 4 deles. Sua tarefa é usar um Algoritmo Genético para **gerar automaticamente casos de teste que maximizem a cobertura de ramos**.

#### Formulação Como Problema de SBSE

| Componente | Definição |
| :--- | :--- |
| **Representação** | Cromossomo = `[valor, tipo, risco]` — vetor de 3 genes inteiros |
| **Espaço de Busca** | `valor ∈ [0, 100001]`, `tipo ∈ {0, 1, 2}`, `risco ∈ {0, 1, 2}` |
| **Fitness** | Número de ramos únicos cobertos pela **população inteira** após execução instrumentada |
| **Operadores** | `mutUniformInt`, `cxUniform`, `selTournament` |
| **Critério de parada** | 100 gerações ou cobertura = 100% |

#### Requisitos Técnicos

- [ ] Instrumente a função com `coverage.py` ou contagem manual de ramos visitados
- [ ] Implemente o AG com DEAP (`toolbox.register`)
- [ ] Mostre a evolução da cobertura geração a geração (gráfico de convergência)
- [ ] Compare com Random Search usando o mesmo número total de avaliações ($n_{pop} \times n_{gen}$)
- [ ] Reporte a cobertura final: `X/10 ramos (Y%)`

---

### Problema B — Fairness Testing: Encontrando Discriminação em Modelo de Crédito

**Módulo de referência:** 4 (Aulas 9–10) | **Complexidade:** ★★★☆☆

#### Contexto

O notebook template fornece um modelo de aprovação de crédito pré-treinado (`modelo_credito.pkl`), treinado com um dataset histórico de um banco fictício. Auditores suspeitam que o modelo trata de forma diferente clientes com os mesmos atributos financeiros, mas com **gênero** diferente.

Sua tarefa é usar um Algoritmo Genético para **encontrar o par de perfis de clientes que maximiza a diferença de probabilidade de aprovação**, onde os dois perfis são idênticos exceto pelo atributo `genero`.

#### Formulação Como Problema de SBSE

| Componente | Definição |
| :--- | :--- |
| **Representação** | Cromossomo = `[idade, renda_mensal, divida_total, score_credito, tempo_emprego]` — vetor de 5 genes reais |
| **Espaço de Busca** | Ranges definidos no notebook (baseados em dados reais do Brasil) |
| **Fitness** | $f = \|P(\text{aprovado} \mid \text{perfil, genero=M}) - P(\text{aprovado} \mid \text{perfil, genero=F})\|$ |
| **Operadores** | `cxBlend`, `mutGaussian`, `selTournament` |
| **Critério de parada** | 200 gerações ou $f \geq 0.5$ (50 p.p. de diferença) |

#### Requisitos Técnicos

- [ ] Carregue o modelo fornecido no template e entenda seus atributos de entrada
- [ ] Implemente o AG para maximizar a disparidade de predição
- [ ] Mostre os **5 perfis mais discriminatórios** encontrados (tabela)
- [ ] Compare com Random Search usando o mesmo orçamento
- [ ] Discuta: "Em que faixa de renda o modelo é mais discriminatório?"

#### Questão Ética Obrigatória (na conclusão do notebook)

> Você encontrou viés de verdade ou o modelo aprendeu uma correlação estatística legítima? Justifique sua resposta em pelo menos 3 parágrafos.

---

### Problema C — Otimização de Hiperparâmetros com Evolução Diferencial

**Módulo de referência:** 4 (Aula 11) | **Complexidade:** ★★★★☆

#### Contexto

Você recebeu um dataset de diagnóstico médico (Cancer Wisconsin, disponível no template) e 48 horas para entregar o melhor classificador possível para produção. Grid Search com os hiperparâmetros fornecidos levou 20 minutos e atingiu 94,7% de acurácia. Sua missão é superar esse resultado usando **Evolução Diferencial** para otimizar os hiperparâmetros de um `RandomForestClassifier`.

#### Formulação Como Problema de SBSE

| Componente | Definição |
| :--- | :--- |
| **Representação** | Cromossomo = `[n_estimators, max_depth, min_samples_split, min_samples_leaf, max_features]` |
| **Espaço de Busca** | Ranges definidos no notebook (combinando inteiros e reais) |
| **Fitness** | Acurácia média em 5-fold cross-validation no conjunto de treino (negada: DEAP minimiza) |
| **Algoritmo** | Evolução Diferencial (`eaSimple` com `mutDE`, `cxBinomial`) via DEAP **ou** NSGA-II via Pymoo (bônus: bi-objetivo acurácia vs. tempo de inferência) |
| **Critério de parada** | 50 gerações ou acurácia ≥ 97% |

#### Requisitos Técnicos

- [ ] Implemente a avaliação de fitness usando cross-validation (atenção à seed para reprodutibilidade)
- [ ] Compare com Grid Search (fornecido no template) e Random Search usando o mesmo número de avaliações
- [ ] Mostre convergência: melhor fitness por geração
- [ ] Avalie o modelo otimizado no conjunto de **teste** (conjunto separado desde o início — sem data leakage)
- [ ] Reporte: accuracy, F1-score, tempo de treinamento

**Bônus (+0,5 aplicado à rubrica do critério 1):** Formule como problema bi-objetivo usando NSGA-II do Pymoo, otimizando simultaneamente acurácia ($\uparrow$) e tempo de inferência ($\downarrow$). Mostre a frente de Pareto.

---

## Seção 4: Guia de Implementação e Boas Práticas

### 4.1. Estrutura Obrigatória do Notebook

Seu notebook deve seguir **exatamente** estas seções (células Markdown com títulos `##`):

```
## 1. Identificação
## 2. Problema: Descrição e Justificativa
## 3. Formulação como Problema de SBSE
## 4. Implementação
   ### 4.1. Configuração do Ambiente
   ### 4.2. Representação e Operadores
   ### 4.3. Função de Fitness
   ### 4.4. Loop Evolutivo
## 5. Baseline: Random Search
## 6. Resultados e Comparação
   ### 6.1. Gráfico de Convergência
   ### 6.2. Tabela Comparativa (AG vs. Random)
## 7. Conclusão e Análise Crítica
```

### 4.2. Checklist de Qualidade Antes de Entregar

**Código:**
- [ ] Seeds fixas em todas as fontes de aleatoriedade (`random.seed`, `np.random.seed`)
- [ ] Código segue PEP 8 (use `flake8` ou o linter do VS Code)
- [ ] Funções com docstrings mínimas (1 linha descrevendo o que faz)
- [ ] Nenhum `print` de debug remanescente
- [ ] Notebook executa **do início ao fim sem erros** em ambiente limpo (`Kernel > Restart & Run All`)

**Experimento:**
- [ ] Baseline Random Search com **exatamente** o mesmo orçamento de avaliações do AG
- [ ] Gráfico de convergência com eixo X = número de avaliações (não de gerações)
- [ ] CSV com resultados salvo em `/results/metricas_finais.csv`

**Entregáveis:**
- [ ] `project_metadata.json` preenchido corretamente
- [ ] Vídeo com duração entre 3 e 5 minutos
- [ ] Vídeo menor que 50 MB (use HandBrake para comprimir se necessário)
- [ ] Link de backup do vídeo preenchido no JSON

### 4.3. Erros Comuns e Como Evitá-los

| Erro | Por quê acontece | Como evitar |
| :--- | :--- | :--- |
| Fitness retorna valor estático | Função de avaliação não depende do indivíduo passado como parâmetro | Garanta que o cromossomo é usado de fato na avaliação |
| Data leakage no Problema C | Escala/normaliza com statistics do conjunto de teste | Fit do scaler apenas no treino, transform em ambos |
| Comparação injusta com baseline | Random Search usa mais avaliações que o AG | Iguale o orçamento: $n_{pop} \times n_{gen}$ avaliações para ambos |
| Notebook não reprodutível | Seeds não fixadas antes de criar `toolbox` | `random.seed(42); np.random.seed(42)` no início da célula de setup |

---

## Seção 5: Síntese e Critérios de Excelência

### 5.1. O que Diferencia uma Nota 7,0 de uma Nota 5,0

| Nota 5,0 (suficiente) | Nota 7,0 (excelente) |
| :--- | :--- |
| Código roda sem erros | Código roda **e** está bem documentado |
| AG implementado corretamente | AG com justificativa de escolha de parâmetros |
| Gráfico de convergência presente | Gráfico mostra tanto AG quanto baseline com desvio padrão (múltiplas runs) |
| Conclusão genérica | Conclusão responde perguntas específicas levantadas no problema |
| Vídeo mostra o código | Vídeo demonstra o sistema rodando e interpreta resultados |

### 5.2. Suporte Disponível

Para dúvidas técnicas durante o desenvolvimento:

- **Email:** `jacksonpradolima@gmail.com`
- **Assunto:** `[SBSE-Recuperacao-Duvida] Problema [A/B/C] - Sua dúvida`
- **Prazo de resposta:** Até 48 horas em dias úteis
- **Tipo de dúvida aceita:** Interpretação do enunciado, dúvidas sobre DEAP/Pymoo, debugging de erros não-triviais
- **Tipo de dúvida não aceita:** Resolver o problema pelo aluno, revisar código antes da entrega

### 5.3. Recursos de Apoio

- **Documentação DEAP:** [deap.readthedocs.io](https://deap.readthedocs.io)
- **Documentação Pymoo:** [pymoo.org](https://pymoo.org)
- **Aulas de referência:** README das Aulas 2, 4, 7, 9, 10 e 11 deste repositório
- **Notebooks de referência:** `workshop.ipynb` das aulas correspondentes ao problema escolhido
