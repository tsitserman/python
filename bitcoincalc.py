querry_price = input("Enter your querry price: \n")
querry_price = float(querry_price)
current_price = 35000
current_price = float(current_price)
btc = input("enter your bitcoin amount:\n")
btc = float(btc)
print ("If you sell at" + str(querry_price) + "ypyou receive" + str(btc*querry_price) + "gbp"  )
print ("If you sell at" + str(current_price) + "you receive" + str(btc*current_price) + "gbp"  )