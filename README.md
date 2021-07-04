# k-vezesDigito
### Objetivo do algoritmo: Faça um programa que verifica quantas vezes um dígito aparece em um determinado número de telefone (celular ou fixo). 
O algoritmo deverá receber dois números inteiros, o primeiro será o número que deve ser verificado e o segundo será o número do telefone. 

### Entrada
- Número inteiro X entre 0 e 9.
- String Y com 8 dígitos ou 9 dígitos. 

### Saída
- Quantidade de vezes que o primeiro número (X) aparece no segundo número (Y) ou string "entrada invalida".

### Observações
**Obs1.:** O número do telefone Y (fixo ou celular) não deve iniciar por 0 ou uma sequência de 0s, caso seja, informar ao usuário ‘entrada invalida’. Tratar outros casos inválidos conforme descrição de entrada do problema, nesse caso informar também ‘entrada invalida’.

**Obs2.:** Não manipular como listas e não usar métodos de contagem com o count().

### Exemplos
| Numero inteiro X | String Y | Saida |
| ------ | ------ | ------ |
| 1 | 656789110 | 2 |
| 1 | 23456789 | 0 |
| 0 | 00000000 | entrada invalida |
| 0 | 000000000 | entrada invalida |
| 0 | 0 | entrada invalida |
| 1 | 00000001 | entrada invalida |
| -1 | 12345678 | entrada invalida |
| 1 | 123 | entrada invalida |

### Instruções gerais
- Escreva seu código dentro do arquivo **exercicio.py**
- Escreva os casos de teste do algoritmo dentro do arquivo **casosDeTeste.py**
- Dentro do arquivo **exercicio.py** existe um código que resolve parcialmente o problema. Vocé deverá validar o que está escrito, realizando as modificações necessárias para a execução correta do algoritmo.
- Dentro do arquivo **casosDeTeste.py** existe um dicionário no formato: { "X-Y": "saida"}, onde X e Y são as entradas já descritas e devem ser separadas po hífen. Você deverá inserir seus casos de teste nele. Por exemplo, {"1-656781111" : "4"} significa que as entradas serão **X = 1**, **Y = 656781111** e a saida será **4**
- Após a codificação do algoritmo não esqueça de **commitar as mudanças**

