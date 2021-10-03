# 10%的首付款和12%的年息。每月的付款金额是定价减去首付之后的5%。编写一个程序，它接受销售价格作为输入。
# 程序显示的应该是一个表格，它拥有相应的表头，包括借贷的整个还款周期的支付计划。表的每一行应该包含如下项：
# * 第几个月（从1开始）
# * 当前的欠款总额
# * 该月所欠利息
# * 该月所欠本金
# * 该月还款额
# * 在还款后所欠总金额
# 一个月的利息等于余额 * 利率 / 12.一个月的本金等于该月的还款减去所欠的利息。
DOWN_PAYMENT_RATE = 0.1
ANNUAL_INTEREST_RATE = 0.12
PAYMENTS_RATE = 0.05


class CreditCard:
    def __init__(self,price):
        self.down_payment = DOWN_PAYMENT_RATE * price
        self.aggregate_amount = 0



if __name__ == '__main__':
    pass