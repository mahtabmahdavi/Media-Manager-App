class Actor:
    def __init__(self, first_name, last_name):
        # Properties
        self.first_name = first_name
        self.last_name = last_name

    # Methods
    @staticmethod
    def show_table():
        print(f"\tFirst Name\t\t|\tLast Name\t\t".expandtabs(12))
        print(f"-----------------------------------" * 2)

    def show_info(self):
        print(f"{self.first_name}\t| {self.last_name}".expandtabs(12))