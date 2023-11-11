E5

Apresente a query para listar o nome dos autores que publicaram livros através de editoras NÃO situadas na região sul do Brasil. Ordene o resultado pela coluna nome, em ordem crescente. Não podem haver nomes repetidos em seu retorno.

Respostas:
select distinct aut.nome
from autor as aut inner join livro as liv
on aut.codautor = liv.autor
inner join editora as ed
on liv.editora = ed.codeditora
inner join endereco as ende
on ed.endereco = ende.codendereco
where ende.estado not in ('MINAS GERAIS', 'PARANÁ')
order by aut.nome