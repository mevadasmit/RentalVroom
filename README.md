# RentalVroom
RentalVroom - Car Rental System  RentalVroom is a modern web-based car rental management system designed to provide a seamless experience for customers looking to rent vehicles.
Built using Django, Bootstrap, and W3.CSS, this project offers a user-friendly interface, secure transactions, and efficient inventory management for car rental businesses.

📌 Features
🔹 Customer Portal
✅ User authentication and session management
✅ Search and browse available cars
✅ View detailed car specifications (name, color, capacity, description, location)
✅ Book a car for a specific number of days
✅ Manage active bookings and view order history
✅ Cancel or modify bookings
✅ View total rent, duration, and car dealer details
✅ Logout functionality

🔹 Car Dealer Management
✅ Car dealers can list available vehicles for rent
✅ View booking requests from customers
✅ Manage vehicle inventory and update car details

🔹 Admin Panel
✅ Add, update, and remove vehicles from inventory
✅ View and manage customer bookings
✅ Track revenue and rental statistics

📂 Project Structure
🔹 Main Django Apps
- Customer Portal (customer_portal) ==> Handles customer interactions
- Car Dealer (car_dealer) ==> Manages car listings and rental processes
- Admin (admin_panel) ==> Provides control over the system

🛠️ Tech Stack

Frontend: HTML, CSS (Bootstrap & W3.CSS)
Backend: Django (Python-based web framework)
Database: SQLite (default, can be switched to PostgreSQL or MySQL)

🚀 How to Run the Project

🔹 Installation Steps

Clone the Repository
git clone https://github.com/mevadasmit/RentalVroom.git
cd RentalVroom

Create & Activate a Virtual Environment
python -m venv env
source env/bin/activate   # For Linux/Mac
env\Scripts\activate      # For Windows


Install Dependencies
pip install -r requirements.txt

Apply Migrations
python manage.py migrate


Create a Superuser (for Admin Panel)
python manage.py createsuperuser


Run the Development Server
python manage.py runserver

Open in Browser
http://127.0.0.1:8000/

👨‍💻 Contributors
MEVADA SMIT (Project Lead)
