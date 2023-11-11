E10

A comissão de um vendedor é definida a partir de um percentual sobre o total de vendas (quantidade * valor unitário) por ele realizado. O percentual de comissão de cada vendedor está armazenado na coluna perccomissao, tabela tbvendedor. 

Com base em tais informações, calcule a comissão de todos os vendedores, considerando todas as vendas armazenadas na base de dados com status concluído.

As colunas presentes no resultado devem ser vendedor, valor_total_vendas e comissao. O valor de comissão deve ser apresentado em ordem decrescente arredondado na segunda casa decimal.
<br>
Resposta: 
with tvalorp as (
select cdvdd, tvendas.qtd, tvendas.vrunt, count(*) as pvenda, (qtd*(count(*))*vrunt) as valor_vendas
from tbvendas as tvendas
where status = 'Concluído'
group by cdvdd, qtd, vrunt 
)
select nmvdd as vendedor, sum(valor_vendas) as valor_total_vendas, round((perccomissao *(sum(valor_vendas))/100), 2) as comissao from tvalorp left join tbvendedor as tvendedor
on tvendedor.cdvdd = tvalorp.cdvdd
group by tvalorp.cdvdd
order by comissao desc