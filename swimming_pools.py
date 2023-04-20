import numpy as np
import pandas as pd
from filters import Filters
from modified_zeolites import ModifiedZeolites
from six_stage_crane import sixstagecrane


class SwimmingPool:
    def __init__(self, volume, length, width, depth):
        self.volume = volume
        self.length = length
        self.width = width
        self.depth = depth
        self.temperature = 25
        self.ph_level = 7.0
        self.chlorine_level = 0.0
        self.filters = Filters()
        self.zeolites = ModifiedZeolites()
        self.crane = sixstagecrane()
        self.water_is_clean = False

    def water_purification(self):
        self.temperature = np.random.normal(25, 1)  # update temperature with a random value
        self.ph_level = np.random.normal(7.0, 0.1)  # update pH level with a random value
        self.chlorine_level = np.random.normal(0.5, 0.1)  # update chlorine level with a random value

        if not self.crane.get_on_status():
            self.crane.turn_on()

        if self.filters.is_dirty:
            self.filters.clean()

        if self.zeolites.is_full:
            self.zeolites.regenerate()

        self.crane.go_to_next_stage()
        self.crane.go_to_next_stage()

        self.water_is_clean = True
        print("The water is now clean and ready for use.")

    def is_water_clean(self):
        return self.water_is_clean

    def pool_status(self):
        data = {
            'Temperature': [self.temperature],
            'pH Level': [self.ph_level],
            'Chlorine Level': [self.chlorine_level]
        }
        df = pd.DataFrame(data)
        print(df)

    def tap_modes(self):
        while True:
            print("\nTap modes:")
            print("1. Water purification")
            print("2. Pool status")
            print("3. Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                self.water_purification()
            elif choice == "2":
                self.pool_status()
            elif choice == "3":
                break
            else:
                print("Invalid choice. Try again.")


if __name__ == '__main__':
    pool = SwimmingPool(100000, 50, 20, 2)
    pool.tap_modes()
