# payment
class Payment:
    def __init__(self):
        """
        Initializes a Payment object.
        """
        self.payment_records = []

    def process_payment(self, policyholder_id: int, amount: float) -> str:
        """
        Processes a payment for a policyholder.

        Args:
            policyholder_id (int): Unique policyholder ID.
            amount (float): Payment amount.

        Returns:
            str: Payment confirmation message.
        """
        if amount <= 0:
            raise ValueError("Payment amount must be positive.")
        self.payment_records.append({"policyholder_id": policyholder_id, "amount": amount})
        return f"Payment of {amount} processed for Policyholder ID: {policyholder_id}"

    def send_reminder(self, policyholder_id: int) -> str:
        """
        Sends a payment reminder to a policyholder.

        Args:
            policyholder_id (int): Unique policyholder ID.

        Returns:
            str: Reminder message.
        """
        return f"Reminder: Payment due for Policyholder ID: {policyholder_id}"

    def apply_penalty(self, policyholder_id: int, penalty_amount: float) -> str:
        """
        Applies a penalty to a policyholder's payment.

        Args:
            policyholder_id (int): Unique policyholder ID.
            penalty_amount (float): Penalty amount.

        Returns:
            str: Penalty confirmation message.
        """
        if penalty_amount <= 0:
            raise ValueError("Penalty amount must be positive.")
        self.payment_records.append({"policyholder_id": policyholder_id, "penalty": penalty_amount})
        return f"Penalty of {penalty_amount} applied to Policyholder ID: {policyholder_id}"





