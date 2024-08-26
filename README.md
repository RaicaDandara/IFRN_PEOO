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

## Enumerções
## Classes e Heranças
## Dicionários
### Conceitos Básicos
O dicionário é responsável por guardar informações através de chaves e valores. Podendo, portanto, também funcionar como uma grande lista de perguntas e respostas se necessário ou somente como um acervo de informações, dependerá do comando dado a você. Exemplo:
>  Você quer guardar as informações sobre as capitais dos estados brasileiros com um dicionário <br> 
    - Então, você cria o seguinte código: <br> 
> capital = {"RN": "Natal", "PB": "João Pessoa", "PE": "Recife"} <br> 
    - Portanto, nele as chaves são: "RN", "PB" e "PE". Enquanto os valores são: "Natal", "João Pessoa" e "Recife". <br>
     <br> 
    - Também é possível fazer "perguntas" a ele, como: <br> 
> print(capital["RN"]) <br> 
    - Onde ele retornará: <br> 
> "Natal"

### CRUD e Operações
O CRUD se refere as operações que um dicionário deve ser capaz de realizar na maioria dos casos.
- C -> CREATE - adicionar uma chave com valores ao dicionário, porque ele não possuí um tamanho máximo e sim dinâmico, ou seja, ele se adapta conforme são inseridos ou removidos os itens.
    - PARA ISSO BASTA - seguindo o exemplo acima - DIGITAR NO CÓDIGO: <br> capital["AM"] = "Manaus"
- R -> READ - ler as informações, sejam as novas ou anteriores, porque ele precisará delas para realizar as demais operações e garantir que não hajam duas chaves iguais para informações diferentes, atualizar dados antigos ou deletar aqueles que não são mais necessários.
- U -> UPDATE - atualizar as informações antigas, portanto ele deve tê-las lido e dar ao usuário a opção de alterar as já preenchidas ou adicionar ainda mais.
    - PARA ISSO BASTA - seguindo o exemplo acima - DIGITAR NO CÓDIGO: <br> capital["PB"] = "J. Pessoa"
- D -> DELETE - deletar, excluir uma chave com valores ao dicionário, porque ele não possuí um tamanho máximo e sim dinâmico, ou seja, ele se adapta conforme são inseridos ou removidos os itens.
As demais operações que você pode ter ao longo do código relacionadas a dicionários são inúmeras, contudo as mais utilizadas são:
- Exibir os itens (chaves e valores) do dicionário -> através da função "print". Exemplo:
  > No código: <br> capital = {"RN": "Natal", "PB": "João Pessoa", "PE": "Recife"} <br> print(capital) <br>  <br> Saída:  <br>  "{'RN':'Natal', 'PB':'João Pessoa', 'PE':'Recife'}"
  
- Exibir apenas as chaves do dicionário -> através da função "print(*dicionario)". Exemplo:
  > No código: <br> capital = {"RN": "Natal", "PB": "João Pessoa", "PE": "Recife"} <br> print(*capital) <br>  <br> Saída:  <br>  "RN PB PE"
  
- Obtenção do número de elementos -> através da função "Len". Exemplo:
  > No código: <br> capital = {"RN": "Natal", "PB": "João Pessoa", "PE": "Recife"} <br> print(len(capital)) <br>  <br> Saída:  <br>  "3"

- Testar se uma chave está no dicionário -> através da função "in". Exemplos:
   > No código: <br> capital = {"RN": "Natal", "PB": "João Pessoa", "PE": "Recife"} <br> print("RN" in capital) <br>  <br> Saída:  <br>  "true"
   > No código: <br> capital = {"RN": "Natal", "PB": "João Pessoa", "PE": "Recife"} <br> print("Natal" in capital) <br>  <br> Saída:  <br>  "false" <br>  <br> # Lembre-se: "natal" é um valor associado a chave "RN", não uma chave e o "in" testa CHAVES

- Remover elementos do dicionário -> através da instrução "del". Exemplo:
   > No código: <br> capital = {"RN": "Natal", "PB": "João Pessoa", "PE": "Recife"} <br> del capital["RN"] <br> print(capital) <br>  <br> Saída:  <br>  "{'PB':'João Pessoa', 'PE':'Recife'}"

- Obter a última chave -> através da função "max", é válido lembrar que ela funciona em uma ordem específica, para string, ela procura em ordem alfabética e para números (int, float...) ela procura na ordem numérica e mostra o maior número. Exemplo:
   > No código: <br> capital = {"RN": "Natal", "PB": "João Pessoa", "PE": "Recife"} <br> del capital["RN"] <br> print(max(capital)) <br>  <br> Saída:  <br>  "RN"

- Obter a primeira chave -> através da função "min", é válido lembrar que ela funciona em uma ordem específica, para string, ela procura em ordem alfabética e para números (int, float...) ela procura na ordem numérica e mostra o menor número. Exemplo:
   > No código: <br> capital = {"RN": "Natal", "PB": "João Pessoa", "PE": "Recife"} <br> del capital["RN"] <br> print(min(capital)) <br>  <br> Saída:  <br>  “PB”

### Iterando em um dicionário
Iterar significa, em termos mais simples, "passar por cada coisa, uma a uma", então quando é dito: "iterar itens da classe tuple", apenas significa passar por uma a um de uma classe onde até mesmo a sua ordem é imutável, portanto tudo dentro dela estaria sempre no mesmo lugar. Por isso é possível iterar separadamente as "chaves"/"keys" de um dicionário e seus "valores"/"values". Com as seguintes operações:
- 'for item in capital.items()': print(item) -> mostra os itens (chaves e valores juntos) da seguinte maneira:
> ('RN', 'Natal') <br> ('PB', 'João Pessoa') <br> ('PE', 'Recife')

- 'for key, value in capital.items(): print(key, value)' -> mostra as chaves e valores separados da seguinte maneira:
> RN Natal <br> PB João Pessoa <br> PE Recife

- 'for key in capital.keys(): print(key)' ou 'for key in capital: print(key)' -> mostra as chaves apenas.
- for value in capital.values(): print(value) -> mostra os valores apenas.
> É válido lembrar que o nome dado após o for não importa, apenas o '.item', '.keys' ou '.values' ao final. Portanto, se utilizado: for values in capital: print(values), retornará as chaves e não valores.
