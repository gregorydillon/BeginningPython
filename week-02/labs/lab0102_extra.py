steak_price = 18.95
manhattan_price = 9.95
salad_price = 12.95
print "Steak             $%s" % steak_price
print "Manhattan         $%s" % manhattan_price
print "Salad             $%s" % salad_price
print "---------------------------"

subtotal = steak_price + manhattan_price + salad_price
tax = subtotal * 0.0825
grand_total = subtotal + tax
print "Subtotal          $%s" % (subtotal)
print "Tax               $%.2f" % (tax)
print "Grand Total       $%.2f" % (grand_total)
