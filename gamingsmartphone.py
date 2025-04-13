from smartphone import Smartphone  

class GamingSmartphone(Smartphone):
    def __init__(self, brand, model, storage, camera_resolution, battery_capacity, cooling_system, refresh_rate):
        super().__init__(brand, model, storage, camera_resolution, battery_capacity)
        self.cooling_system = cooling_system
        self.refresh_rate = refresh_rate

    def display_info(self): #Overriding the parent class method
        super().display_info()
        print(f"Cooling System: {self.cooling_system}")
        print(f"Refresh Rate: {self.refresh_rate} Hz")

    def play_game(self, game_name):
        if self.is_on:
            print(f"Playing {game_name} on {self.brand} {self.model} with {self.refresh_rate}Hz.")
        else:
            print("Please turn on the phone first.")

gaming_phone = GamingSmartphone("ROG", "Phone 5", 512, 64, 6000, "AeroActive Cooler 5", 144)
gaming_phone.display_info()
gaming_phone.turn_on()
gaming_phone.play_game("Genshin Impact")