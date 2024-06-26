class Flight():
     # Method to create new flight with given capacity
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []
    # Method to add a passenger to the flight:
    def add_passenger(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True
    # Method to check if there are open seats
    def open_seats(self):
        return self.capacity - len(self.passengers)
    
flight = Flight(3)

people = ["Harry", "Ron", "Hermione", "Ginny"]

for person in people: 
   success = flight.add_passenger(person)
   if success: 
       print (f"Added {person} too flight successsfully.")
   else: 
       print(f"No available seats for {person}.")