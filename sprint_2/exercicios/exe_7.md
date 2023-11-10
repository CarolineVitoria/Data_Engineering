E7

Apresente a query para listar o nome dos autores com nenhuma publicação. Apresentá-los em ordem crescente.
<br>

Resposta:
select aut.nome
from autor as aut left join livro as liv
on aut.codautor = liv.autor
group by aut.nome
having count(liv.autor) = 0