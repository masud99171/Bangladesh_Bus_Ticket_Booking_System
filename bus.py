

class Bus:
    def __init__(self, number, route, total_seats):
        self.number = number
        self.route = route
        self.total_seats = total_seats
        self.booked_seats = 0

    def available_seats(self):

        return self.total_seats - self.booked_seats

    def book_seat(self):
        if self.available_seats() > 0:
            self.booked_seats += 1
            return True
        return False


class Passenger:
    def __init__(self, name, phone, bus):  # ekhane bus er obj ta asbe
        self.name = name
        self.phone = phone
        self.bus = bus


class BusSystem:
    def __init__(self):
        self. buses = []
        self. passengers = []
        self.fare = 500

    # ekhane obj ke arr er modde neoa hobe
    def Buses(self, bus):
        self.buses.append(bus)

    def Passengers(self, pas):
        self.passengers.append(pas)

    def show_buses(self):
        if not self.buses:
            print("\nEkhono kono bus add kora hoyni!")
            return
        print(f"\n{'Bus Number':<20}{'Route':<25}{'Available Seats'}")
        print("-" * 60)
        for b in self.buses:
            print(f"{b.number:<20}{b.route:<25}{b.available_seats()}")

    def show_pas(self):
        if not self.passengers:
            print("\nEkhono kono passenger ticket book koreni!")
            return

        print(
            f"\n{'Passenger Name':<20}{'Phone':<18}{'Bus Number':<15}{'Route':<20}{'Fare'}")
        print("-" * 80)
        for p in self.passengers:
            print(
                f"{p.name:<20}{p.phone:<18}{p.bus.number:<15}{p.bus.route:<20}৳{self.fare}")

    def bus_exst(self, num):
        for b in self.buses:
            if b.number == num:
                return True
        return False


class Admin:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self):
        if self.username == 'admin' and self.password == '1234':
            return True
        else:
            return False

    def add_bus(self, num, route, seats):
        if not system.bus_exst(num):
            bus = Bus(num, route, seats)
            system.Buses(bus)
            print(f"Bus {num} successfully add kora hoyeche!")
        else:
            print("eta age thekei ache ,, so onno number use koro !")


def book_ticket(bus_num, name, phone):
    chk = False
    set = False
    for seat in system.buses:
        if seat.number == bus_num:
            chk = True
            if seat.available_seats() > 0:
                set = True
                seat.booked_seats += 1
                pas = Passenger(name, phone, seat)
                system.Passengers(pas)
                print(f"Ticket booked successfully! Fare: ৳500")
    if chk and not set:
        print("ei bus e ekhon kono seat baki nei")
    elif not chk:
        print("eta ekta invalid bus numbor")


def view_buses():
    system.show_buses()


system = BusSystem()
while True:
    print("\n--- User Menu ---")
    print("1. Admin Login")
    print("2. Book Ticket")
    print("3. View Buses")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        name = input("Enter the name :")
        pas = input("Enter the password :")
        is_admin = Admin(name, pas)
        if is_admin.login():
            while True:
                print("\n--- Admin Menu ---")
                print("1. Add Bus")
                print("2. View All Buses")
                print("3. View All passengers")
                print("4. Logout")

                admin_choice = input("Enter your choice (1-4): ")

                if admin_choice == '1':
                    try:
                        bus_num = int(input("Enter the bus number : "))
                        route = input("Enter the route : ")
                        seats = int(input("Enter total seats : "))
                        if seats > 0:
                            is_admin.add_bus(bus_num, route, seats)
                        else:
                            print("0 er niche seat count kora hoy na !")
                    except ValueError:
                        print(
                            "Invalid input! Bus number ebong seats obosshoi songkha hote hobe.")

                elif admin_choice == '2':
                    view_buses()

                elif admin_choice == '3':
                    system.show_pas()
                elif admin_choice == '4':
                    print("Logging out from Admin...")
                    break
                else:
                    print("Invalid choice! Please select between 1 and 4.")
        else:
            print("\nInvalid id")

    elif choice == '2':
        try:
            bus_num = int(input("Enter the bus number : "))
            name = input("Enter your name : ")
            phone = input("Enter your phone : ")
            book_ticket(bus_num, name, phone)
        except ValueError:
            print("Invalid input! Bus number obosshoi songkha hote hobe.")

    elif choice == '3':
        view_buses()
    elif choice == '4':
        print("Exiting the system...")
        break
    else:
        print("Invalid choice! Please select between 1 and 4.")
