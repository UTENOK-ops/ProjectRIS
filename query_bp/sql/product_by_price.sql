select prod_name, prod_measure, prod_price
from product
where prod_price between %s and %s
order by prod_price
