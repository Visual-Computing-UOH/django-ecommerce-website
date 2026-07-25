Django E-Commerce Website

A full-stack e-commerce web application built with **Django**. The front-end UI was based on an open-source template (customized for this project), and the entire **backend — models, authentication, cart, checkout, orders, and admin management — was built from scratch**.

This was my first full-stack web development project, built to understand how a real-world backend actually connects to a front-end.



## 🚀 Features

* **User Authentication** — signup, login, logout (Django's built-in auth system)
* **Product Catalog** — 8 categories (Men's Fashion, Women's Fashion, Electronics, Jewellery, Footwear, Cosmetics, Perfume, Bags & Accessories)
* **Dynamic Homepage Sections** — Best Sellers, New Arrivals, Trending, Top Rated, Deal of the Day
* **Category-based Filtering** — browse products by category
* **Hot Offers Page** — automatically lists discounted products (based on `old_price`)
* **Session-based Shopping Cart** — add, remove, update quantity without needing to log in
* **Checkout Flow** — collects shipping details and places an order
* **Order History** — logged-in users can view their past orders
* **Django Admin Panel** — full product/category/order management without touching code
* **Blog Page** — placeholder section for future content

---

## 🛠️ Tech Stack

| Layer          | Technology                         |
|----------------|-------------------------------------|
| Backend        | Django 6.0                          |
| Database       | SQLite (default, easy to swap)      |
| Frontend       | HTML, CSS, JavaScript (customized template) |
| Image Handling | Pillow                              |
| Language       | Python 3                            |

---

## 📁 Project Structure

```
djecommerce_updated/
├── ecommerce/          # Project settings, URLs, WSGI
├── store/              # Main app — models, views, urls, admin
│   ├── models.py       # Category, Product, Order, OrderItem
│   ├── views.py        # Home, cart, checkout, auth, orders
│   ├── urls.py
│   └── admin.py
├── templates/           # HTML templates (base, index, cart, checkout, etc.)
├── static/               # CSS, JS, images, icons
├── media/products/      # Uploaded product images
├── add_categories.py    # Script to bulk-add categories
├── add_products.py      # Script to bulk-add sample products
└── manage.py
```

---

## ⚙️ Setup & Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/<your-username>/<repo-name>.git
   cd djecommerce_updated
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate      # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser (for the admin panel)**
   ```bash
   python manage.py createsuperuser
   ```

6. **(Optional) Load sample categories & products**
   ```bash
   python add_categories.py
   python add_products.py
   ```

7. **Run the development server**
   ```bash
   python manage.py runserver
   ```

8. Visit `http://127.0.0.1:8000/` for the store, and `http://127.0.0.1:8000/admin/` for the admin panel.

---

## 🧩 Adding Products (Admin Panel)

Products can be added without writing any code:

1. Go to `/admin/` and log in with your superuser account
2. Click **Products → Add Product**
3. Fill in name, price, category, description
4. Upload a product image
5. Check any of the flags (`Best Seller`, `New Arrival`, `Trending`, `Top Rated`, `Deal of Day`) to feature it on the homepage
6. Save — it appears on the site instantly

---

## 🐞 Problems Faced & What I Learned

* **URL routing & templates** — Learned how `urls.py → views.py → templates` connect the full request-response cycle in Django's MVT architecture, and debugged broken navigation links / missing templates that caused page crashes.
* **Database persistence** — Verified that Category/Product data actually persists across server restarts by testing migrations and the SQLite database directly, reinforcing how Django's ORM maps models to real database tables.
* **Session-based cart** — Implemented a cart system that works for both guest and logged-in users using Django sessions.
* **Category filtering without slugs** — Filtered products by category using Django's ORM lookups (`category__id`, `name__icontains`) instead of building a separate slug system.
* **Admin customization** — Registered models in `admin.py` with custom list filters and search fields to make product management fast and code-free.

---


## 👩‍💻 Author

**Saira Bibi**
BS Artificial Intelligence, University of Haripur


