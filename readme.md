## Estágio - Target

## [Exercicio 1](ex1.py)
1)  Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...),
    escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.
```sh
    def fibonacci(n):
        a = 0
        b = 1
        sequencia_fibo = [a, b]  

        while b < n:
            a, b = b, a + b
            sequencia_fibo.append(b)

        return sequencia_fibo

    def x_fibonacci(n):
        if n < 0:
            return f"O número {n} é negativo e não pertence à sequência de Fibonacci."
        
        fib = fibonacci(n)

        if n in fib:
            return f"O número {n} pertence à sequência de Fibonacci."
        else:
            return f"O número {n} não pertence à sequência de Fibonacci."

    numero = int(input("Digite um número: "))
    resultado = x_fibonacci(numero)
    print(resultado)
```
## [Exercicio 2](ex2.py)
2) Escreva um programa que verifique, em uma string, a existência da letra ‘a’, seja maiúscula ou minúscula, além de informar a quantidade de vezes em que ela ocorre.
```sh
c_letras = 0

letras_a = 'aáàâãAÁÀÂÃ'

texto = input("Digite a palavra desejada: ")

for palavra in texto:
    if palavra in letras_a:
        c_letras += 1

if c_letras > 1:
    print(f"A palavra {texto} tem {c_letras} letras A's nela")
else:
    print(f"A palavra {texto} não tem nenhuma letra A nela")
```
## [Exercicio 3](ex3.py)
3) Observe o trecho de código abaixo: int INDICE = 12, SOMA = 0, K = 1; enquanto K < INDICE faça { K = K + 1; SOMA = SOMA + K; } imprimir(SOMA);
   Ao final do processamento, qual será o valor da variável SOMA?

   ## Resposta: 77

```sh
    ind = 12
    soma = 0
    k = 1
    while k < ind:
        k += 1
        soma += k

    print(soma) # resposta 77
```
## [Exercicio 4](ex4.py)
4) Descubra a lógica e complete o próximo elemento:

a) 1, 3, 5, 7, **R = 9**

b) 2, 4, 8, 16, 32, 64, **R = 128**

c) 0, 1, 4, 9, 16, 25, 36, **R = 49**

d) 4, 16, 36, 64, **R = 100**

e) 1, 1, 2, 3, 5, 8, **R = 13**

f) 2,10, 12, 16, 17, 18, 19, **R = 200 Duzentos**

## [Exercicio 5](ex5.py)

5)  Você está em uma sala com três interruptores, cada um conectado a uma lâmpada em salas diferentes. 
    Você não pode ver as lâmpadas da sala em que está, mas pode ligar e desligar os interruptores quantas vezes quiser.
    Seu objetivo é descobrir qual interruptor controla qual lâmpada.
    Como você faria para descobrir, usando apenas duas idas até uma das salas das lâmpadas, qual interruptor controla cada lâmpada?  

**Ligando o interruptor 1 por 9 minutos, desligando ele e depois ligando o interruptor 2. Chegando na primeira sala só tem como ou ter a lampada acessa resultando nessa sala sendo do interruptor 2 ou ela estar apagada, se a lampada estiver quente pertece ao interruptor 1 se não so sobra o interruptor 3 Na segunda sala é so repetir a mesma observação da primeira sala só vão sobrar duas opções**