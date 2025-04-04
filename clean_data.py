import pandas as pd

# Load Dataset 1
df1 = pd.read_csv("/home/tino/Documents/Projects/LabFlow/ML NCF/Extended_Employee_Performance_and_Productivity_Data.csv")

# Load Dataset 2
df2 = pd.read_csv("/home/tino/Documents/Projects/LabFlow/ML NCF/large_dataset.csv")

# Merge datasets on Employee_ID and user_id
merged_df = pd.merge(
    df1,
    df2,
    left_on="Employee_ID",
    right_on="user_id",
    how="inner"  # Use "inner" to keep only matching rows
)

# Drop redundant columns (e.g., user_id since Employee_ID is sufficient)
merged_df.drop(columns=["user_id"], inplace=True)

# List of relevant columns
relevant_columns = [
    "Employee_ID",
    "Job_Title",
    "Performance_Score",
    "Work_Hours_Per_Week",
    "Projects_Handled",
    "Employee_Satisfaction_Score",
    "Team_Size",
    "Training_Hours",
    "Promotions",
    "Resigned",
    "technical_skills",
    "skill_proficiency",
    "preferred_role",
    "collaboration_score",
    "personality_type",
    "communication_style",
    "work_habits",
    "teamwork_style",
    "leadership_score",
    "project_interests",
    "availability",
    "Department",  # From Dataset 1
    "Gender",  # From Dataset 1
    "Age",  # From Dataset 1
    "Hire_Date",  # From Dataset 1
    "Years_At_Company",  # From Dataset 1
    "Education_Level",  # From Dataset 1
    "Monthly_Salary",  # From Dataset 1
    "Overtime_Hours",  # From Dataset 1
    "Sick_Days",  # From Dataset 1
    "Remote_Work_Frequency",  # From Dataset 1
    "past_projects",  # From Dataset 2
    "time_zone"  # From Dataset 2
]

# Filter the merged dataset
filtered_df = merged_df[relevant_columns]

# Save the filtered dataset
filtered_df.to_csv("filtered_employee_data.csv", index=False)

print("Filtered dataset saved as 'filtered_employee_data.csv'")
print(filtered_df.head())