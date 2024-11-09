# Resumo TPC6
## 19/10/2024

# Autora: Clara Carvalho A107195

Para este trabalho foi-nos pedido para realizar uma aplicação para gestão de alunos onde seria criado uma turma, que seria uma lista de launos, e um aluno seria um túplo onde tinha o seu nome, id e uma lista com as respetivas notas dos seus TPC, Projeto e Teste. Teriamos de colocar também uma função para consultar um aluno pelo seu id e de guardar a turma num ficheiro e carregar uma turma de um ficheiro.

# Defenir o menu
Inicilmente comecei por defenir o menu que iria aparecer ao utilizador de forma a me poder orientar nas opções que precisava de realizar para que o utilizador tivesse estas opções.
Decidi colocar cada opção associada a um número como realizado nos trabalhos anteriores.

# Defenir as funções
Como referido nos  trabalhos anteriores enquanto ia defenindo as funções ia ao ciclo while criado abaixo do menu ajustar as opções de forma ao programa rolar da melhor forma.~
* Função criar turma e inserir aluno na turma:
De forma  bastante paerida á do TPC5, criei a turma defenindo uma função criar turma e colocando esta inicialmente vazia. De seguida para inserir alunos na turma comecei por questionar o seu nome, o seu id, e as suas notas respetivas fazendo um ciclo while para que as notas estivessem entre os valores de 0 e 20. Por fim coloquei que um aluno era o tuplo dessas informações sendo as notas uma lista dentro do tuplo. Por fim utilizando a ferramenta append juntei o aluno inserido á turma anteriormente criada.

* Função listar turma e função consultar aluno:
Para a função listar turma defeni-a de forma bastante igual á forma listar salas no exercício do cinema, usando um ciclo for neste caso sendo alunos coloquei a in turma e coloquei print dos alunos. Para a função consultar alunos coloquei a questionar o id do respetivo aluno e de seguida coloquei que caso não encontra-se o aluno (e=False) coloquei a devolver que esse id não se encontrava na turma. Caso encontra-se(usei o ciclo for e coloquei que para o aluno(a) na turma se aluno com esse respetivo id que se encontra na posição 1 (a[1]) iria devolver o aluno) a variável "e" iria se tornar verdadeira.

* Função guardar turma e carregar turma:
Para a função guardar turma  inicialmente tive de  criar outra função onde iria converter o aluno que é um tuplo para uma linha de texto. Para isso defeni que o nome, id e notas seria o correspondente ao aluno e coloquei a dar return do nome, id, nota[0]-nota TPC, nota[1]-nota Projetos, nota [2]- nota Testes. De seguida para a função guardar turma coloquei abrir um ficheiro atribuindo a este o nome de variável file e coloquei a abrir com o fnome e em modo de escrita ("w"). De seguida a função irá percorrer a lista de alunos e escrever a linha formatada anteriormente criada. Por fim irá fechar o arquivo. Para a função carregar turma coloquei inicialmente a questionar o nome do ficheiro que desejava carregar.  De seguida coloquei a abri-lo em modo de leitura e a percorrer cada linha para extrair os dados de cada aluno, convertendo-os de uma sequência de texto para um tuplo com as informações organizadas. Para isto voltei a usar o comando de comprimento (len()) e coloquei que seria 5, uma vez que cada aluno teria 5 dados sobre si. Por fim coloquei que se o ficheiro não existisse para devolver que ele não foi encontrado e que caso o ficheiro estivesse desformatado para dar erro. 

Em algumas opções, como tinha sido pedido anteriormente, coloquei a quando o utilizador acaba-se de realizar a opção, como por exemplo consultar um aluno ou inserir um aluno na turma, coloquei a questionar se desejava continuar nesse opção ou não de forma a se tornar mais prático para o utilizador. Também coloquei que caso ainda não tivesse sido selecionada a opção 1 (Criar turma) a devolver  que ("Ainda não existem turmas").
No fim de colocar todas as opções, fora do ciclo while, como usei anteriomente no trabalho do cinema, coloquei a aplicação a fechar (opção 0) e a devolver uma mensagem de "Obrigado e até á próxima".
Para terminar, como tinha sido pedido inicialmente, criei uma turma com 5 alunos e guardei num formato de ficheiro. 