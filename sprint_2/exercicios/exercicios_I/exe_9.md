E9

Apresente a query para listar o código e nome do produto mais vendido entre as datas de 2014-02-03 até 2018-02-02, e que estas vendas estejam com o status concluída. As colunas presentes no resultado devem ser cdpro e nmpro.

<br>
Resposta:
<br>
with produtos_vendidos as(
select cdpro, nmpro , count(nmpro) as pvendas from tbvendas
where status = 'Concluído'  and dtven BETWEEN '2014-02-03 00:00:00' and '2018-02-02 00:00:00'
group by cdpro, nmpro
order by pvendas desc
)
select cdpro, nmpro from produtos_vendidos
limit 1