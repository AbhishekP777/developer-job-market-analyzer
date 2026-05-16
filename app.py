import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



st.title("Developer Job Market Analyzer")

st.markdown("""
Analyze trends in AI, Data Science, and Analytics jobs.

Use the sidebar filters to explore:
- salaries
- job roles
- industries
- remote work trends
""")




df = pd.read_csv("data/jobs.csv")



## Side bar section

# Adding sidebar filters

role_options = ["All Roles"] + list(df["job_title"].unique())

selected_role = st.sidebar.selectbox(
    "Select Job Role",
    role_options
)

industry_options = ["All Industries"] + list(df["company_industry"].unique())

selected_industry = st.sidebar.selectbox(
    "Select Industry",
    industry_options
)

# Adding row count slider
row_count = st.sidebar.slider(
    "Select Number of Rows",
    min_value=5,
    max_value=50,
    value=10
)

# Adding salary range slider
salary_range = st.sidebar.slider(
    "Select Salary Range",
    int(df["salary"].min()),
    int(df["salary"].max()),
    (
        int(df["salary"].min()),
        int(df["salary"].max())
    )
)


# About filters section

st.subheader("Current Filters")

st.write("Job Role:", selected_role)
st.write("Industry:", selected_industry)
st.write(
    "Salary Range:",
    f"{salary_range[0]} - {salary_range[1]}"
)

# Apply filters

filtered_df = df.copy()

filtered_df = filtered_df[
    (filtered_df["salary"] >= salary_range[0]) &
    (filtered_df["salary"] <= salary_range[1])
]

if selected_role != "All Roles":
    filtered_df = filtered_df[
        filtered_df["job_title"] == selected_role
    ]

if selected_industry != "All Industries":
    filtered_df = filtered_df[
        filtered_df["company_industry"] == selected_industry
    ]






# Download button for filtered data

csv = filtered_df.to_csv(index=False)

st.download_button(
    label="Download Filtered Data",
    data=csv,
    file_name="filtered_jobs.csv",
    mime="text/csv"
)



# Main Data Overview Section

st.subheader("Data Overview (Filtered Job Postings)")

# st.write(filtered_df.head(row_count))
st.dataframe(filtered_df.head(row_count))




# Adding dataset information section

st.subheader("Dataset Shape")

st.write("Rows and Columns:", filtered_df.shape)




# Adding key Metrics 

if filtered_df.empty:
    st.warning("No data available for selected filters.")
    st.stop()

st.subheader("Key Metrics")

col1, col2, col3 = st.columns(3)

with col1:
    overall_avg_salary = round(df["salary"].mean(), 2)

    filtered_avg_salary = round(filtered_df["salary"].mean(), 2)

    salary_difference = round(
        filtered_avg_salary - overall_avg_salary,
        2
    )

    st.metric(
        "Average Salary",
        filtered_avg_salary,
        delta=f"{salary_difference}"
    )

with col2:
    st.metric(
        "Total Job Postings",
            len(filtered_df)
        )

with col3:
    st.metric(
        "Most Common Role",
        filtered_df["job_title"].mode()[0]
    )



## Charts Section

chart1, chart2 = st.columns(2)


# Most common job roles

with chart1:
    st.subheader("Most Common Job Roles")

    job_counts = filtered_df["job_title"].value_counts()

    st.bar_chart(job_counts)


# Salary distribution

with chart2:
    st.subheader("Salary Distribution")

    fig, ax = plt.subplots()

    bins = range(40000, 200001, 20000)      # range(start, stop, step)

    ax.hist(
        filtered_df["salary"],
        bins=bins,
        edgecolor="black"
    )

    ax.set_title("Salary Distribution")
    ax.set_xlabel("Salary Range")
    ax.set_ylabel("Frequency")

    plt.xticks(bins, rotation=45)

    st.pyplot(fig)


# Remote Work Distribution

st.subheader("Remote Work Distribution")

remote_counts = filtered_df["remote_type"].value_counts()

st.bar_chart(remote_counts)



# About the dataset section
st.markdown("---")

st.markdown(
    "Built using Python, Pandas, Matplotlib, and Streamlit"
)