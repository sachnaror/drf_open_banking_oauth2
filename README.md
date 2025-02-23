# Django DRF Open Banking API with OAuth2 & OpenID Connect

This project is a **Django REST Framework (DRF) API** for **Open Banking Authentication**, implementing **OAuth2 & OpenID Connect** using `django-oauth-toolkit`. It provides secure banking API endpoints with **token-based authentication**.

## 🚀 Features

✅ **OAuth2 & OpenID Connect** authentication  
✅ **Bank Account API** with balance check & money transfer  
✅ **Token-based API Access** (OAuth2 Bearer Tokens)  
✅ **Secure Permissions & Scopes** for different banking operations  
✅ **SQLite Database** for quick setup  

---

## 🛠️ Installation

### 1️⃣ Clone the Repository

```sh
git clone https://github.com/your-repo/drf-open-banking.git
cd drf-open-banking
```

### 2️⃣ Install Dependencies

```sh
pip install -r requirements.txt
```

### 3️⃣ Run Migrations & Create Superuser

```sh
python manage.py migrate
python manage.py createsuperuser
```

### 4️⃣ Start the Server

```sh
python manage.py runserver
```

---

## 🔑 OAuth2 Authentication Flow

1. **Get Authorization Code:**  
   Open in browser:
   ```sh
   http://127.0.0.1:8000/o/authorize/?client_id=<YOUR_CLIENT_ID>&response_type=code&redirect_uri=http://localhost/callback/
   ```
2. **Exchange Code for Token:**  
   ```sh
   curl -X POST -d "grant_type=authorization_code&code=<AUTH_CODE>&redirect_uri=http://localhost/callback/&client_id=<YOUR_CLIENT_ID>&client_secret=<YOUR_CLIENT_SECRET>" http://127.0.0.1:8000/o/token/
   ```
3. **Use API with Token:**  
   ```sh
   curl -H "Authorization: Bearer <ACCESS_TOKEN>" http://127.0.0.1:8000/api/balance/
   ```

---

## 📌 API Endpoints

| Method | Endpoint             | Description                | Auth Required |
|--------|----------------------|----------------------------|--------------|
| GET    | `/api/balance/`      | Get account balance       | ✅ Yes |
| POST   | `/api/transfer/`     | Transfer money            | ✅ Yes |

---

## 🏆 Contribution

Feel free to submit pull requests to improve the project! 🚀

