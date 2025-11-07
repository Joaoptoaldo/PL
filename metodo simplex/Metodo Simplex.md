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

| Base   | x₁ | x₂ | f₁ | f₂ | Solução |
|--------|----|----|----|----|---------|
| f₁     | a₁₁| a₁₂|  1 |  0 |   b₁    |
| f₂     | a₂₁| a₂₂|  0 |  1 |   b₂    |
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
   x₁ + x₂ + f₁ = 4   
   x₁      + f₂ = 2   
        x₂ + f₃ = 3
   ```

2. Tabela inicial:
   
   
| Base   | x₁ | x₂ | f₁ | f₂ | f₃ | Sol |
|--------|----|----|----|----|----|-----|
| f₁     |  1 |  1 |  1 |  0 |  0 |  4  |
| f₂     |  1 |  0 |  0 |  1 |  0 |  2  |
| f₃     |  0 |  1 |  0 |  0 |  1 |  3  |
| Z      | -3 | -2 |  0 |  0 |  0 |  0  |


3. Olhe os coeficientes negativos na linha Z.
   O mais negativo é o -3 (coluna x₁).
   x₁ entra na base.


| Base   | x₁ | x₂ | f₁ | f₂ | f₃ | Sol |
|--------|----|----|----|----|----|-----|
| f₁     |  1 |  1 |  1 |  0 |  0 |  4  |
| f₂     |  1 |  0 |  0 |  1 |  0 |  2  |
| f₃     |  0 |  1 |  0 |  0 |  1 |  3  |
| Z      | -3 | -2 |  0 |  0 |  0 |  0  |

                

4. Divida os valores da coluna Sol pelo coef. de x₁ nas restrições:

    s₁: 4 / 1 = 4
    s₂: 2 / 1 = 2
   
f₃: 3 / 0 = ∞ (ignora, pois não pode dividir por zero)
Menor quociente positivo é 2 (f₂).
s₂ sai da base.


| Base   | x₁ | x₂ | f₁ | f₂ | f₃ | Sol |
|--------|----|----|----|----|----|-----|
| f₁     |  1 |  1 |  1 |  0 |  0 |  4  |
| f₂     |  1 |  0 |  0 |  1 |  0 |  2  | <-
| f₃     |  0 |  1 |  0 |  0 |  1 |  3  |
| Z      | -3 | -2 |  0 |  0 |  0 |  0  |


4. Ajuste a linha de f₂ para que o coeficiente de x₁ vire 1 (dividindo pelo mesmo valor pivo):

  - Linha pivô: divide toda f₂ por 1 (já está assim).
  - Zere os outros valores de x₁ usando operações entre linhas, usando a formula:
    
        No caso do exemplo:
    
        Novas linhas: linha antiga - Coeficiente pivo(1) x nova linha pivo(x2)
  


| Base   | x₁ | x₂ | f₁ | f₂ | f₃ | Sol |
|--------|----|----|----|----|----|-----|
| f₁     |  0 |  1 |  1 | -1 |  0 |  2  |  
| x₂     |  1 |  0 |  0 |  1 |  0 |  2  |  
| f₃     |  0 |  1 |  0 |  0 |  1 |  3  |  
| Z      | -3 | -2 |  0 |  0 |  0 |  0  |


- x2: Coluna ajustada
- f1: Nova linha pivo
- f3: Permance igual pois o coeficiente já está zerado


5. Na linha Z, o coeficiente negativo é -2 (x₂).
   x₂ entra na base.

   Divida Sol por coef. de x₂:

    s₁: 2 / 1 = 2
    x₁: 2 / 0 = ∞ (ignora)
    s₃: 3 / 1 = 3
   
  Menor quociente: 2 (s₁ sai da base).

7. Segundo Pivoteamento (x₂ entra, s₁ sai)

   
---

## Observações

- O método Simplex pode ser aplicado para problemas de **maximização** com restrições do tipo ≤ e variáveis ≥ 0.
- Para restrições de outros tipos ou variáveis livres, utilize transformações adequadas (adicionar variáveis artificiais, multiplicar por -1, etc).


