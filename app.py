from flask import Flask, render_template
import profile_data as pd

app = Flask(__name__)

@app.route("/")
def index():
    return render_template(
        "index.html",
        profile=pd.PROFILE,
        skill_groups=pd.SKILL_GROUPS,
        strengths=pd.STRENGTHS,
        experience=pd.EXPERIENCE,
        education=pd.EDUCATION,
        certifications=pd.CERTIFICATIONS,
        achievements=pd.ACHIEVEMENTS,
        nav_sections=pd.NAV_SECTIONS,
    )


if __name__ == "__main__":
    app.run()
