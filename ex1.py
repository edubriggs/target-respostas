"""
1)  Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...),
    escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.
"""

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