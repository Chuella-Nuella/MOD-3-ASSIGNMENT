README.md:
Policy Management System

Overview
This is a Python-based policy management system for an insurance company. The system is designed to provide the following functionalities:

•	Registration, suspension, and reactivation of policyholders.
•	Creation, updating, and removal of products.
•	Payment processing, sending reminders, and applying penalties.
The project applies object-oriented programming concepts such as classes, methods, and error handling.

Features

Policyholder Management
Register policyholders.
Suspend or reactivate policyholder accounts.
Associate policyholders with insurance products.

Product Management
Create new products with details like name, description, and price.
Update product information.
Suspend (remove) products from availability.

Payment Management
Process payments for policyholders.
Send payment reminders.
Apply penalties to overdue payments.

Installation and Usage

Installation Steps

1. Clone or download this repository:
https://github.com/Chuella-Nuella/MOD-3-ASSIGNMENT/tree/main/project.py
2. Navigate to the project directory
3. Ensure all required Python files are in the same directory:

•	policyholder.py
•	product.py
•	payment.py
•	main.py

Running the Program

1. Open a terminal or command prompt.
2. Run the main program:
python main.py
Example Output:
The program will demonstrate the following:
•	 Products are created and displayed.
•	 In this model, policyholders are registered and associated with products.
•	 Payments are processed; details pertaining to the payments are then shown.
•	 Error handling: In case there is any error, it catches it and shows a friendly message.

Project Structure
policy-management-system/
├── policyholder.py    # Manages policyholder-related operations.
├── product.py         # Manages product-related operations.
├── payment.py         # Manages payment-related operations.
├── main.py            # Main script to demonstrate the functionality.
└── README.md          # Project instructions and documentation.
