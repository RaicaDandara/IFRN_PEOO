# Repositório da disciplina de Programação Estruturada e Orientada a Objetos (PEOO)

## Conteúdos Estudados:
- Entidade, Classificação e Abstração
- Encapsulamento
- Construtores
- ToString
- Listas
- Datas e Intervalos
- Enumerações
- Classes e Heranças
- Dicionários

## Encapsulamento
## Construtores
## ToString
## Listas
## Datas e Intervalos
### Conceitos Básicos
Utilizando o módulo no python "datetime" podemos trabalhar com datas, horas e intervalos de tempo. Mas primeiro é necessário que ele seja importado no início do código com o comando "import datetime". Dentro dele existem algumas classes disponíveis, como:
- .date –> representa uma data com informações de ano, mês e dia, ou seja, é como o calendário. Ele te diz a data exata, por exemplo, "1º de junho de 2023" = '2023-06-01'
    - Exemplo em código:
> No código: <br> data_exemplo = datetime.date(2023, 6, 1) <br> Saída: <br> Data: 2023-06-01
        
- .time –> representa um horário com dados de horas, minutos, segundos e microssegundos, ou seja, é como o relógio. O computador pode te dizer que são "09:30:15", ou seja, 9 horas, 30 minutos e 15 segundos.
    - Exemplo em código:
> No código: <br> horario_exemplo = datetime.time(9, 30, 15) <br> Saída: <br> Hora: 09:30:15
 
- .datetime –> é uma combinação dos tipos date e time. Portanto, este é um jeito de juntar o calendário (data) e o relógio (hora) em uma coisa só. Exemplo: 2023-06-01 09:30:15 significa que é 1º de junho de 2023 às 9 horas, 30 minutos e 15 segundos.
    - Exemplo em código:
> No código: <br> datetime_exemplo = datetime.datetime(2023, 6, 1, 9, 30, 15) <br> Saída: <br> Data e Hora: 2023-06-01 09:30:15
 
- .timedelta –> intervalo (ou período) de tempo com informações até microssegundos, dessa forma, ele é, obviamente, usado para contar o tempo que passou ou que vai passar.
    - Exemplo em código:
> No código: <br> intervalo_tempo = datetime.timedelta(days=10, hours=5) <br> Saída: <br> Intervalo de Tempo: 10 days, 5:00:00

- .now -> utilizado para mostrar conforme a sua escolha a data, hora ou ambos do momento. Exemplo: 'agora = datetime.datetime.now()' mostra '2023-06-22 10:49:26.165175'. Altera-se a forma a qual aparece mudando o formado do primeiro elemento após o ponto "."
 
### Operações com datetime e timedelta
> import datetime  <br> <br> # Data inicial <br> data_inicial = datetime.datetime(2023, 6, 1, 9, 30, 15) <br> <br># Intervalo de tempo <br> intervalo = datetime.timedelta(days=5, hours=3) <br> <br> # Somando intervalo à data inicial <br> nova_data = data_inicial + intervalo <br> <br> # Imprimindo nova data e diferença de tempo  <br> print("Data Inicial:", data_inicial) <br> print("Nova Data (após adicionar intervalo):", nova_data) <br> print("Diferença entre as datas:", nova_data - data_inicial) <br> <br> Saída: <br> Data Inicial: 2023-06-01 09:30:15 <br> Nova Data (após adicionar intervalo): 2023-06-06 12:30:15 <br> Diferença entre as datas: 5 days, 3:00:00
