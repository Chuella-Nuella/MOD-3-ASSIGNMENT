
class Product:
    def __init__(self, product_id: int, name: str, description: str, price: float):
        """
        Initializes a Product object.

        Args:
            product_id (int): Unique product ID.
            name (str): Product name.
            description (str): Product description.
            price (float): Product price.
        """
        self.product_id = product_id
        self.name = name
        self.description = description
        self.price = price

    def update_product(self, name: str = None, description: str = None, price: float = None) -> None:
        """
        Updates the product's details.

        Args:
            name (str, optional): New product name. Defaults to None.
            description (str, optional): New product description. Defaults to None.
            price (float, optional): New product price. Defaults to None.
        """
        if name:
            self.name = name
        if description:
            self.description = description
        if price:
            self.price = price

    def display_details(self) -> str:
        """
        Returns a string containing the product's details.

        Returns:
            str: Product details.
        """
        return f"ID: {self.product_id}, Name: {self.name}, Description: {self.description}, Price: {self.price}"

