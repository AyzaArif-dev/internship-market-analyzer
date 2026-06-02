import pandas as pd

# Load dataset
df = pd.read_csv("data/linkedin_jobs.csv")

# -----------------------------
# BASIC INFO
# -----------------------------
print("\n================ DATA OVERVIEW ================\n")
print("Shape:", df.shape)

print("\nColumns:")
print(df.columns)

print("\nFirst 5 rows:")
print(df.head())


# -----------------------------
# CLEANING (optional safety step)
# -----------------------------
df = df.dropna(subset=["companyName", "title", "location"])


# -----------------------------
# INSIGHTS SECTION
# -----------------------------

# Top companies hiring
print("\n================ TOP COMPANIES ================\n")
print(df["companyName"].value_counts().head(10))


# Top job titles
print("\n================ TOP JOB TITLES ================\n")
print(df["title"].value_counts().head(10))


# Top locations
print("\n================ TOP LOCATIONS ================\n")
print(df["location"].value_counts().head(10))


# Experience level breakdown
print("\n================ EXPERIENCE LEVELS ================\n")
print(df["experienceLevel"].value_counts())


# Contract type breakdown
print("\n================ CONTRACT TYPES ================\n")
print(df["contractType"].value_counts())


# Most competitive jobs (by applications)
print("\n================ MOST COMPETITIVE JOBS ================\n")

# Convert applicationsCount safely (handles text like "Over 200 applicants")
df["applicationsCount_clean"] = (
    df["applicationsCount"]
    .astype(str)
    .str.extract(r"(\d+)")
    .astype(float)
)

print(
    df[["title", "companyName", "applicationsCount_clean"]]
    .sort_values("applicationsCount_clean", ascending=False)
    .head(10)
)


# -----------------------------
# SUMMARY INSIGHT
# -----------------------------
print("\n================ SUMMARY ================\n")
print("Total Jobs:", len(df))
print("Unique Companies:", df["companyName"].nunique())
print("Unique Locations:", df["location"].nunique())
df.to_json("dashboard/public/data.json", orient="records")