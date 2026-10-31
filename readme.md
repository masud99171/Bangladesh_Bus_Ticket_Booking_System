# 🚌 Bangladesh Bus Ticket Booking System

A command-line interface (CLI) based Bus Ticket Management System built with Python using Object-Oriented Programming (OOP) principles. This application allows administrators to manage bus fleets and passenger lists, while general users can view available buses and book tickets.

---

## ✨ Features

### 👤 User Features
- **View Available Buses:** Check bus numbers, routes, and real-time seat availability.
- **Book Tickets:** Book seats on a specific bus by providing a name and phone number (Fixed flat rate: `৳500` per ticket).
- **Real-Time Validation:** Prevents booking on full buses or non-existent bus numbers.

### 🛠️ Admin Features
- **Secure Login:** Password-protected access to the admin dashboard.
- **Add New Buses:** Register new buses with unique bus numbers, routes, and seat capacities.
- **Duplicate Prevention:** Automatically checks and blocks duplicate bus numbers.
- **View All Buses:** Overview of all registered buses and remaining seats.
- **View Passenger List:** Detailed list of all booked passengers, their contact info, assigned bus, route, and fare.

---

## 🏗️ Code Structure (OOP)

The system is modularized into four core classes:

| Class | Responsibility |
| :--- | :--- |
| `Bus` | Manages individual bus details (`number`, `route`, `total_seats`, `booked_seats`) and seat availability calculations. |
| `Passenger` | Stores passenger details (`name`, `phone`) and links them to their booked `Bus` object. |
| `BusSystem` | Acts as the central database storing lists of buses and passengers, handling display formatting, and managing default fare (`৳500`). |
| `Admin` | Handles administrator authentication and interfaces with `BusSystem` to add new buses. |

---

## 🚀 Getting Started

### Prerequisites
- Python 3.x installed on your system.
- Git installed on your system.

### Installation & Execution

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/masud99171/Bangladesh_Bus_Ticket_Booking_System.git](https://github.com/masud99171/Bangladesh_Bus_Ticket_Booking_System.git)
   ```

2. **Navigate to the project directory:**
   ```bash
   cd Bangladesh_Bus_Ticket_Booking_System
   ```

3. **Run the application:**
   ```bash
   python bus.py
   ```

---

## 🔐 Default Admin Credentials

To access the **Admin Menu** (Option `1` from the main menu), use the following hardcoded credentials:

- **Username:** `admin`
- **Password:** `1234`

---

## 💻 Usage Example

```text
--- User Menu ---
1. Admin Login
2. Book Ticket
3. View Buses
4. Exit
Enter your choice (1-4): 1
Enter the name :admin
Enter the password :1234

--- Admin Menu ---
1. Add Bus
2. View All Buses
3. View All passengers
4. Logout
Enter your choice (1-4): 1
Enter the bus number : 101
Enter the route : Dhaka to Rajshahi
Enter total seats : 40
Bus 101 successfully add kora hoyeche!
```

---

## 🛡️ Error Handling
- **Input Validation:** Handles `ValueError` exceptions if non-numeric values are entered for bus numbers or seat counts.
- **Capacity Checks:** Ensures buses cannot be created with `0` or negative seats, and prevents overbooking when available seats reach `0`.

---

## 🔗 Repository Link
- **Source Code:** [bus.py](https://github.com/masud99171/Bangladesh_Bus_Ticket_Booking_System)
