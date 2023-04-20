class sixstagecrane:
    def __init__(self):
        self.is_on = False
        self.current_stage = 0

    def turn_on(self):
        self.is_on = True
        print("The six-stage crane is now on.")

    def turn_off(self):
        self.is_on = False
        print("The six-stage crane is now off.")

    def go_to_next_stage(self):
        if self.current_stage < 6:
            self.current_stage += 1
            print(f"The crane is now at stage {self.current_stage}.")
        else:
            print("The crane is already at the highest stage.")

    def get_on_status(self):
        return self.is_on

    @property
    def get_current_stage(self):
        return self.current_stage
