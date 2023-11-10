E8

Apresente a query para listar o código e o nome do vendedor com maior número de vendas (contagem), e que estas vendas estejam com o status concluída.  As colunas presentes no resultado devem ser, portanto, cdvdd e nmvdd.
<br>

Resposta: 
with vendas_vendedor as (
select tvendedor.cdvdd, tvendedor.nmvdd, count(tvendas.cdven) as vendas from tbvendas as tvendas left join tbvendedor as tvendedor
on tvendas.cdvdd = tvendedor.cdvdd 
and tvendas.status = 'Concluído'
group by nmvdd
)
select cdvdd, nmvdd from vendas_vendedor
where vendas = (select max(vendas) from vendas_vendedor)
