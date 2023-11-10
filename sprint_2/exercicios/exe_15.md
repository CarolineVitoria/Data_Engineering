E15

Apresente a query para listar os códigos das vendas identificadas como deletadas. Apresente o resultado em ordem crescente.
<br>
 
Resposta:
select cdven 
from tbvendas
where deletado <> 0