E13

Apresente a query para listar os 10 produtos menos vendidos pelos canais de E-Commerce ou Matriz (Considerar apenas vendas concluídas).  As colunas presentes no resultado devem ser cdpro, nmcanalvendas, nmpro e quantidade_vendas.
<br>
Respostas:
with vendasporcanais as(
select nmcanalvendas, nmpro, tppro, cdpro, qtd , count(*) as vendas, (qtd*(count(*))) as quantidade_total 
from tbvendas
where status = 'Concluído'
group by nmcanalvendas, nmpro, tppro, cdpro, qtd
)
select cdpro, nmcanalvendas, nmpro, sum(quantidade_total) as quantidade_vendas from vendasporcanais
group by cdpro, nmcanalvendas
order by quantidade_vendas
limit 10