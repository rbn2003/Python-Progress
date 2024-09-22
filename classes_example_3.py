class Airplane:
    """ A simple airplane class"""
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color 
        self.flight_hours = 0

    def list_airplanes(self):
        """Return a neatly formatted airplane"""
        airplane_attributes = f"Make: {self.make}\n Model: {self.model}\n Year: {self.year}\n Color: {self.color}"
        return airplane_attributes

    def read_flight_hours(self):
        """Print Flight Hours"""
        flight_hours_message = f"FLight hours {self.flight_hours} hours."
        return flight_hours_message

    def update_flight_hours(self, hours):
        """Set total flight hours"""
        self.flight_hours += hours 

new_airplane = Airplane ('AERO', 'BOEING 747', '2001', 'Blue')
new_airplane.update_flight_hours (100)
new_airplane.update_flight_hours (300)

print(new_airplane.list_airplanes())
print(new_airplane.read_flight_hours())