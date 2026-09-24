'''
task: Calculate the Sales Tax
name: calc_sales_tax
inputs: order_total, tax_rate
side effect: no
return: tax
'''
def calc_sales_tax(order_total, tax_rate):
    tax = order_total * tax_rate
    return tax