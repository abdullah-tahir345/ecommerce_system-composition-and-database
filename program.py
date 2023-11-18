from ecommerce_system import Ecommerce
from user_address import Address
from product import Product
from cart import ShoppingCart
from order import Order
from users import User

store_1 = Ecommerce()
store_1.get_data()

print('1. Add Product')
print('2. Update Product')
print('3. Display Product Information')
number = int(input('Press Number : '))


if number == 1:
    name = str(input('Enter Product Name : '))
    quantity_in_stock = int(input(f'Enter {name} Product Quantity : '))
    price = int(input(f'Enter {name} Product Price : ' ))
    store_1.add_product_in_store(name, quantity_in_stock, price)
elif number == 2:
    product_name = str(input('Enter Product Name : '))
    new_quantity = int(input(f'Enter {product_name} Product Quantity : '))
    new_price = int(input(f'Enter {product_name} Product Price : ' ))
    store_1.update_product_in_store(product_name, new_quantity, new_price)
elif number == 3:
    store_1.disp_product_info()
else:
    print(store_1.store_products)

#store_1.add_product_in_store('lux', 500, 150)
#store_1.add_product_in_store('Surf exCel', 200, 1000)
#store_1.add_product_in_store('large pizza', 199, 1500)
#store_1.add_product_in_store('meDIUm Pizza', 10, 850)
#store_1.add_product_in_store('Small pizza', 10, 400)


#lux = Product(1, 'Lux', 500, 150)
#s_excel = Product(2, 'Surf Excel', 200, 1000)
#l_pizza = Product(3, 'Large Pizza', 199, 1500)
#m_pizza = Product(4, 'Medium Pizza', 10, 850)
#s_pizza = Product(5, 'Small Pizza', 10, 400)

#cart_1 = ShoppingCart(store_1)
#cart_1.add_product('luX', 5)
#cart_1.add_product('large pizZa', 1)

#cart_1.remove_product('lux', 4)

#user1 = User(1, 'James', 'james@gmail.com')
#user1.address = Address('11th Street', 'Lahore', 'Punjab', 55221)
#user1.add_cart(cart_1)
#user1.display_cart_info()

#order_james = Order()
#order_james.create_receipt(user1, cart_1)