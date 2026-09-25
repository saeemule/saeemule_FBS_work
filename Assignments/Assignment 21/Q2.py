class InvalidTelevisionException(Exception):
    pass


class Television:
    def __init__(self):
        self.ModelNumber = 0
        self.ScreenSize = 0
        self.Price = 0

    def AcceptDetails(self):
        try:
            model_number = int(input("Enter Model Number: "))
            screen_size = float(input("Enter Screen Size (in inches): "))
            price = float(input("Enter Price (Rs): "))

            if len(str(model_number)) > 4:
                raise InvalidTelevisionException("Model number cannot have more than 4 digits")

            if screen_size < 12 or screen_size > 70:
                raise InvalidTelevisionException("Screen size must be between 12 and 70 inches")

            if price < 0 or price > 5000:
                raise InvalidTelevisionException("Price must be between 0 and 5000 Rs")

            self.ModelNumber = model_number
            self.ScreenSize = screen_size
            self.Price = price

            print("Television details accepted successfully.")

        except InvalidTelevisionException as e:
            print(f"Error: {e}")
            print("Resetting all values to zero.")
            self.ModelNumber = 0
            self.ScreenSize = 0
            self.Price = 0

        except ValueError:
            print("Error: Invalid input type entered.")
            print("Resetting all values to zero.")
            self.ModelNumber = 0
            self.ScreenSize = 0
            self.Price = 0

    def Display(self):
        print("=" * 40)
        print(f"Model Number : {self.ModelNumber}")
        print(f"Screen Size  : {self.ScreenSize} inches")
        print(f"Price        : Rs {self.Price}")
        print("=" * 40)


# ---- Demo ----
if __name__ == "__main__":
    tv = Television()
    tv.AcceptDetails()
    tv.Display()