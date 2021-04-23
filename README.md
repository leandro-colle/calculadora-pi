# Calculadora Pi
Programa que efetua o cálculo do Pi com multiprocessamento.

## Como foi desenvolvido?
Foram desenvolvidas duas versões do programa. Uma utilizando multiprocessos com fila de mensagem e outra utilizando uma lista de threads.

## Parâmetros do programa
Para execução do programa deve-se enviar o número de termos e o número de processos/threads que efetuarão o cálculo.

## Como iniciar o programa?
executar os seguintes comandos em um terminal:
- `python3 multiprocessing_pi_calculator.py <nTerms> <nProcess>`
- `python3 threading_pi_calculator.py <nTerms> <nThreads>`