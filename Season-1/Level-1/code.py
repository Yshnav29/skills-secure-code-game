'''
Welcome to Secure Code Game Season-1/Level-1!

Follow the instructions below to get started:

1. tests.py is passing but code.py is vulnerable
2. Review the code. Can you spot the bug?
3. Fix the code but ensure that tests.py passes
4. Run hack.py and if passing then CONGRATS!
5. If stuck then read the hint
6. Compare your solution with solution.py
'''

from collections import namedtuple
from decimal import Decimal

Order = namedtuple('Order', 'id, items')
Item = namedtuple('Item', 'type, description, amount, quantity')

def validorder(order: Order):
    payment = 0
    expense = 0

    for item in order.items:
        if item.type == 'payment':
            if -100000 <= item.amount <= 100000:
                payment += Decimal(str(item.amount))
        elif item.type == 'product':
            if type(item.quantity) is int and 0 < item.quantity <= 100 and 0 < item.amount <= 100000:
                expense += Decimal(str(item.amount)) * item.quantity
        else:
            return "Invalid item type: %s" % item.type
    if payment > 1000000 or expense > 1000000:
        return "Total amount payable for an order exceeded"
    if payment != expense:
        return "Order ID: %s - Payment imbalance: $%0.2f" % (order.id, payment - expense)
    else:
        return "Order ID: %s - Full payment received!" % order.id