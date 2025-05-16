# 📘 SkillConnect – A Service Provider Marketplace

SkillConnect is a full-stack Python-based web app where users can register, post services, and browse service providers.

## 🚀 Features
- 🔐 User registration
- 🛠️ Create and browse services
- 🧾 REST API using FastAPI
- 🎨 Simple Bootstrap frontend
- 🗃️ SQLite DB (easy to upgrade to PostgreSQL)

## 🛠️ Tech Stack
- **Backend:** Python, FastAPI, SQLAlchemy
- **Frontend:** HTML, CSS, JS (Bootstrap)
- **Database:** SQLite (default), PostgreSQL (optional)

## 🧑‍💻 Installation & Run

### 1. Clone the repo
```bash
git clone https://github.com/yourusername/skillconnect.git
cd skillconnect
```

### 2. Create and activate virtualenv
```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

### 3. Install dependencies
```bash
pip install fastapi uvicorn sqlalchemy pydantic
```

### 4. Run the server
```bash
uvicorn main:app --reload
```

## 🌐 Use the frontend
Open `index.html` in your browser. Backend must run on `localhost:8000`.

## 🧪 Test API (Optional)
- POST /register
- POST /services
- GET /services