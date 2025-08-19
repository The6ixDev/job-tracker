import os

from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})
# Allow this origins (for development)


# Setup database connectivity:

# get abs path of where  we are with app.py

basedir = os.path.abspath(os.path.dirname(__file__))

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + \
    os.path.join(basedir, "jobtracker.db")

# unnecessary feature causing warning now,we dont want that

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company = db.Column(db.String(100), nullable=False)
    position = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(50), nullable=False)
    date_applied = db.Column(db.String(100), nullable=True)

    def __repr__(self):
        return f"<Job {self.id} - {self.company} - {self.position}>"


# route from home to / to this method here


@app.route("/")
def home():
    return "Welcome to my Job Tracker API"

# Post Request aka CREATE


@app.route("/jobs", methods=["POST"])
def add_job():
    data = request.get_json()

    # Validate input
    if not data or not all(k in data for k in ("company", "position", "status")):
        return jsonify({"error": "Missing required fields"}), 400

    new_job = Job(
        company=data["company"],
        position=data["position"],
        status=data["status"],
        date_applied=data.get("date_applied")  # optional
    )

    db.session.add(new_job)
    db.session.commit()

    return jsonify({
        "id": new_job.id,
        "company": new_job.company,
        "position": new_job.position,
        "status": new_job.status,
        "date_applied": new_job.date_applied
    }), 201


@app.route("/jobs", methods=["GET"])
def get_jobs():
    jobs = Job.query.all()
    output = []

    for job in jobs:
        job_data = {
            "id": job.id,
            "company": job.company,
            "position": job.position,
            "status": job.status,
            "date_applied": job.date_applied
        }
        output.append(job_data)

    return jsonify(output)


@app.route("/jobs/", methods=["GET"])
def get_jobs1():
    jobs = Job.query.all()
    output = []

    for job in jobs:
        job_data = {
            "id": job.id,
            "company": job.company,
            "position": job.position,
            "status": job.status,
            "date_applied": job.date_applied
        }
        output.append(job_data)

    return jsonify(output)


# Get Request to now get the jobs by id aka READ

@app.route("/jobs/<int:job_id>", methods=["GET"])
def get_job(job_id):
    job = Job.query.get_or_404(job_id)
    return jsonify({
        "id": job.id,
        "company": job.company,
        "position": job.position,
        "status": job.status,
        "date_applied": job.date_applied
    })

# for updating the job aka UPDATE


@app.route("/jobs/<int:job_id>", methods=["PUT"])
def update_job(job_id):
    job = Job.query.get_or_404(job_id)
    data = request.get_json()

    if not data:
        return jsonify({"error": "no data provided"}), 400

    job.company = data.get("company", job.company)
    job.position = data.get("position", job.position)
    job.status = data.get("status", job.status)
    job.date_applied = data.get("date_applied", job.date_applied)

    db.session.commit()
    return jsonify({
        "id": job.id,
        "company": job.company,
        "position": job.position,
        "status": job.status,
        "date_applied": job.date_applied
    })


@app.route("/jobs/<int:job_id>", methods=["DELETE"])
def delete_job(job_id):
    job = Job.query.get_or_404(job_id)
    db.session.delete(job)
    db.session.commit()

    return jsonify({"message": f"Job number {job.id} deleted successfully."}), 200


if __name__ == "__main__":

    app.run(debug=True)
