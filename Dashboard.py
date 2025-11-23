import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Page config
st.set_page_config(
    page_title="Banggood Analytics Dashboard",
    page_icon="🛒",
    layout="wide"
)

# Load data
@st.cache_data
def load_data():
    return pd.read_csv('./banggood_cleaned.csv')

df = load_data()

# Title
st.title("🛒 Banggood E-commerce Analytics Dashboard")
st.markdown("*Complete ETL Pipeline: Web Scraping → Data Cleaning → SQL Analysis*")

# Sidebar
st.sidebar.header("Filters")
categories = st.sidebar.multiselect(
    "Select Categories",
    options=df['Category'].unique(),
    default=df['Category'].unique()
)
price_range = st.sidebar.slider(
    "Price Range ($)",
    min_value=float(df['Price_Clean'].min()),
    max_value=float(df['Price_Clean'].max()),
    value=(float(df['Price_Clean'].min()), float(df['Price_Clean'].max()))
)

# Filter data
filtered_df = df[
    (df['Category'].isin(categories)) &
    (df['Price_Clean'].between(price_range[0], price_range[1]))
]

# Metrics
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Total Products", len(filtered_df))
with col2:
    st.metric("Avg Price", f"${filtered_df['Price_Clean'].mean():.2f}")
with col3:
    st.metric("Avg Rating", f"{filtered_df['Rating_Clean'].mean():.2f}/5")
with col4:
    st.metric("Total Reviews", f"{filtered_df['Reviews_Clean'].sum():,}")

# Charts
st.header("📊 Visual Analytics")

col1, col2 = st.columns(2)

with col1:
    # Price by Category
    fig1 = px.box(filtered_df, x='Category', y='Price_Clean',
                  title='Price Distribution by Category',
                  color='Category')
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    # Rating Distribution
    fig2 = px.histogram(filtered_df, x='Rating_Clean',
                        title='Rating Distribution',
                        nbins=20)
    st.plotly_chart(fig2, use_container_width=True)

# Top Products
st.header("🏆 Top 10 Products by Popularity")
top_products = filtered_df.nlargest(10, 'Popularity_Score')[
    ['Name', 'Category', 'Price_Clean', 'Rating_Clean', 'Reviews_Clean', 'Popularity_Score']
]
st.dataframe(top_products, use_container_width=True)

# Price Level Distribution
st.header("💰 Price Level Analysis")
price_dist = filtered_df['Price_Level'].value_counts()
fig3 = px.pie(values=price_dist.values, names=price_dist.index,
              title='Product Distribution by Price Level')
st.plotly_chart(fig3, use_container_width=True)

# Category Performance
st.header("📈 Category Performance Summary")
category_summary = filtered_df.groupby('Category').agg({
    'Price_Clean': 'mean',
    'Rating_Clean': 'mean',
    'Reviews_Clean': 'sum',
    'Name': 'count'
}).round(2)
category_summary.columns = ['Avg Price', 'Avg Rating', 'Total Reviews', 'Product Count']
st.dataframe(category_summary, use_container_width=True)

# Scatter plot
st.header("🔍 Rating vs Reviews Analysis")
fig4 = px.scatter(filtered_df, x='Reviews_Clean', y='Rating_Clean',
                  size='Price_Clean', color='Category',
                  hover_data=['Name'],
                  title='Relationship between Reviews and Ratings')
st.plotly_chart(fig4, use_container_width=True)

# Footer
st.markdown("---")
st.markdown("**Data Pipeline:** Selenium Scraping → Pandas Cleaning → SQL Server → Analysis")
st.markdown("*Project by: Abdur Rehman | November 2025*")