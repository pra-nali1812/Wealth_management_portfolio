# 💹 Wealth & Portfolio Management System – Project Setup

A full-stack Flask-based system to help users manage investments, track portfolio performance, and receive AI-based investment recommendations using reinforcement learning.

---

## 🧱 Tech Stack

- **Backend**: Flask (Python)
- **Database**: PostgreSQL
- **Frontend**: HTML + JS + Charts (Matplotlib)
- **APIs**: Alpha Vantage (mock), yFinance (mock)
- **AI**: Reinforcement Learning (e.g., Q-Learning for asset allocation)
- **Deployment**: Gunicorn + Nginx

---

## ⚙️ Flask + PostgreSQL Setup

### 1. Install and Setup Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 2. Install Dependencies

```bash
pip install flask flask_sqlalchemy psycopg2-binary matplotlib
```
Run the Project:
```bash
python app.py
```

### 3. PostgreSQL Commands

```sql
-- Login to PostgreSQL
psql -U postgres

-- Create a new database
CREATE DATABASE wealthdb;

-- Create a new user
CREATE USER wealthuser WITH PASSWORD 'securepassword';

-- Grant privileges
GRANT ALL PRIVILEGES ON DATABASE wealthdb TO wealthuser;
```

### 4. Flask DB Config (`config.py`)

```python
SQLALCHEMY_DATABASE_URI = 'postgresql://wealthuser:securepassword@localhost/wealthdb'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = 'your-secret-key'
```

---

## 📁 Project Structure

```
wealth-manager/
├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── models.py
│   ├── portfolio/
│   │   ├── views.py
│   │   └── utils.py
│   ├── ai/
│   │   └── rl_model.py
│   └── templates/
├── static/
├── ml/
│   ├── rl_trainer.py
│   └── model.pkl
├── config.py
├── wsgi.py
└── run.py
```

---

## 🗂️ Flask Apps & Modules

- `portfolio`: Manages user investments, holdings, asset tracking
- `ai`: Handles RL-based investment strategy logic
- `routes`: Main route endpoints
- `models`: DB schema (users, holdings, history)
- `templates/static`: UI and visualization


        self.q_table[s][a] += alpha * (r + gamma * np.max(self.q_table[s_]) - self.q_table[s][a])


## ⚙️ Gunicorn Setup (wsgi.py)

```python
from app import app
if __name__ == "__main__":
    app.run()
```

## 🔐 Nginx Config

```nginx
server {
    listen 80;
    server_name yourdomain.com;

    location / {
        include proxy_params;
        proxy_pass http://unix:/run/wealth.sock;
    }

    location /static/ {
        alias /home/youruser/wealth-manager/static/;
    }
}
```

---

## ✅ Final Deliverables

- ✅ Flask app with PostgreSQL and user management
- ✅ Mocked Alpha Vantage/yFinance integration
- ✅ RL-based investment recommendations
- ✅ Performance graphs and charts
- ✅ Deployed with Gunicorn + Nginx
