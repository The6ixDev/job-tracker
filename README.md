
# 🧠 Job Tracker

A simple full-stack Job Tracker application that allows users to create, read, update, and delete job applications. Built with **React** on the frontend and **Flask** on the backend.

---

## 🚀 Tech Stack

| Layer     | Technology                  |
|-----------|-----------------------------|
| Frontend  | React (Vite)                |
| Backend   | Flask + Flask-CORS          |
| Database  | SQLite                      |
| API       | RESTful CRUD routes         |
| Dev Tools | Git, GitHub, Render.com     |

---

## 📸 Features

- ✅ Add, view, edit, and delete job applications  
- 🔄 Real-time data update with React state  
- 🔗 RESTful API integration  
- 🔒 CORS handled securely for dev environments  
- 🌐 Deployable to services like **Render.com**

---

## 📁 Project Structure

```

job-tracker/
│
├── job-tracker-api/         # Flask backend
│   ├── app.py
│   └── jobtracker.db
│
├── job-tracker-app/         # React frontend
│   └── job-tracker-frontend/
│       ├── src/
│       └── index.html
│
├── .gitignore
└── README.md

````

---

## 🛠️ Getting Started (Local Setup)

### 1️⃣ Backend (Flask API)

```bash
cd job-tracker/job-tracker-api
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt  # if you have one
python app.py
````

Runs locally at: `http://127.0.0.1:5000`

---

### 2️⃣ Frontend (React App)

```bash
cd job-tracker/job-tracker-app/job-tracker-frontend
npm install
npm run dev
```

Runs locally at: `http://localhost:5173`

---

## 🌐 Deployment

This project can be deployed to various sources such as:

* **Frontend:** [Vercel](https://vercel.com/) or [Netlify](https://netlify.com/)
* **Backend:** [Render.com](https://render.com/) or [Fly.io](https://fly.io/)

But please make sure to:

* Allow CORS in Flask
* Set environment variables if needed
* Configure build/start scripts in `render.yaml` or Vercel config

---

## 📦 Future Improvements that can be done

* User authentication (login/signup)
* Pagination and search
* Tagging jobs by status (e.g., Applied, Interview, Offer)
* Export job data (CSV/PDF)

---

## 👨‍💻 Author

Made with ❤️ by [Hamid (The6ix Dev)](https://github.com/The6ixDev)

---

## 📄 License

This project is open source and free to use.


