# ---------------------------------------------------------------------------
# All portfolio content lives here as plain data. To update the site, edit
# these structures — the templates just loop over them, nothing is hardcoded
# in the HTML. This keeps content and presentation cleanly separated.
# ---------------------------------------------------------------------------

PROFILE = {
    "name": "Bipin A Abraham",
    "title": "Python Developer",
    "location": "Bengaluru, Karnataka",
    "phone": "+91 9061143741",
    "email": "bipinabraham10@gmail.com",
    "linkedin" : "https://www.linkedin.com/in/bipin-a-abraham-a867571b9/",
    "linkedinid" : "bipin-a-abraham",
    "summary": (
        "Python Developer with 4+ years of experience in backend development, "
        "data automation, and ETL pipeline design. Proficient in Python, Pandas, "
        "and NumPy for large-scale data processing and transformation. Experienced "
        "in building and testing REST APIs and developing web applications using "
        "Flask and SQLAlchemy. Skilled in writing modular, OOP-based automation "
        "scripts and working with MySQL for data persistence. Familiar with Selenium "
        "for browser automation and CI/CD workflows. A collaborative team player "
        "committed to delivering clean, production-ready Python solutions."
    ),
}

# Grouped so the skills section can render distinct clusters instead of one
# undifferentiated bag of chips.
SKILL_GROUPS = [
    {
        "label": "Languages & Frameworks",
        "skills": ["Python", "Flask", "JavaScript", "ReactJS"],
    },
    {
        "label": "Data & Persistence",
        "skills": ["Pandas & NumPy", "SQLAlchemy", "MySQL"],
    },
    {
        "label": "Automation & Tooling",
        "skills": ["Selenium", "Bash Scripts", "Git", "GCP"],
    },
    {
        "label": "AI-Assisted Development",
        "skills": ["Prompt Engineering", "Gemini CLI"],
    },
]

# Synthesized from the recurring themes in the professional summary and work
# history — not new facts, just the throughlines pulled to the surface.
STRENGTHS = [
    {
        "icon": "layers",
        "title": "ETL & Data Pipelines",
        "description": (
            "Designs pipelines that turn heterogeneous raw datasets into clean, "
            "structured output, cutting manual processing time significantly."
        ),
    },
    {
        "icon": "terminal",
        "title": "Modular, OOP Python",
        "description": (
            "Writes reusable, class-based automation scripts built to scale "
            "across multiple data sources rather than one-off scripts."
        ),
    },
    {
        "icon": "git-branch",
        "title": "API & Backend Design",
        "description": (
            "Builds and tests RESTful services with Flask and SQLAlchemy, from "
            "schema design to query optimization for backend scalability."
        ),
    },
    {
        "icon": "users",
        "title": "Collaborative Delivery",
        "description": (
            "Works across Agile, cross-functional teams and CI/CD pipelines, "
            "acting as technical point of contact for junior engineers."
        ),
    },
]

EXPERIENCE = [
    {
        "role": "System Engineer",
        "team": "Data Commons",
        "company": "Infosys Limited",
        "location": "Bengaluru, India",
        "period": "Aug 2024 — Sep 2025",
        "current": True,
        "bullets": [
            "Contributed to building and maintaining lightweight Flask-based web applications, following OOP principles and design patterns to keep the codebase modular and maintainable.",
            "Maintained and extended SQLAlchemy ORM integrations for relational data storage, including schema updates, indexing adjustments, and query optimisation for backend scalability.",
            "Developed and tested RESTful APIs enabling internal services and external consumers to access statistical datasets in JSON format.",
            "Supported data ingestion and transformation pipelines using Pandas and NumPy, automating conversion of heterogeneous datasets into structured, graph-compatible formats — reducing manual processing time by approximately 70%.",
            "Supported CI/CD pipelines where approved GitHub pull requests triggered automated Docker image builds and deployed updates via GCP batch jobs.",
            "Collaborated with cross-functional teams using Agile methodologies, acting as primary technical POC for the junior team.",
        ],
    },
    {
        "role": "System Associate",
        "team": "Data Commons",
        "company": "Infosys Limited",
        "location": "Bengaluru, India",
        "period": "Aug 2021 — Jul 2024",
        "current": False,
        "bullets": [
            "Automated retrieval of public datasets from government and open-data portals using Python's Requests library and BeautifulSoup, reducing manual data collection effort.",
            "Developed Selenium WebDriver scripts to extract data from dynamic, JavaScript-rendered web pages where static scraping was not feasible.",
            "Cleaned, normalised, and transformed raw datasets using Pandas and NumPy — handling missing values, standardising formats, and structuring data for downstream processing.",
            "Wrote modular, reusable OOP-based Python scripts to standardise and scale repetitive download, process, and upload workflows across multiple data sources.",
            "Regularly utilized Gemini AI and Gemini CLI for code generation, debugging, and testing, improving development speed and code quality.",
            "Collaborated in an Agile environment, using Git for version control and peer-reviewed code maintenance across distributed teams.",
        ],
    },
]

EDUCATION = [
    {
        "degree": "Bachelor of Computer Application",
        "institution": "Kristu Jyoti College of Management & Technology",
        "location": "Changanachery, Kottayam",
        "period": "Jun 2018 — Jul 2021",
    }
]

CERTIFICATIONS = [
    {"name": "Prompt Engineering for Developers", "issuer": "DeepLearning.AI"},
    {"name": "SQL for Data Analysis", "issuer": "Udemy"},
    {"name": "Python Data Analysis", "issuer": "Udemy"},
    {"name": "Python Pro Bootcamp", "issuer": "Udemy"},
]

ACHIEVEMENTS = [
    {
        "title": "Infosys INSTA Award",
        "period": "Sep 2024",
        "description": "Recognised for playing a key role in the Data Commons project.",
    },
    {
        "title": "Infosys RISE Award — Rookie of the Quarter",
        "period": "FY23 Q3",
        "description": "Awarded for exceptional performance during the early stages of the career at Infosys.",
    },
]

NAV_SECTIONS = [
    {"id": "hero", "label": "~/intro"},
    {"id": "strengths", "label": "~/strengths"},
    {"id": "skills", "label": "~/skills"},
    {"id": "experience", "label": "~/experience"},
    {"id": "education", "label": "~/education"},
    {"id": "certifications", "label": "~/certifications"},
    {"id": "contact", "label": "~/contact"},
]