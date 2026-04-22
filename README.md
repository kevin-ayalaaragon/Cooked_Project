# 🍳 Cooked

A full-stack Django web app for discovering, sharing, and tracking recipes. Browse a global feed of trending dishes, follow your favorite chefs, and build your personal cookbook — no account required to explore, but sign up to unlock the full experience.

**🔗 Live Demo:** [cooked-app-4kof.onrender.com](https://cooked-app-4kof.onrender.com/)

---

## What This Is

Cooked is a recipe social platform built to go beyond a simple recipe list. Users can follow friends and chefs, track which recipes they've actually tried, earn badges for cooking milestones, and see what's trending across the community in real time.

This project was an exercise in building a data-driven social app end-to-end — user authentication, relational data modeling (followers, favorites, badges), dynamic search and filtering, and deployment to a production PostgreSQL environment on Render.

---

## Features

- 🔍 **Recipe search & browse** — search and filter recipes without an account
- 📈 **Trending feed** — global view of the most popular and recently reviewed recipes
- ❤️ **Favorites** — save recipes to your personal collection
- 👨‍🍳 **Follow chefs** — follow friends and chefs to see their recipes and activity
- ✅ **Tried it tracking** — mark recipes you've actually cooked
- 🏅 **Badges** — earn achievements based on cooking milestones
- ⭐ **Reviews** — read and leave reviews on any recipe
- 🔐 **Auth** — browse publicly, sign up to unlock social and personal features

---

## Tech Stack

| Layer | Tool |
|---|---|
| Backend | Django 4.2 |
| Frontend | Bootstrap 5 + vanilla JS |
| Database | PostgreSQL (Render) |
| Static files | WhiteNoise |
| Hosting | Render |
| Web server | Gunicorn |

---

## Local Setup

```bash
# 1. Clone the repo and create a virtual environment
git clone https://github.com/kevin-ayalaaragon/Cooked_Project.git
cd Cooked_Project
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Copy env file and configure
cp .env.example .env
# Set DATABASE_URL to a local PostgreSQL instance or use SQLite for dev

# 4. Run migrations
python manage.py migrate

# 5. Run the development server
python manage.py runserver
```

Open [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser.

---

## Deployment (Render)

1. Push to GitHub and create a new **Web Service** on Render
2. Create a **PostgreSQL** database on Render and copy the Internal Database URL
3. **Build command:** `pip install -r requirements.txt && python manage.py collectstatic --noinput`
4. **Start command:** `gunicorn Cooked.wsgi --bind 0.0.0.0:$PORT`
5. **Environment variables:**
   - `SECRET_KEY` — Django secret key
   - `DEBUG=False`
   - `DATABASE_URL` — Internal Database URL from Render PostgreSQL
   - `ALLOWED_HOSTS=your-domain.onrender.com`
6. After deploy, run migrations via the Shell tab: `python manage.py migrate`

---

## Topics

`django` · `python` · `postgresql` · `bootstrap` · `recipes` · `social-app` · `web-app` · `render` · `authentication`