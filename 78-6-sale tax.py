# we need to convert the purchase into float
amtPurchase=float(input("Amount of Purchase? "))

percentStateTx = 0.05
percentFedTx   = 0.025


stateTx = amtPurchase*percentStateTx
fedTx   = amtPurchase*percentFedTx

print('State Tax',   stateTx)
print('Federal Tax', fedTx)
print('Total Tax',   fedTx+stateTx)
print('Total of the sale', amtPurchase+fedTx+stateTx)



