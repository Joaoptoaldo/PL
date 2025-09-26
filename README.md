# Programação Linear (PL)

Repositório dedicado a **Programação Linear**, uma técnica de otimização matemática usada para **maximizar ou minimizar objetivos** respeitando certas restrições.

---

## Para que serve

A Programação Linear é aplicada em situações como:
- Maximizar lucros de produção
- Minimizar custos de transporte
- Alocação eficiente de recursos
- Planejamento de projetos e logística

---

## Exemplo simples em Python

```python
# Instalar a biblioteca PuLP: pip install pulp
from pulp import LpMaximize, LpProblem, LpVariable, lpSum

# Criando o problema de maximização
model = LpProblem(name="exemplo-pl", sense=LpMaximize)

# Variáveis de decisão
x = LpVariable(name="canetas", lowBound=0)
y = LpVariable(name="cadernos", lowBound=0)

# Função objetivo: maximizar lucro
model += 2*x + 3*y, "Lucro_Total"

# Restrições
model += 1*x + 2*y <= 100, "Horas_Trabalho"

# Resolver o problema
model.solve()

print(f"Produzir {x.value()} canetas e {y.value()} cadernos")
print(f"Lucro máximo: {model.objective.value()}")
