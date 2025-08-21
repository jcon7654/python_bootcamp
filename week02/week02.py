# Week02 Stuff
## Receipts
# create a product and price for 3 items
p1_name, p1_price = "Books", 49.95
p2_name, p2_price = "Computer", 579.99
p3_name, p3_price = "Monitor", 124.89

# create a company name and info
company_name = "coding temple, inc."
company_address = "283 Franklin St."
company_city = "Boston, MA"

# declare ending message
message = "Yo, thank you and come again!!"

# create a top border
print("*" * 50)

# print company information first, using format
#print( "\t\t{ }".format(company_name.title()) )
print( "*\t\t{}".format(company_name.title()), "\t\t *")
print( "*\t\t{}".format(company_address), "\t\t *" )
print( "*\t\t{}".format(company_city), "\t\t\t *" )

# print line between sections
print("=" * 50)

# print product details
print( "*\t{}\t\t${}".format(p1_name.title(), p1_price), "\t\t\t *" )
print( "*\t{}\t${}".format(p2_name.title(), p2_price), "\t\t *"  )
print( "*\t{}\t\t${}".format(p3_name.title(), p3_price), "\t\t *"  )
print("=" * 50)

# print out header for section of total  
total = p1_price + p2_price + p3_price
print( "*\t\t\t${}".format(total), "\t\t *" )

print("=" * 50)
print( "*", " " * 46, "*\n*\t", message.title(), "\t *\n*", " " * 46, "*" )
print("*" * 50)

var_hello = "Hello"
var_hello_len_count = int(len(var_hello))
print(var_hello_len_count)
var_hello_rev = ""
print(var_hello)
print(var_hello_rev)
while (var_hello_len_count > 0):
    var_hello_len_count = var_hello_len_count - 1
    var_hello_rev = var_hello_rev + var_hello[var_hello_len_count]
print(var_hello_rev)
print(var_hello[::-1])