# Create a custom object
class Purchase(object):
    def __init__(self, amount):
        self.amount = amount

    def calculatetax(self, taxpercent):
        return self.amount * taxpercent/100.0

    def calculatetip(self, tippercent):
        return self.amount * tippercent/100.0

    def calculatetotal(self, taxpercent, tippercent):
        return self.amount * (1 + taxpercent/100.0 + tippercent/100.0)

# Create Purchase object given an amount
purchase = Purchase(100.0)
cost = 100.0

# Set the tax and tip percentages
taxpercent = 7.5
tippercent = 20.0

# Use the object to caclucate tax and tip
tax = purchase.calculatetax(taxpercent)
tip = purchase.calculatetip(tippercent)

# Display some useful information

print ('Purchase: ', cost)
print ('Tax: ', tax)
print ('Tip: ', tip)
print ('Total: ', purchase.calculatetotal(taxpercent, tippercent))
print ('My name is Kim Leach')