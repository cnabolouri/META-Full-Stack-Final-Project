# META-Full-Stack-Final-Project (Little Lemon)

Full-stack **Django** app for Little Lemon with a browsable website **and** a **DRF** API.  
Users can sign up / sign in, make reservations, view **their own** reservations, and browse the menu.

---

## ✨ Features

- Django templates for the public site (Home, About, Menu, Booking)
- Auth (signup / login / logout) and an **Account** area
- Reservations tied to the logged-in user (users **cannot** see other users’ bookings)
- DRF API for Menu & Bookings (CRUD), browsable UI, filtering & pagination
- Django Admin for managing content

---

## 🔧 Requirements

- Python **3.10+** (3.12+ recommended)
- pip
- SQLite (default). You can swap to MySQL/PostgreSQL later.

---

## 🚀 Quick Start

```bash
# 1) Clone
git clone https://github.com/cnabolouri/META-Full-Stack-Final-Project.git
cd META-Full-Stack-Final-Project/LittleLemon

# 2) Create & activate a virtual environment
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
# source .venv/bin/activate

# 3) Install dependencies
pip install -r requirements.txt
# If missing, minimally:
# pip install django djangorestframework

# 4) Migrate
python manage.py makemigrations
python manage.py migrate

# 5) Create an admin user
python manage.py createsuperuser

# 6) Run
python manage.py runserver
```
Open: http://127.0.0.1:8000/

🗂️ App URLs (Pages)
Path	URL name	Notes
/	home	Landing page
/about/	about	About the restaurant
/book/	book	Booking form (login required to submit)
/menu/	menu	Menu listing
/menu_item/<int:pk>/	menu_item	Single menu item
/reservations/	reservations	Styled list of your reservations (login required)
/account/	account	Account area: profile, reservations, sign out
/admin/	—	Django admin
Auth
Path	URL name	Notes
/accounts/login/	login	Sign in
/accounts/logout/	logout	Sign out
/accounts/signup/	signup	Register
🔌 API (Django REST Framework)

Base: /api/ (Browsable API available if DEBUG=True)

Menu
Endpoint	Methods	URL name
/api/menu/	GET, POST	api_menu_list
/api/menu/<int:pk>/	GET, PUT, PATCH, DELETE	api_menu_detail
Bookings
Endpoint	Methods	URL name	Notes
/api/bookings/	GET, POST	api_booking_list	Returns only the authenticated user’s bookings. Supports ?date=YYYY-MM-DD.
/api/bookings/<int:pk>/	GET, PUT, PATCH, DELETE	api_booking_detail	Auth required; can only access your own records.

If you enabled DRF routers, you may also see router-style paths (e.g. ^menu/$, ^bookings/$) in the browsable API; they map to the same views.

Filtering & Pagination

Bookings by date: GET /api/bookings/?date=2025-10-15

Pagination: ?page=2
If dynamic page size is enabled: ?page_size=10.

Sample Requests
# List menu items
curl -s http://127.0.0.1:8000/api/menu/

# Create a booking (must be authenticated)
curl -X POST http://127.0.0.1:8000/api/bookings/ \
  -H "Content-Type: application/json" \
  -d '{"reservation_date":"2025-10-15","reservation_time":"10:00","guest_number":2,"comment":"Window seat"}'

🔐 Auth & Permissions

Website: login required for booking and for viewing your reservations.

API: write operations require auth; bookings are user-scoped (you only see yours).

If you later add token auth (e.g., DRF Token or Djoser), document the token endpoints here.

🛠️ Dev Tips

Admin: create categories, menu items, and view all bookings at /admin/.

Static files: ensure django.contrib.staticfiles is in INSTALLED_APPS and templates load static via {% load static %}.

Migrations (when models change):

python manage.py makemigrations
python manage.py migrate


Tests (if present):

python manage.py test

🗃️ Database

Default: SQLite (db.sqlite3).
Switching to MySQL/PostgreSQL? Update DATABASES in settings.py and install the driver (e.g., mysqlclient or psycopg2-binary), then re-run migrations.

🔗 Quick Links

Pages

Admin — http://127.0.0.1:8000/admin/

Home — http://127.0.0.1:8000/ (home)

About — http://127.0.0.1:8000/about/ (about)

Book — http://127.0.0.1:8000/book/ (book)

Menu — http://127.0.0.1:8000/menu/ (menu)

Menu Item — http://127.0.0.1:8000/menu_item/1/ (menu_item)

Reservations — http://127.0.0.1:8000/reservations/ (reservations)

Account — http://127.0.0.1:8000/account/ (account)

Auth

Login — http://127.0.0.1:8000/accounts/login/ (login)

Logout — http://127.0.0.1:8000/accounts/logout/ (logout)

Signup — http://127.0.0.1:8000/accounts/signup/ (signup)

API

Menu list — http://127.0.0.1:8000/api/menu/ (api_menu_list)

Menu detail — http://127.0.0.1:8000/api/menu/1/ (api_menu_detail)

Bookings list — http://127.0.0.1:8000/api/bookings/ (api_booking_list)

Bookings detail — http://127.0.0.1:8000/api/bookings/1/ (api_booking_detail)

Filter bookings by date — http://127.0.0.1:8000/api/bookings/?date=2025-10-15

🧭 Project Notes

Prefer one models app (e.g., restaurant) and expose APIs from a separate api app to avoid migration conflicts.

Users cannot view or edit other users’ bookings.

The Reservations tab renders a styled list, not raw JSON.

The Book page prevents selecting time slots already taken for the selected date.
