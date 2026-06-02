# import streamlit as st
# import pandas as pd
# import plotly.express as px

# # --------------------------------------------------
# # PAGE CONFIG
# # --------------------------------------------------

# st.set_page_config(
#     page_title="Internship Market Analyzer",
#     page_icon="",
#     layout="wide"
# )

# # --------------------------------------------------
# # LOAD DATA
# # --------------------------------------------------

# @st.cache_data
# def load_data():
#     df = pd.read_csv("data/linkedin_jobs.csv")
#     df.columns = df.columns.str.strip()
#     return df

# df = load_data()

# # --------------------------------------------------
# # THEME
# # --------------------------------------------------

# st.markdown("""
# <style>

# .stApp {
#     background-color: #f5f1ed;
# }

# h1,h2,h3 {
#     color:#2d2420;
# }

# div[data-testid="stMetric"]{
#     background:white;
#     padding:18px;
#     border-radius:18px;
#     box-shadow:0 4px 12px rgba(0,0,0,0.08);
# }

# .block-container{
#     padding-top:2rem;
# }

# </style>
# """, unsafe_allow_html=True)

# # --------------------------------------------------
# # SIDEBAR
# # --------------------------------------------------

# st.sidebar.title("Filters")

# selected_contract = st.sidebar.multiselect(
#     "Contract Type",
#     sorted(df["contractType"].dropna().unique())
# )

# selected_experience = st.sidebar.multiselect(
#     "Experience Level",
#     sorted(df["experienceLevel"].dropna().unique())
# )

# selected_work_type = st.sidebar.multiselect(
#     "Work Type",
#     sorted(df["workType"].dropna().unique())
# )

# filtered_df = df.copy()

# if selected_contract:
#     filtered_df = filtered_df[
#         filtered_df["contractType"].isin(selected_contract)
#     ]

# if selected_experience:
#     filtered_df = filtered_df[
#         filtered_df["experienceLevel"].isin(selected_experience)
#     ]

# if selected_work_type:
#     filtered_df = filtered_df[
#         filtered_df["workType"].isin(selected_work_type)
#     ]

# # --------------------------------------------------
# # HEADER
# # --------------------------------------------------

# st.title("Internship Market Intelligence Dashboard")

# st.markdown(
#     """
# Analyze internship demand, hiring trends, top employers,
# locations, and competitiveness across the market.
# """
# )

# # --------------------------------------------------
# # KPI SECTION
# # --------------------------------------------------

# total_jobs = len(filtered_df)

# unique_companies = filtered_df["companyName"].nunique()

# unique_locations = filtered_df["location"].nunique()

# top_company = (
#     filtered_df["companyName"]
#     .value_counts()
#     .index[0]
#     if not filtered_df.empty
#     else "N/A"
# )

# k1, k2, k3, k4 = st.columns(4)

# with k1:
#     st.metric("Total Jobs", total_jobs)

# with k2:
#     st.metric("Companies", unique_companies)

# with k3:
#     st.metric("Locations", unique_locations)

# with k4:
#     st.metric("Top Employer", top_company)

# st.markdown("---")

# # --------------------------------------------------
# # TOP COMPANIES
# # --------------------------------------------------

# top_companies = (
#     filtered_df["companyName"]
#     .value_counts()
#     .head(10)
#     .reset_index()
# )

# top_companies.columns = ["Company", "Postings"]

# fig_companies = px.bar(
#     top_companies,
#     x="Company",
#     y="Postings",
#     color="Postings",
#     title="Top Companies"
# )

# fig_companies.update_layout(
#     plot_bgcolor="white",
#     paper_bgcolor="white",
#     height=450
# )

# # --------------------------------------------------
# # TOP LOCATIONS
# # --------------------------------------------------

# top_locations = (
#     filtered_df["location"]
#     .value_counts()
#     .head(10)
#     .reset_index()
# )

# top_locations.columns = ["Location", "Postings"]

# fig_locations = px.bar(
#     top_locations,
#     x="Location",
#     y="Postings",
#     color="Postings",
#     title="Top Locations"
# )

# fig_locations.update_layout(
#     plot_bgcolor="white",
#     paper_bgcolor="white",
#     height=450
# )

# left, right = st.columns(2)

# with left:
#     st.plotly_chart(fig_companies, use_container_width=True)

# with right:
#     st.plotly_chart(fig_locations, use_container_width=True)

# # --------------------------------------------------
# # CONTRACT TYPES
# # --------------------------------------------------

# c1, c2 = st.columns(2)

# contract_data = (
#     filtered_df["contractType"]
#     .value_counts()
#     .reset_index()
# )

# contract_data.columns = ["Contract Type", "Count"]

# fig_contract = px.pie(
#     contract_data,
#     names="Contract Type",
#     values="Count",
#     title="Contract Type Breakdown"
# )

# with c1:
#     st.plotly_chart(fig_contract, use_container_width=True)

# # --------------------------------------------------
# # EXPERIENCE LEVEL
# # --------------------------------------------------

# experience_data = (
#     filtered_df["experienceLevel"]
#     .value_counts()
#     .reset_index()
# )

# experience_data.columns = ["Experience", "Count"]

