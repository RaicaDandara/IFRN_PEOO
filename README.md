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
Utilizando o módulo no python "datetime" podemos trabalhar com datas, horas e intervalos de tempo. Mas primeiro é necessário que ele seja importado no início do código com o comando "import datetime". Dentro dele existem algumas classes disponíveis, como:
- date –> representa uma data com informações de ano, mês e dia, ou seja, é como o calendário. Ele te diz a data exata, por exemplo, "1º de junho de 2023" = '2023-06-01'
    - Exemplo em código: <br>
        import datetime
<br>
        '''# Criando uma data'''
        data_exemplo = datetime.date(2023, 6, 1)
<br>
        '''# Imprimindo a data'''
        print("Data:", data_exemplo)
- time –> representa um horário com dados de horas, minutos, segundos e microssegundos, ou seja, é como o relógio. O computador pode te dizer que são "09:30:15", ou seja, 9 horas, 30 minutos e 15 segundos.
- datetime –> é uma combinação dos tipos date e time. Portanto, este é um jeito de juntar o calendário (data) e o relógio (hora) em uma coisa só. Exemplo: 2023-06-01 09:30:15 significa que é 1º de junho de 2023 às 9 horas, 30 minutos e 15 segundos.
- timedelta –> intervalo (ou período) de tempo com informações até microssegundos, dessa forma, ele é, obviamente, usado para contar o tempo que passou ou que vai passar.
