
class Policyholder:
    def __init__(self, policyholder_id: int, name: str, email: str):
        """
        Initializes a Policyholder object.

        Args:
            policyholder_id (int): Unique policyholder ID.
            name (str): Policyholder name.
            email (str): Policyholder email.
        """
        self.policyholder_id = policyholder_id
        self.name = name
        self.email = email
        self.active = True
        self.policies = []

    def register_policy(self, policy: str) -> None:
        """
        Registers a policy for the policyholder.

        Args:
            policy (str): Policy name or ID.
        """
        if policy not in self.policies:
            self.policies.append(policy)
        else:
            print("Policy already registered.")

    def suspend(self) -> None:
        """
        Suspends the policyholder's account.
        """
        self.active = False

    def reactivate(self) -> None:
        """
        Reactivates the policyholder's account.
        """
        self.active = True

    def display_details(self) -> str:
        """
        Returns a string containing the policyholder's details.

        Returns:
            str: Policyholder details.
        """
        status = "Active" if self.active else "Suspended"
        policies = ", ".join(self.policies) if self.policies else "None"
        return f"ID: {self.policyholder_id}, Name: {self.name}, Email: {self.email}, Status: {status}, Policies: {policies}"
