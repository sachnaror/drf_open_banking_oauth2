
# Open Banking OAuth2 Application

## 📌 Overview
This app is a **Django REST Framework (DRF) application** that implements **OAuth2 authentication** using `django-oauth-toolkit` for **Open Banking APIs**.

### 🌟 Key Features:
- Implements OAuth2 authentication with **Authorization Code Grant**.
- Supports **PKCE (Proof Key for Code Exchange)** for secure authorization.
- Uses **Django OAuth Toolkit** for access tokens, refresh tokens, and grants.
- Provides **secure API endpoints** for bank transactions.

---

## Directory_Structure

```sh
├── drf_open_banking_oauth2/
│   ├── requirements.txt
│   ├── db.sqlite3
│   ├── README.md
│   ├── manage.py
│   ├── req.py
│   ├── drf_open_banking_oauth2/
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── bank_api/
│   │   ├── urls.py
│   │   └── views.py
│   │   ├── management/
│   │   │   ├── commands/
│   │   │   │   └── populate_oauth.py

```

## 🚀 **1. Setting Up the Project**

### **Step 1: Clone the Repository**
```sh
git clone https://github.com/your-repo/drf_open_banking_oauth2.git
cd drf_open_banking_oauth2
```

### **Step 2: Create a Virtual Environment**
```sh
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### **Step 3: Install Dependencies**
```sh
pip install -r requirements.txt
```

### **Step 4: Apply Migrations**
```sh
python manage.py migrate
```

### **Step 5: Create a Superuser**
```sh
python manage.py createsuperuser
```

---

## 🏗 **2. Configuring OAuth2 in Django**

### **Step 6: Update `settings.py`**

Ensure `INSTALLED_APPS` includes:
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'oauth2_provider',  # OAuth2 support
    'rest_framework',
    'bank_api',
]
```

Enable OAuth2 settings:
```python
OAUTH2_PROVIDER = {
    'ACCESS_TOKEN_EXPIRE_SECONDS': 3600,
    'REFRESH_TOKEN_EXPIRE_SECONDS': 86400,
    'PKCE_REQUIRED': True,  # Ensure PKCE is enabled for security
    'SCOPES': {
        'read': 'Read your data',
        'write': 'Modify your data',
        'payments': 'Initiate payments'
    }
}
```

---

## 🔗 **3. Registering OAuth2 Applications**

### **Step 7: Create an OAuth2 Application**
1. **Go to Django Admin** (`http://127.0.0.1:8000/admin/`).
2. Navigate to **OAuth2 Provider → Applications**.
3. **Create a new application** with:
   - **Client Type:** `Confidential`
   - **Authorization Grant Type:** `Authorization Code`
   - **Redirect URIs:**
     ```
     http://127.0.0.1:8000/callback/
     http://localhost/callback/
     ```
   - **Scope:** `read write payments`

4. **Save and copy the Client ID & Secret.**

---

## 🧪 **4. Testing OAuth2 Authorization Flow**

### **Step 8: Request Authorization Code**
#### **Method 1: Open in Browser**
```
http://127.0.0.1:8000/o/authorize/?client_id=YOUR_CLIENT_ID&response_type=code&redirect_uri=http://127.0.0.1:8000/callback/&code_challenge=YOUR_CODE_CHALLENGE&code_challenge_method=S256
```

#### **Method 2: Using cURL**
```sh
curl -X GET "http://127.0.0.1:8000/o/authorize/?client_id=YOUR_CLIENT_ID&response_type=code&redirect_uri=http://127.0.0.1:8000/callback/&code_challenge=YOUR_CODE_CHALLENGE&code_challenge_method=S256"
```

✅ You will be redirected to login. After login, **copy the `code` from the URL.**

---

### **Step 9: Exchange Authorization Code for an Access Token**
```sh
curl -X POST "http://127.0.0.1:8000/o/token/"      -d "grant_type=authorization_code"      -d "code=YOUR_AUTHORIZATION_CODE"      -d "redirect_uri=http://127.0.0.1:8000/callback/"      -d "client_id=YOUR_CLIENT_ID"      -d "client_secret=YOUR_CLIENT_SECRET"      -d "code_verifier=YOUR_CODE_VERIFIER"
```
✅ **Response Example:**
```json
{
  "access_token": "your_access_token",
  "expires_in": 3600,
  "token_type": "Bearer",
  "refresh_token": "your_refresh_token",
  "scope": "read write payments"
}
```

---

## 💳 **5. Testing API Endpoints with Access Token**

### **Step 10: Get Account Balance**
```sh
curl -X GET "http://127.0.0.1:8000/api/balance/"      -H "Authorization: Bearer your_access_token"
```
✅ **Expected Response:**
```json
{
  "balance": "₹1,00,000",
  "currency": "INR"
}
```

### **Step 11: Transfer Money**
```sh
curl -X POST "http://127.0.0.1:8000/api/transfer/"      -H "Authorization: Bearer your_access_token"      -H "Content-Type: application/json"      -d '{"amount": 5000}'
```
✅ **Expected Response:**
```json
{
  "message": "₹5000 transferred successfully!"
}
```

---

## 🔄 **6. Refreshing an Expired Access Token**
```sh
curl -X POST "http://127.0.0.1:8000/o/token/"      -d "grant_type=refresh_token"      -d "refresh_token=your_refresh_token"      -d "client_id=YOUR_CLIENT_ID"      -d "client_secret=YOUR_CLIENT_SECRET"
```
✅ **Response Example:**
```json
{
  "access_token": "new_access_token",
  "expires_in": 3600,
  "token_type": "Bearer",
  "refresh_token": "new_refresh_token",
  "scope": "read write payments"
}
```

---

## 🔒 **7. Revoking Access Token (Logout)**
```sh
curl -X POST "http://127.0.0.1:8000/o/revoke_token/"      -d "token=your_access_token"      -d "client_id=YOUR_CLIENT_ID"      -d "client_secret=YOUR_CLIENT_SECRET"
```
✅ **Expected Response:**
```json
{
  "status": "revoked"
}
```

---

## 📢 **Conclusion**
🎯 You have successfully implemented **OAuth2 authentication with Django OAuth Toolkit** for an **Open Banking API**.

✅ Now, you can:
- Securely authenticate users with **OAuth2 Authorization Code Flow**.
- Test your API endpoints with **Bearer Tokens**.
- Refresh or revoke tokens as needed.



## 📩 Contact

| Name              | Details                             |
|-------------------|-------------------------------------|
| **👨‍💻 Developer**  | Sachin Arora                      |
| **📧 Email**       | [sachnaror@gmail.com](mailto:sachnaror@gmail.com) |
| **📍 Location**    | Noida, India                       |
| **📂 GitHub**      | [github.com/sachnaror](https://github.com/sachnaror) |
| **🌐 Website**     | [https://about.me/sachin-arora](https://about.me/sachin-arora) |
| **📱 Phone**       | [+91 9560330483](tel:+919560330483) |
