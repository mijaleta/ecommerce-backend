# E-Commerce Backend API

[![Python](https://img.shields.io/badge/Python-5.1.4-blue.svg)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-5.1.4-green.svg)](https://www.djangoproject.com/)
[![DRF](https://img.shields.io/badge/DRF-3.16.1-orange.svg)](https://www.django-rest-framework.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A robust **Django REST Framework** backend for an e-commerce platform. Features user authentication (JWT), product catalog, shopping cart, order management, and admin interface. Deployed-ready for Render.com with PostgreSQL support.

## ✨ Features
- **Authentication**: JWT tokens with custom `User` model (email, phone, profile picture, roles: admin/customer).
- **Products**: CRUD operations, categories, images, stock management.
- **Cart**: User-specific cart with items (quantity, price).
- **Orders**: Full order lifecycle with order items, shipping info, total pricing.
- **Admin Panel**: Django admin for all models.
- **Media Upload**: Product/profile images.
- **CORS**: Supports frontend integration (Vite/React at localhost:5173).
- **API Documentation**: Auto-generated via DRF browsable API.

## 📋 API Endpoints
Base URL: `http://localhost:8000/api/`

| Endpoint | Methods | Description |
|----------|---------|-------------|
| `/token/` | POST | Login (obtain JWT tokens) |
| `/token/refresh/` | POST | Refresh access token |
| `/users/` | GET, POST | List/Create users |
| `/products/` | GET, POST | List/Create products |
| `/cart/` | GET, POST, DELETE | User cart management |
| `/cart/items/` | GET, POST, DELETE | Cart items CRUD |
| `/orders/` | GET, POST | User orders |

**Auth**: Include `Authorization: Bearer <access_token>` header for protected routes.

Example login:
```bash
curl -X POST http://localhost:8000/api/token/ -d "email=admin@gmail.com&password=admin@123"
```

## 🚀 Quick Start (Development)

1. **Clone & Setup**
   ```bash
   git clone <repo-url>
   cd ecommerce-backend
   ```

2. **Virtual Environment**
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # macOS/Linux
   source venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Variables** (`.env` or local):
   ```
   DB_ENGINE=django.db.backends.sqlite3  # or postgresql
   DB_NAME=your_db
   DB_USER=your_user
   DB_PASSWORD=your_pass
   DB_HOST=localhost
   DB_PORT=5432
   DJANGO_SECRET_KEY=your-secret-key
   ```

5. **Migrations & Superuser**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   python manage.py createsuperuser  # or visit /create-superuser/
   ```

6. **Run Server**
   ```bash
   python manage.py runserver
   ```
   Visit `http://localhost:8000/api/` (browsable API) or `http://localhost:8000/admin/`.

## 🛠️ Admin Login
- Email: `admin@gmail.com`
- Password: `admin@123`
- Endpoint: `http://create-superuser/` to recreate.

## ☁️ Deployment (Render.com)
1. Fork repo & connect to Render.
2. Add PostgreSQL service.
3. Set env vars from `render.yaml`.
4. Deploy!

## 📁 Project Structure
```
ecommerce-backend/
├── apps/
│   ├── users/     # Custom User, auth views
│   ├── products/  # Product models/serializers
│   ├── cart/      # Cart & items
│   └── orders/    # Orders, shipping
├── config/        # Django settings/urls
├── media/         # Uploaded images
├── requirements.txt
├── render.yaml
└── manage.py
```

## 🔧 Tech Stack
- **Backend**: Django 5.1.4, DRF 3.16.1
- **Auth**: SimpleJWT 5.5.1
- **DB**: SQLite (dev) / PostgreSQL (prod)
- **Images**: Pillow
- **Deployment**: Gunicorn + Render

## 🤝 Contributing
1. Fork & PR.
2. Run `python manage.py test`.
3. Follow PEP8.

## 📄 License
MIT License - see [LICENSE](LICENSE) file.

---

*Built with ❤️ for portfolio projects.*

