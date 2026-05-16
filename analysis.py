import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data/jobs.csv")

# Shows first 5 rows
print(df.head())

# Shows basic info
print(df.info())

# Show column names
print(df.columns)

# Show unique job titles and their counts
print(df["job_title"].value_counts())

''' Using matplotlib to visualize the most common job roles '''

# Count job titles
job_counts = df["job_title"].value_counts()

# Create bar chart
job_counts.plot(kind="bar")

# Add title and labels
plt.title("Most Common Job Roles")
plt.xlabel("Job Title")
plt.ylabel("Count")

# Show graph
plt.show()


''' Analyzing  which technical skills are most in demand '''

# List of skill columns in the dataset
skills = [
    "skills_python",
    "skills_sql",
    "skills_ml",
    "skills_deep_learning",
    "skills_cloud"
]

# Sum the values for each skill to see how many job postings require each skill
print(df[skills].sum())

# Now we can visualize this data as well

skill_counts = df[skills].sum()

skill_counts.plot(kind="bar")

plt.title("Most Demanded Skills")
plt.xlabel("Skills")
plt.ylabel("Job Count")

plt.show()



# Now let's analyze the salary distribution for data science jobs
print("\n\nSalary Distribution:\n")

average_salary = df["salary"].mean()
print("Average Salary:", average_salary, "\n")

salary_by_role = df.groupby("job_title")["salary"].mean()
print("salary distribution by Role : \n",salary_by_role, "\n")

# Visualize salary distribution by role
salary_by_role.plot(kind="bar")

plt.title("Average Salary by Job Role")
plt.xlabel("Job Role")
plt.ylabel("Average Salary")

plt.show()




# Now analyzing remote work distribution

print("\n\nRemote Work Distribution:\n")
print(df["remote_type"].value_counts())

# Visualize remote work distribution
remote_counts = df["remote_type"].value_counts()

remote_counts.plot(kind="pie", autopct="%1.1f%%")

plt.title("Remote vs Hybrid vs Onsite Jobs")

plt.ylabel("")

plt.show()



# Salary distribution by experience level

experience_salary = df.groupby("experience_level")["salary"].mean()

print("\n\nSalary distribution by experience level:\n", experience_salary)




# Which industries hire the most AI/Data professionals?

industry_counts = df["company_industry"].value_counts()
print("\n\nIndustry Distribution:\n", industry_counts, "\n")


industry_salary = df.groupby("company_industry")["salary"].mean()
print("\nAverage Salary by Industry:\n", industry_salary)

# Visualize industry distribution

sns.boxplot(x="experience_level", y="salary", data=df)      # Seaborn Boxplot to show salary distribution by experience level

plt.title("Salary Distribution by Experience Level")

plt.show()




# Correlation between salary and skills

correlation = df[[
    "skills_python",
    "skills_sql",
    "skills_ml",
    "skills_deep_learning",
    "skills_cloud",
    "salary"
]].corr()

print("\nCorrelation between Salary and Skills:\n", correlation)

#correlation heatmap
sns.heatmap(correlation, annot=True)
plt.title("Correlation Heatmap")
plt.show()