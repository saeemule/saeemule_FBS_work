class TYMarks:
    def __init__(self, theory, practical):
        self.Theory = theory
        self.Practical = practical

    def __str__(self):
        return f"TY Marks -> Theory: {self.Theory}, Practical: {self.Practical}"


# ---- Demo ----
if __name__ == "__main__":
    ty = TYMarks(65, 28)
    print(ty)