# Resumo TPC5
## 8/10/2024

## Autora: Clara Carvalho A107195
Para este trabalho foi-nos pedido para realizar um programa para uma aplicação para gerir  um cinema. Teriamos de  ter várias opções como inserir novas salas no cinema, referindo o filme em exibição e o número de lugares nessa sala.Também teriamos de ter a opção de listar as salas e a opção de vender bilhetes e de verificar os lugares disponíveis em alguma sala.

# 1.Defenir o menu
Inicilmente comecei por defenir o menu que iria aparecer ao utilizador de forma a me poder orientar nas opções que precisava de realizar para que o utilizador tivesse estas opções.
Decidi colocar cada opção associada a um número como realizado nos trabalhos anteriores.

# 2. Defenir as funções
De seguida antes do menu, defeni as funções necessárias para a realização do programa, mas primeiro coloquei o cinema como uma lista vazia para que inicialmente este não tivesse nenhuma sala.

Opção 1: A opção 1 era de criar sala então defeni uma função com esse nome, coloquei a questão de quantos lugares teria a sala e de que filme estaria em exibição e coloquei um append para juntar a lista do cinema e denominei de sala. De seguida decidi colocar os bilhetes vendidos a 0 pois inicialmente cada sala não tem bilhetes vendidos. Também decidi, após fazer as restantes funções, adicionar o comando capitalize para que coloque as letras do filme maiúsculas  de modo a que futuramente caso seja necessário pesquisar algo sobre o filme não considere erro ao inserir as letras maiúsculas ou minúsculas.

Opção 2: A segunda opção era para remover uma sala e eu decidi usar o comando index para o utilizador introduzir o índice da sala que deseja remover e utilizei o pop para a sua remoção.

Opção 3: A opção 3 era a opção de listar as salas e basicamente usei o ciclo for onde coloquei for s(sala) in cinema print(s) de modo a mostrar as salas em uma lista.

Opção 4: Para opção 4, sendo esta bastante parecida com a 3, coloquei a opção de consultar as salas em que apenas, numa só lista, coloquei print do cinema.

Opção 5:Para opção 5 coloquei para verificar os ligares disponíveis numa certa sala. Decidi novamente usar o ciclo for com for s in cinema e de seguida coloquei que se s[2] que significa o indice na sala ( neste caso o silme), coloquei que iria fazer o s[0](lugares da sala)-s[1] (os bilhetes vendidos).

Opção 6: A sexta opção era para vender bilhetes e decidi fazer uma função parecida á anterior porém coloquei no s[1](bilhetes vendidos) a ser estes mesmo + os nbilhetes que em baixo perguntei o número de bilhetes que desejava vender.

# 3. As opções
Conforme fui realizando as funções fui adicionando em baixo do menu as opções e as diferentes condições para estas opções. Coloquei em cada uma delas a condição if not cinema que significa se o cinema estiver vazio, a devolver a resposta de que o cinema não tinha salas.
Na opção 5 coloquei para intruzir o nome do filme que deseja consultar os lugares dispoíveis e usei novamente o comando capitalize para que não aconteça o referido acima.
Na opção 6 coloquei novamente o mesmo comando e a mesma questão mas também coloquei o número de bilhetes que pretende e caso este seja maior que o número de lugares disponíveis coloquei a devolver que para esse número de bilhetes não existem lugares disponíveis.

Por fim como nos outros trabalhos realizados, ainda dentro do ciclo while, coloquei que caso selecione uma opção diferente de 0,1,2,3,4,5 e 6 seja devolvido "Opção inválida". Fora do while (para a opção 0) coloquei a devolver "Obrigado e até á próxima e não coloquei o menu novamente pois com essa opção o programa iria fechar. 