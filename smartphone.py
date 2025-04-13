class Smartphone:
    def __init__(self, brand, model, storage, camera_resolution, battery_capacity):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.camera_resolution = camera_resolution
        self.battery_capacity = battery_capacity
        self.is_on = False  # Initial state: smartphone is off 

    def turn_on(self):
        if not self.is_on:
            self.is_on = True
            print(f"{self.brand} {self.model} is now on.")
        else:
            print(f"{self.brand} {self.model} is already on.")

    def turn_off(self):
        if self.is_on:
            self.is_on = False
            print(f"{self.brand} {self.model} is now off.")
        else:
            print(f"{self.brand} {self.model} is already off.")

    def take_photo(self):
        if self.is_on:
            print(f"Taking a photo with {self.camera_resolution} camera.")
        else:
            print("Please turn on the phone first.")

       