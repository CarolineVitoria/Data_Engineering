E6

Apresente a query para listar o autor com maior número de livros publicados. O resultado deve conter apenas as colunas codautor, nome, quantidade_publicacoes. 
<br>
Resposta:
select aut.codautor, aut.nome, count(liv.autor) as quantidade_publicacoes
from autor as aut left join livro as liv
on aut.codautor = liv.autor
group by aut.nome 
order by quantidade_publicacoes desc
limit 1
