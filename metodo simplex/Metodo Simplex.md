# Método Simplex 

Passo a Passo do **método Simplex**, incluindo como montar e manipular a tabela Simplex

---

## 1. **Escreva o problema na forma padrão**

- Transforme a função objetivo para maximizar:
  ```
  Max Z = c₁x₁ + c₂x₂ + ... + cₙxₙ
  ```
- Escreva as restrições do tipo ≤:
  ```
  a₁₁x₁ + a₁₂x₂ + ... + a₁ₙxₙ ≤ b₁
  a₂₁x₁ + a₂₂x₂ + ... + a₂ₙxₙ ≤ b₂
  ...
  ```
- Todas as variáveis **xᵢ ≥ 0**.

---

## 2. **Adicione variáveis de folga**

- Para cada restrição, adicione uma variável de folga (s):
  ```
  a₁₁x₁ + ... + a₁ₙxₙ + s₁ = b₁
  ```
- As variáveis de folga também devem ser **≥ 0**.

---

## 3. **Monte a tabela Simplex inicial**

Monte uma tabela com:
- Colunas: todas as variáveis (originais + folga)
- Linhas: restrições e uma linha para a função objetivo (Z)
- Uma coluna adicional para os valores do lado direito das equações (termo independente)

Exemplo:

| Básica | x₁ | x₂ | s₁ | s₂ | Solução |
|--------|----|----|----|----|---------|
| s₁     | a₁₁| a₁₂|  1 |  0 |   b₁    |
| s₂     | a₂₁| a₂₂|  0 |  1 |   b₂    |
| Z      | -c₁| -c₂|  0 |  0 |    0    |

---

## 4. **Identifique a variável que entra na base**

- Observe a linha Z: escolha a variável de coeficiente negativo mais baixo. Esta é a que entra na base.

---

## 5. **Identifique a variável que sai da base**

- Para cada restrição, divida o termo independente pelo coeficiente positivo na coluna que vai entrar.
- O menor quociente positivo indica a linha da variável que vai sair da base.

---

## 6. **Efetue o pivoteamento**

- Identifique o pivô (interseção da linha da variável que sai e da coluna da variável que entra).
- Divida toda a linha do pivô por ele mesmo para que o pivô fique 1.
- Zere o restante da coluna do pivô realizando operações entre as linhas.

---

## 7. **Repita os passos 4 a 6**

- Continue até que a linha Z **não possua mais coeficientes negativos** (caso de maximização).
- Quando isso acontecer, atingiu-se a solução ótima.

---

## 8. **Leitura da solução**

- O valor das variáveis básicas está na coluna "Solução".
- Variáveis que não estão na base valem zero.
- O valor ótimo da função objetivo estará no final da linha Z, coluna solução.

---

## Exemplo Resumido

**Maximize**  
```
Z = 3x₁ + 2x₂
```
**Sujeito a**
```
x₁ + x₂ ≤ 4
x₁      ≤ 2
    x₂  ≤ 3
x₁, x₂ ≥ 0
```

1. Inclua folgas:
   ```
   x₁ + x₂ + s₁ = 4   
   x₁      + s₂ = 2   
        x₂ + s₃ = 3
   ```

2. Tabela inicial:

   
| Básica | x₁ | x₂ | s₁ | s₂ | s₃ | Sol |
|--------|----|----|----|----|----|-----|
| s₁     |  1 |  1 |  1 |  0 |  0 |  4  |
| s₂     |  1 |  0 |  0 |  1 |  0 |  2  |
| s₃     |  0 |  1 |  0 |  0 |  1 |  3  |
| Z      | -3 | -2 |  0 |  0 |  0 |  0  |

---

## Observações

- O método Simplex pode ser aplicado para problemas de **maximização** com restrições do tipo ≤ e variáveis ≥ 0.
- Para restrições de outros tipos ou variáveis livres, utilize transformações adequadas (adicionar variáveis artificiais, multiplicar por -1, etc).

---

## Fontes

- Winston, W.L. Pesquisa Operacional: Aplicações e Algoritmos.
- Hillier, F.S.; Lieberman, G.J. Introdução à Pesquisa Operacional.
