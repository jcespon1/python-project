
flat_charge = 20

#Ground shipping
def groundShipping(weight):

    if (weight < 2):
        cost = ((weight * 1.5) + flat_charge)
        print(cost)

    elif (weight > 2) & (weight < 6):
        cost =  ((weight * 3) + flat_charge)
        print(cost)
    elif (weight >= 6) & (weight <10):
        cost = ((weight * 4) + flat_charge)
        print(cost)
    elif weight >= 10:
        cost = ((weight * 4.75) + flat_charge)
        print(cost)

groundShipping(8.4)