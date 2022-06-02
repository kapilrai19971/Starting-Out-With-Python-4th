# Stock Transaction Program
purchase_share = 2000
per_share = 40
purchase_commision = 0.03

total_amount = purchase_share * per_share
print("Total amount of share purchase: ", total_amount)

brokerCommisonPurchase = total_amount * purchase_commision

print("Broker commission when purchasing share: ", brokerCommisonPurchase)

saleStock = purchase_share * 42.75

print("Total sales of stock: ", saleStock)
brokerCommisionSale = saleStock * purchase_commision

print("Broker commisson after sales:  ", brokerCommisionSale)

total = (saleStock - brokerCommisionSale) - (total_amount - brokerCommisonPurchase)
print("Total amount left after giving to broker: ", total)