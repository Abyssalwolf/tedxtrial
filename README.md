# 🔐 Django Auth API

A secure and extensible authentication API built with Django, JWT, and Google OAuth.  
Deployed on Render, using Supabase as the PostgreSQL database.

> ✅ **Live Demo:** [https://tedxtrial.onrender.com](https://tedxtrial.onrender.com)

---

## 📌 Features

- ✅ Email & Password Signup/Login
- ✅ JWT-based Authentication
- ✅ Token Refresh
- ✅ Role-Based Access (User/Admin)
- ✅ Google OAuth Integration (Optional)
- ✅ Hosted on Render (Free Tier)

---

## 🚀 Base URL

```
https://tedxtrial.onrender.com
```

All API endpoints are prefixed with `/api/auth/`

---

## 📬 API Endpoints & How to Test

---

### 🔸 Register a New User

**POST** `/api/auth/register/`

**Request Body:**
```json
{
  "username": "johndoe",
  "email": "john@example.com",
  "password": "secret123"
}
```

**Response:**
```json
{
  "username": "johndoe",
  "email": "john@example.com"
}
```

---

### 🔸 Login (Obtain JWT Tokens)

**POST** `/api/auth/login/`

**Request Body:**
```json
{
  "username": "johndoe",
  "password": "secret123"
}
```

**Response:**
```json
{
  "refresh": "<refresh_token>",
  "access": "<access_token>"
}
```

---

### 🔸 Refresh Access Token

**POST** `/api/auth/token/refresh/`

**Request Body:**
```json
{
  "refresh": "<your_refresh_token>"
}
```

**Response:**
```json
{
  "access": "<new_access_token>"
}
```

---

### 🔒 User-Only Route

**GET** `/api/auth/user/`

**Headers:**
```
Authorization: Bearer <access_token>
```

**Response:**
```json
{
  "message": "Hello, johndoe! You are a user."
}
```

---

### 🔒 Admin-Only Route

**GET** `/api/auth/admin/`

**Headers:**
```
Authorization: Bearer <access_token>
```

**Response if Admin:**
```json
{
  "message": "Hello Admin johndoe!"
}
```

**Response if Not Admin:**
```json
{
  "error": "Admins only!"
}
```

---

## 🧪 How to Test

You can use:

- [Postman](https://www.postman.com/)
- [Insomnia](https://insomnia.rest/)
- Curl from the terminal

**Example curl test:**
```bash
curl -X POST https://tedxtrial.onrender.com/api/auth/login/   -H "Content-Type: application/json"   -d '{"username": "johndoe", "password": "secret123"}'
```

---

## 🛡️ Admin Role Setup

To make a user an admin, open Django shell or use Django Admin:

```python
from django.contrib.auth.models import User
u = User.objects.get(username="johndoe")
u.is_staff = True
u.save()
```

---

## 🌐 Google Sign-In (Optional)

If enabled and configured:

**GET** `/dj-rest-auth/google/login/`  
Redirects to Google for OAuth login, returns a valid token upon success.

> ⚠️ Requires setting up credentials in Google Developer Console and adding redirect URI:  
`https://tedxtrial.onrender.com/dj-rest-auth/google/login/callback/`

---

## 🏠 Root Health Check

**GET** `/`

**Response:**
```json
{
  "message": "Django Auth API is live 🎉"
}
```

---

## 🧰 Built With

- [Django](https://www.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [Simple JWT](https://django-rest-framework-simplejwt.readthedocs.io/)
- [dj-rest-auth](https://github.com/iMerica/dj-rest-auth)
- [Supabase](https://supabase.com/) (PostgreSQL)
- [Render](https://render.com/) (Free Tier Hosting)

---

## 📂 Project Structure

```
project-root/
├── tedx/                  # Django project (has settings.py, wsgi.py)
├── accounts/              # Authentication app
├── manage.py
├── requirements.txt
├── Procfile               # gunicorn startup command
├── .env                   # Environment variables (not committed)
```

---

## 🛠️ Deployment Notes (Render)

**Procfile:**
```
web: gunicorn tedx.wsgi:application --bind 0.0.0.0:$PORT
```

**Start Command (Render Dashboard):**
```
gunicorn tedx.wsgi:application --bind 0.0.0.0:$PORT
```

---

## 📄 License

MIT – Use freely for learning, testing, and building projects.  
Please attribute if extended.

---