# fig_exp = px.pie(
#     experience_data,
#     names="Experience",
#     values="Count",
#     title="Experience Level Breakdown"
# )

# with c2:
#     st.plotly_chart(fig_exp, use_container_width=True)

# # --------------------------------------------------
# # MOST COMPETITIVE JOBS
# # --------------------------------------------------

# st.subheader("Most Competitive Internships")

# competitive_cols = [
#     "title",
#     "companyName",
#     "location",
#     "applicationsCount"
# ]

# existing_cols = [
#     c for c in competitive_cols
#     if c in filtered_df.columns
# ]

# st.dataframe(
#     filtered_df[existing_cols].head(20),
#     use_container_width=True
# )

# # --------------------------------------------------
# # RAW DATA
# # --------------------------------------------------

# with st.expander("View Raw Dataset"):
#     st.dataframe(
#         filtered_df,
#         use_container_width=True
#     )

import streamlit as st
import pandas as pd
import plotly.express as px

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="Internship Market Analyzer",
    layout="wide"
)

# --------------------------------------------------
# LOAD DATA
# --------------------------------------------------

df = pd.read_csv("data/linkedin_jobs.csv")
df.columns = df.columns.str.strip()

# Fixed columns
company_col = "companyName"
location_col = "location"
title_col = "title"
experience_col = "experienceLevel"
contract_col = "contractType"

# --------------------------------------------------
# STYLING
# --------------------------------------------------

st.markdown("""
<style>

.stApp {
    background-color: #f7f5f2;
}

h1,h2,h3 {
    color:#2d2420;
}

div[data-testid="stMetric"] {
    background:white;
    border-radius:18px;
    padding:18px;
    box-shadow:0 4px 12px rgba(0,0,0,0.08);
}

.block-container {
    padding-top:2rem;
    padding-bottom:2rem;
}

</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.title("Internship Market Analyzer")
st.caption("Market Intelligence Dashboard for Internship Opportunities")

# --------------------------------------------------
# KPI CARDS
# --------------------------------------------------

total_jobs = len(df)
total_companies = df[company_col].nunique()
total_locations = df[location_col].nunique()

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Jobs", f"{total_jobs:,}")

with col2:
    st.metric("Companies", f"{total_companies:,}")

with col3:
    st.metric("Locations", f"{total_locations:,}")

st.markdown("---")

# --------------------------------------------------
# TOP COMPANIES
# --------------------------------------------------

top_companies = (
    df[company_col]
    .value_counts()
    .head(10)
    .reset_index()
)

top_companies.columns = ["Company", "Postings"]

fig_companies = px.bar(
    top_companies,
    x="Company",
    y="Postings",
    title="Top Hiring Companies",
    color="Postings"
)

fig_companies.update_layout(
    plot_bgcolor="white",
    paper_bgcolor="white",
    title_x=0
)

# --------------------------------------------------
# TOP LOCATIONS
# --------------------------------------------------

top_locations = (
    df[location_col]
    .value_counts()
    .head(10)
    .reset_index()
)

top_locations.columns = ["Location", "Postings"]

fig_locations = px.bar(
    top_locations,
    x="Location",
    y="Postings",
    title="Top Locations",
    color="Postings"
)

fig_locations.update_layout(
    plot_bgcolor="white",
    paper_bgcolor="white",
    title_x=0
)

# --------------------------------------------------
# CHARTS ROW
# --------------------------------------------------

left, right = st.columns(2)

with left:
    st.plotly_chart(
        fig_companies,
        use_container_width=True
    )

with right:
    st.plotly_chart(
        fig_locations,
        use_container_width=True
    )

# --------------------------------------------------
# EXPERIENCE LEVELS
# --------------------------------------------------

if experience_col in df.columns:

    exp_counts = (
        df[experience_col]
        .value_counts()
        .reset_index()
    )

    exp_counts.columns = ["Level", "Count"]

    fig_exp = px.pie(
        exp_counts,
        names="Level",
        values="Count",
        title="Experience Levels"
    )

# --------------------------------------------------
# CONTRACT TYPES
# --------------------------------------------------

if contract_col in df.columns:

    contract_counts = (
        df[contract_col]
        .value_counts()
        .reset_index()
    )

    contract_counts.columns = ["Contract", "Count"]

    fig_contract = px.pie(
        contract_counts,
        names="Contract",
        values="Count",
        title="Contract Types"
    )

# --------------------------------------------------
# PIE CHARTS ROW
# --------------------------------------------------

left2, right2 = st.columns(2)

with left2:
    st.plotly_chart(
        fig_exp,
        use_container_width=True
    )

with right2:
    st.plotly_chart(
        fig_contract,
        use_container_width=True
    )

# --------------------------------------------------
# MOST COMPETITIVE JOBS
# --------------------------------------------------

st.subheader("Most Competitive Internships")

competitive = df[
    [
        "title",
        "companyName",
        "location",
        "applicationsCount"
    ]
].head(10)

st.dataframe(
    competitive,
    use_container_width=True
)

# --------------------------------------------------
# RAW DATA
# --------------------------------------------------

with st.expander("View Raw Dataset"):

    st.dataframe(
        df,
        use_container_width=True
    )