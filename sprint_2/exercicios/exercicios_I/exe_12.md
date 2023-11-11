E12

Apresente a query para listar código, nome e data de nascimento dos dependentes do vendedor com menor valor total bruto em vendas (não sendo zero). As colunas presentes no resultado devem ser cddep, nmdep, dtnasc e valor_total_vendas.

Observação: Apenas vendas com status concluído.

<br>
Resposta: 
with vedendorvendas as(
select cdvdd, vrunt, qtd, count(*) as vendas, (qtd*(count(*))) as quantidade_total, ((qtd*(count(*)))*vrunt) as valor_vendas
from tbvendas
where status = 'Concluído'
group by cdvdd, vrunt, qtd
)
select tdepe.cddep , tdepe.nmdep, tdepe.dtnasc, sum(valor_vendas) as valor_total_vendas 
from vedendorvendas as tvede right join tbdependente as tdepe
on tvede.cdvdd = tdepe.cdvdd  
group by tvede.cdvdd
order by valor_total_vendas
limit 1