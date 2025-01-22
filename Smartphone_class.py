class Smartphone:
    def __init__(self, brand, model, storage):
        self.brand = brand
        self.model = model
        self.__storage = storage  

    def get_storage(self):
        """Encapsulation: Getter for storage"""
        return self.__storage

    def set_storage(self, storage):
        """Encapsulation: Setter for storage"""
        if storage > 0:
            self.__storage = storage
        else:
            print("Storage must be positive!")

    def display_info(self):
        return f"Brand: {self.brand}, Model: {self.model}, Storage: {self.__storage}GB"


class GamingSmartphone(Smartphone):
    def __init__(self, brand, model, storage, cooling_system):
        super().__init__(brand, model, storage)
        self.cooling_system = cooling_system

    def display_info(self):
        """Polymorphism: Overriding display_info"""
        return (
            super().display_info()
            + f", Cooling System: {self.cooling_system}"
        )



phone = Smartphone("Tecno", "Camon 30s Pro", 256)
print(phone.display_info()) 

gaming_phone = GamingSmartphone("Redmi", "Note 13 Pro", 512, "LiquidCool")
print(gaming_phone.display_info())

