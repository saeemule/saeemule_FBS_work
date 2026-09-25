class SYMARKS:
    def __init__(self, computer_total, maths_total, electronics_total):
        self.ComputerTotal = computer_total
        self.MathsTotal = maths_total
        self.ElectronicsTotal = electronics_total

    def __str__(self):
        return (f"SY Marks -> Computer: {self.ComputerTotal}, "
                f"Maths: {self.MathsTotal}, Electronics: {self.ElectronicsTotal}")


# ---- Demo ----
if __name__ == "__main__":
    sy = SYMARKS(75, 68, 72)
    print(sy)