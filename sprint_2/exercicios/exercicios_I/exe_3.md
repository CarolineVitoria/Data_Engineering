E3

 Apresente a query para listar as 5 editoras com mais livros na biblioteca. O resultado deve conter apenas as colunas quantidade, nome, estado e cidade. Ordenar as linhas pela coluna que representa a quantidade de livros em ordem decrescente. 

<br>
Resposta:

select count(*) as quantidade, ed.nome, ende.estado, ende.cidade
from livro as liv left join editora as ed on liv.editora = ed.codeditora 
left join endereco as ende on ed.endereco = ende.codendereco 
group by ed.nome