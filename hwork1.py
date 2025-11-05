price_rice = 45.0
price_sugar = 40.0
price_oil = 130.0
qty_rice = 3.0
qty_sugar = 2.5
qty_oil = 1.8
total_rice = price_rice * qty_rice
total_sugar = price_sugar * qty_sugar
total_oil = price_oil * qty_oil
total_bill = total_rice + total_sugar + total_oil
total_bill_int = int(total_bill)
total_bill_str = str(total_bill)
delivery_charge = 7.0
final_bill = total_bill + delivery_charge
print("----- Grocery Store Bill -----")
print(f"Rice:  {qty_rice} kg × ₹{price_rice} = ₹{total_rice}")
print(f"Sugar: {qty_sugar} kg × ₹{price_sugar} = ₹{total_sugar}")
print(f"Oil:   {qty_oil} kg × ₹{price_oil} = ₹{total_oil}")
print("--------------------------------")
print(f"Total (without delivery): ₹{total_bill:.2f}")
print(f"Total as integer: ₹{total_bill_int}")
print(f"Total as string: '{total_bill_str}'")
print(f"Delivery charge: ₹{delivery_charge}")
print("--------------------------------")
print(f"Final Bill (with delivery): ₹{final_bill:.2f}")

