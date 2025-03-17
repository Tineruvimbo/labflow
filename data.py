import pandas as pd
import random
from faker import Faker

# Initialize Faker for generating realistic names and other details
fake = Faker()

# Define possible values for categorical columns
technical_skills_list = [
    "Python, ML", "Java, Spring", "UI/UX, Figma", "SQL, PostgreSQL", "React, TypeScript",
    "C++, Robotics", "Python, TensorFlow", "PHP, Laravel", "Python, R", "JavaScript, Node.js",
    "Golang, DevOps", "Rust, Blockchain", "Swift, iOS Dev", "C#, Unity", "Python, NLP"
]

preferred_roles = [
    "Data Scientist", "Backend Dev", "Designer", "Database Admin", "Frontend Dev",
    "Embedded Dev", "ML Engineer", "Web Dev", "Data Analyst", "Full Stack Dev",
    "DevOps Engineer", "Blockchain Dev", "Mobile Dev", "Game Developer", "AI Researcher"
]

past_projects = [
    "AI Research", "E-Commerce", "Web Apps", "Finance Apps", "SaaS", "IoT, Robotics",
    "AI Startups", "CMS Systems", "Healthcare AI", "Marketplace", "Cloud Security",
    "DeFi", "FinTech Apps", "Indie Games", "NLP Research"
]

personality_types = ["INTJ", "ENFP", "ISFJ", "ISTJ", "ENTP", "ISTP", "INFJ", "ESTP", "ENFJ", "ENTJ", "ISFP", "ESTJ", "INTP"]

communication_styles = ["Slack", "Email", "Zoom", "Teams", "Discord"]

work_habits = ["Remote", "Agile", "Office", "Hybrid"]

project_interests = [
    "AI, Bioinformatics", "FinTech, AI", "Design, HCI", "Data Science", "Web Dev, SaaS",
    "AI, Hardware", "NLP, AI Ethics", "E-commerce", "HealthTech", "SaaS, Web3",
    "Cloud Computing", "Crypto, Security", "FinTech, UX", "Game Dev, AI", "AI, Ethics"
]

time_zones = [f"GMT+{i}" for i in range(-12, 13)]

# Function to generate a single user profile
def generate_user_profile(user_id):
    return {
        "user_id": user_id,
        "name": fake.name(),
        "technical_skills": random.choice(technical_skills_list),
        "skill_proficiency": random.randint(1, 10),
        "preferred_role": random.choice(preferred_roles),
        "past_projects": random.choice(past_projects),
        "collaboration_score": random.randint(1, 10),
        "personality_type": random.choice(personality_types),
        "communication_style": random.choice(communication_styles),
        "work_habits": random.choice(work_habits),
        "availability": random.randint(10, 50),  # Hours per week
        "teamwork_style": random.randint(1, 10),
        "leadership_score": random.randint(1, 10),
        "project_interests": random.choice(project_interests),
        "time_zone": random.choice(time_zones)
    }

# Generate a large dataset (e.g., 1000 users)
num_users = 1000
data = [generate_user_profile(i + 1) for i in range(num_users)]

# Create DataFrame
df = pd.DataFrame(data)

# Save to CSV
output_file = "large_dataset.csv"
df.to_csv(output_file, index=False)

print(f"Dataset with {num_users} entries has been saved to '{output_file}'.")