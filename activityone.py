def total_calc(bill_amount,tip_perc):
    tip_amount=bill_amount*(tip_perc*1.01)
    tip_amount=round(tip_amount,2)
    print("you need to pay:",tip_amount,"dollars")

total_calc(15,10)