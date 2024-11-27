from  policyholder import Policyholder
from   product import Product
from payment import Payment

def main():

    # Error Handlig
      try:
         
         #Create products
         product1 = Product(1, "Health Insurance", "Covers health expenses", 5000)
         product2 = Product(2, "Car Insurance", "Covers car damages", 3000)

          # Display product details
         print(product1.display_details())
         print(product2.display_details())

         # Create policyholders
         policyholder2 = Policyholder(2, "Angela", "angelojone@gmail.com")

         # Register policies for policyholders
         policyholder1.register_policy(product1)
         policyholder2.register_policy(product2)

         # Create payment instance and process payments
         payment_system = Payment()
         print(payment_system.process_payment(policyholder1.policyholder_id, product1.price))
         print(payment_system.process_payment(policyholder2.policyholder_id, product2.price))

         # Display policyholder details
         print(policyholder1.display_details())
         print(policyholder2.display_details())
        
        # Error Handling for Exception
      except Exception as e:
        # Error Message
         error_message = {"message":str(e)}
         print(error_message)


if __name__ == "__main__":
    main()


