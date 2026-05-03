<div align="center">

# 💈 Barber Shop

### *A sleek, full-stack barbershop booking web app built with Python & Flask*

[![Python](https://img.shields.io/badge/-Python-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![Flask](https://img.shields.io/badge/-Flask-000000?style=flat-square&logo=flask&logoColor=white)](https://flask.palletsprojects.com)
[![HTML5](https://img.shields.io/badge/-HTML5-E34F26?style=flat-square&logo=html5&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/HTML)
[![Stripe](https://img.shields.io/badge/-Stripe-635BFF?style=flat-square&logo=stripe&logoColor=white)](https://stripe.com)
[![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=flat-square)]()

</div>

---

## 📌 Overview

**Barber Shop** is a modern, responsive booking platform for a premium barbershop experience. Customers can browse services, choose their barber, select an appointment slot, and complete a simulated payment — all from one clean interface powered by a Flask REST backend.

---

## ✨ Features

- 💇 **Service Catalog** — 6 premium services with pricing, duration & descriptions
- 👨‍💼 **Barber Profiles** — Choose from 3 specialists with listed expertise
- 📅 **Appointment Booking** — Full daily time-slot scheduling (9 AM – 6 PM)
- 💳 **Payment Flow** — Demo Stripe integration ready for production wiring
- 🔌 **REST API** — Clean JSON endpoints for all booking & payment operations
- ⚡ **Lightweight** — Single-file Flask backend, zero database setup required

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| **Backend** | Python, Flask |
| **Frontend** | HTML5, CSS3, JavaScript (Jinja2 templates) |
| **Payments** | Stripe (demo mode) |
| **Storage** | In-memory (upgradeable to SQLite / PostgreSQL) |

---

## 📁 Project Structure

```
💈 Barber_shop/
├── 📄 app.py               # Flask app & all API routes
├── 📄 requirements.txt     # Python dependencies
└── 📂 templates/
    └── 📄 index.html       # Main frontend template
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- pip

### Installation

```bash
# 1. Clone the repo
git clone https://github.com/Ammarahmed-git/Barber_shop.git
cd Barber_shop

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the app
python app.py
```

> 🌐 App runs at **http://localhost:5000**

---

## 💇 Services Menu

| ✂️ Service | 💰 Price | ⏱️ Duration | 📝 Description |
|---|---|---|---|
| Classic Cut | $35 | 30 min | Precision scissor cut with styling |
| Fade & Taper | $45 | 45 min | Sharp fade with seamless blend |
| Hot Towel Shave | $40 | 40 min | Traditional straight razor experience |
| Beard Sculpt | $30 | 30 min | Defined shape & expert grooming |
| 👑 Royal Package | $95 | 90 min | Cut + Shave + Beard + Styling |
| Hair Color | $65 | 60 min | Premium coloring & highlights |

---

## 👨‍💼 Meet the Barbers

| | Name | Specialty | Experience |
|---|---|---|---|
| ✂️ | **Marcus Steel** | Fades & Tapers | 12 Years |
| 💈 | **Diego Reyes** | Classic Cuts | 8 Years |
| 🪒 | **Jax Thornton** | Beard Artistry | 10 Years |

---

## 📡 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/` | Renders the main booking page |
| `GET` | `/api/services` | Returns all available services |
| `GET` | `/api/bookings` | Returns all current bookings |
| `POST` | `/api/book` | Creates a new appointment |
| `POST` | `/api/payment/create-intent` | Creates a payment intent (demo) |
| `POST` | `/api/payment/confirm` | Confirms a payment (demo) |

### 📬 Example Booking Request

```json
POST /api/book
{
  "name": "John Doe",
  "email": "john@example.com",
  "phone": "555-1234",
  "service": "Fade & Taper",
  "barber": "Marcus Steel",
  "date": "2025-06-15",
  "time": "10:00 AM",
  "price": 45
}
```

### ✅ Example Response

```json
{
  "success": true,
  "booking_id": 1,
  "message": "Booking confirmed!"
}
```

---

## ⚠️ Production Checklist

> Before going live, make sure to address the following:

- 🗄️ **Database** — Replace the in-memory `bookings` list with a persistent DB (SQLite, PostgreSQL, etc.)
- 💳 **Stripe** — Swap demo payment routes with real `stripe.PaymentIntent.create()` calls
- 🔐 **Secret Key** — Store `app.secret_key` in an environment variable, never hardcoded
- 🌐 **Deployment** — Use a production WSGI server like Gunicorn behind Nginx

---

## 📬 Connect with Me

<div align="center">

[![LinkedIn](https://img.shields.io/badge/-LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://pk.linkedin.com/in/ammar-ahmed-1606a1242)
[![GitHub](https://img.shields.io/badge/-GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Ammarahmed-git)
[![Portfolio](https://img.shields.io/badge/-Portfolio-ff6b6b?style=for-the-badge&logo=firefox&logoColor=white)](https://ammarahmed-git.github.io/Portfolio/)
[![Gmail](https://img.shields.io/badge/-Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:Innoxentammar27@gmail.com)

</div>

---

<div align="center">

*Built with ❤️ by [Ammar Ahmed](https://github.com/Ammarahmed-git)*

</div>
