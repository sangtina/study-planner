from flask import Flask, render_template, request, redirect, url_for, session
import pandas as pd

app = Flask(__name__)
app.secret_key = "studyplanner"


# ---------------- LOGIN ----------------
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        return redirect(url_for("availability"))
    return render_template("login.html")


# ---------------- AVAILABILITY ----------------
@app.route("/availability", methods=["GET", "POST"])
def availability():
    if request.method == "POST":
        session["weeks"] = int(request.form.get("weeks") or 0)
        session["weekdays"] = request.form.getlist("weekdays")
        return redirect(url_for("planner"))
    return render_template("page2_availability.html")


# ---------------- PLANNER ----------------
@app.route("/planner", methods=["GET", "POST"])
def planner():

    df = pd.read_csv("data/BAD601 SYLLABUS CONTENT.csv")
    modules = sorted(df["COURSE MODULE"].unique())

    if "selected_topics" not in session:
        session["selected_topics"] = []

    selected_modules = []
    topics = []

    if request.method == "POST":

        action = request.form.get("action")
        selected_modules = request.form.getlist("modules")
        current_topics = request.form.getlist("topics")

        updated = set(session["selected_topics"]) | set(current_topics)
        session["selected_topics"] = list(updated)

        # -------- LOAD --------
        if action == "load":
            if selected_modules:
                selected_modules_int = list(map(int, selected_modules))
                filtered = df[df["COURSE MODULE"].isin(selected_modules_int)]
                topics = filtered.to_dict(orient="records")

        # -------- GENERATE --------
        elif action == "generate":

            selected = df[df["TOPIC"].isin(session["selected_topics"])]
            topic_list = selected.to_dict(orient="records")

            if not topic_list:
                return redirect(url_for("planner"))

            total_hours = selected["EST STUDY HOURS"].sum()

            weeks = session.get("weeks", 1)
            selected_days = session.get("weekdays", [])

            if not selected_days:
                selected_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

            if weeks == 0:
                weeks = 1

            total_days = weeks * len(selected_days)
            routine=[]
            for week in range(1, weeks + 1):
               for day in selected_days:
                routine.append({
                "month": None,
                "week": week,
                "day": day,
                "topic": [],
                "hours": 0
            })
            # STEP 2: Distribute topics round-robin
            total_slots = len(routine)

            for i, topic in enumerate(topic_list):
              slot_index = i % total_slots

              routine[slot_index]["topic"].append(topic["TOPIC"])
              routine[slot_index]["hours"] += topic["EST STUDY HOURS"]
            # STEP 3: Clean formatting
            for day in routine:
                if not day["topic"]:
                 day["topic"] = "Nil"
                 day["hours"] = 0
                else:
                 day["topic"] = ", ".join(day["topic"])
                 day["hours"] = round(day["hours"], 2) 

            return render_template(
                "page4_result.html",
                routine=routine,
                total_hours=total_hours
            )

    return render_template(
        "page3_planner.html",
        modules=modules,
        topics=topics,
        selected_modules=selected_modules,
        selected_topics=session["selected_topics"]
    )


if __name__ == "__main__":
    app.run(debug=True)