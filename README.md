# coffee-shop-challenge

# coffee-shop-challenge

A simple Python project that models the relationships between **Customers**, **Coffees**, and **Orders** in a coffee shop.

## Project Structure

Customer class — represents a customer who places coffee orders.
Coffee class — represents a type of coffee offered.
Order class — connects a customer and a coffee, with a specific price.


- **Class Relationships**
  - One-to-many: A customer can place many orders.
  - One-to-many: A coffee can be ordered many times.

- **Data Validation**
  - Enforces price limits (between $1.00 and $10.00)
  - Type checking for associations

- Create and store customers, coffees, and orders.
- Automatically link orders to both customer and coffee.
- Retrieve associated orders from both customer and coffee.

## Example Usage

# Create customers and coffees
alice = Customer("Sebastian")
latte = Coffee("Latte")

# Create an order
order1 = Order(Sebastian, latte, 4)

# Accessing the related data
print(order1.customer.name)   # Sebastian
print(order1.coffee.name)     # Latte
