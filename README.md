# algoritmo-cyk

Implementação de um reconhecedor de palavras utilizando o algoritmo CYK.

O algoritmo funciona da seguinte maneira: Em cada etapa da verificação, combina as células e verifica se essa combinação aparece na gramática. Se após todos os passos o símbolo inicial "S" estiver contido na última linha, a palavra pode ser derivada pela gramática dada.

Esse repositório utiliza dois arquivos, o algoritmo-cyk, com a implementação em si e a gramatica.txt, com a gramática que será lida e que obrigatoriamente tem que estar na forma normal de Chomsky para o reconhecedor ler.

Exemplo: 
S => XB | AB
X => AS
A => a
B => b

Para executar o arquivo é preciso escrever a linha de comando $ python algoritmo-cyk.py ou executar o comando run em algum editor de texto.
