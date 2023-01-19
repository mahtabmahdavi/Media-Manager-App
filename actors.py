class Actor:
    def __init__(self, first_name, last_name):
        # Properties
        self.first_name = first_name
        self.last_name = last_name

    # Methods
    def show_info(self):
        print(f"{self.first_name} {self.last_name}")