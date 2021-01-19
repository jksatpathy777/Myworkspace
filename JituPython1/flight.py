class flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []
    
    def add_passenger(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True

    def open_seats(self):
        return self.capacity - len(self.passengers)

flight = flight(3)

people = ["Harry", "Ron", "Hermione", "Ginny"]
for person in people:
    #success = flight.add_passenger(person)
    #if success:
    if flight.add_passenger(person):
        print(f"added {person} to flight successfully.")
    else:
        print(f"No available seats for {person}")
        
    
