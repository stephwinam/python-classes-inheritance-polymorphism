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
            print(f"Taking a photo with {self.camera_resolution} MP camera.")
        else:
            print("Please turn on the phone first.")

    def display_info(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Storage: {self.storage} GB")
        print(f"Camera: {self.camera_resolution} MP")
        print(f"Battery: {self.battery_capacity} mAh")
        print(f"Is On: {self.is_on}")

# Creating instances of the Smartphone class
phone1 = Smartphone("Apple", "iPhone 13", 128, 12, 3240)
phone2 = Smartphone("Samsung", "Galaxy S21", 256, 108, 4000)

phone1.display_info()
phone1.turn_on()
phone1.take_photo()
phone1.turn_off()

       