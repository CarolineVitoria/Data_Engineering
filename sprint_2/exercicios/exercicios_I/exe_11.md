E11

Apresente a query para listar o código e nome cliente com maior gasto na loja. As colunas presentes no resultado devem ser cdcli, nmcli e gasto, esta última representando o somatório das vendas (concluídas) atribuídas ao cliente.
<br>
Resposta:
with tbcompras as(
select cdcli, nmcli, vrunt, qtd,  count(*) as compra, (qtd*(count(*))) as quantidade_total, ((qtd*(count(*)))*vrunt) as valor_compras
from tbvendas 
where status='Concluído'
group by nmcli, cdcli, vrunt, qtd
)
select cdcli, nmcli, sum(valor_compras) as gasto from tbcompras
group by cdcli, nmcli
order by gasto desc
limit 1
