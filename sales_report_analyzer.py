import streamlit as st
import pandas as pd
import plotly.express as px


# ------------------ Load Data ------------------
def load_data(file):
    try:
        df = pd.read_csv(file, encoding="latin1")
        return df
    except Exception as e:
        st.error(f"Error loading CSV: {e}")
        return None


# ------------------ Clean Data ------------------
def clean_data(df):
    st.write("### Cleaning Data...")

    df['Cuisines'] = df['Cuisines'].fillna("Unknown")
    df['Aggregate rating'] = pd.to_numeric(df['Aggregate rating'], errors='coerce')
    df['Votes'] = pd.to_numeric(df['Votes'], errors='coerce')
    df['Average Cost for two'] = pd.to_numeric(df['Average Cost for two'], errors='coerce')

    df = df.dropna()

    st.success("Data cleaned successfully!")
    return df


# ------------------ Analyze Data (Charts + Tables) ------------------
def analyze_data(df):

    st.header("📊 Zomato Data Insights")

    # 1. Top Cities
    st.subheader("Top 10 Cities by Number of Restaurants")
    city_counts = df['City'].value_counts().head(10)
    st.bar_chart(city_counts)

    # 2. Top Cuisines
    st.subheader("Top 10 Popular Cuisines")
    cuisines = df['Cuisines'].value_counts().head(10)
    st.bar_chart(cuisines)

    # 3. Highest Rated Restaurants
    st.subheader("Top 10 Highest Rated Restaurants")
    top_rated = df.sort_values(by="Aggregate rating", ascending=False).head(10)
    st.dataframe(top_rated[['Restaurant Name', 'City', 'Aggregate rating']])

    # 4. Average Cost Histogram
    st.subheader("Average Cost for Two - Distribution")
    fig_cost = px.histogram(df, x="Average Cost for two", nbins=30)
    st.plotly_chart(fig_cost)

    # 5. Votes vs Rating
    st.subheader("Votes vs Rating Scatter Plot")
    fig_scatter = px.scatter(df, x="Aggregate rating", y="Votes",
                             hover_data=["Restaurant Name", "City"],
                             title="Votes vs Rating")
    st.plotly_chart(fig_scatter)

    # 6. Rating Category Count
    st.subheader("Rating Category Count")
    rating_counts = df['Rating text'].value_counts()
    fig_rating = px.bar(rating_counts, x=rating_counts.index, y=rating_counts.values,
                        labels={'x': 'Rating Text', 'y': 'Count'})
    st.plotly_chart(fig_rating)


# ------------------ Main ------------------
def main():
    st.title("🍽️ Zomato Data Analyzer ")

    uploaded_file = st.file_uploader("Upload your Zomato CSV file", type=["csv"])

    if uploaded_file is not None:
        df = load_data(uploaded_file)

        if df is not None:
            df = clean_data(df)
            analyze_data(df)
    else:
        st.info("Please upload a Zomato CSV file to begin.")


if __name__ == "__main__":
    main()





# import pandas as pd
# import matplotlib.pyplot as plt


# def load_data(file_path):
#     try:
#         data = pd.read_csv(file_path, encoding="latin1")
#         print("Data loaded successfully!")
#         return data
#     except Exception as e:
#         print("Error loading data:", e)
#         return None


# def clean_data(data):
#     print("\nCleaning Data...")

#     # Fill missing values
#     data['Cuisines'] = data['Cuisines'].fillna("Unknown")
#     data['Aggregate rating'] = pd.to_numeric(data['Aggregate rating'], errors='coerce')
#     data['Votes'] = pd.to_numeric(data['Votes'], errors='coerce')
#     data['Average Cost for two'] = pd.to_numeric(data['Average Cost for two'], errors='coerce')

#     data = data.dropna()

#     print("Data cleaned successfully!")
#     return data


# def analyze_data(data):
#     print("\n--- Zomato Dataset Insights ---")

#     # 1. Top cities by number of restaurants
#     city_counts = data['City'].value_counts().head(10)
#     print("\nTop 10 cities by number of restaurants:")
#     print(city_counts)

#     # 2. Most common cuisines
#     cuisines = data['Cuisines'].value_counts().head(10)
#     print("\nTop 10 popular cuisines:")
#     print(cuisines)

#     # 3. Highest rated restaurants
#     top_rated = data.sort_values(by="Aggregate rating", ascending=False).head(10)
#     print("\nTop 10 highest rated restaurants:")
#     print(top_rated[['Restaurant Name', 'City', 'Aggregate rating']])

#     # 4. Average cost distribution
#     plt.figure(figsize=(10, 6))
#     data['Average Cost for two'].plot(kind='hist', bins=30)
#     plt.title("Average Cost for Two Distribution")
#     plt.xlabel("Cost")
#     plt.ylabel("Frequency")
#     plt.show()

#     # 5. Votes vs Rating
#     plt.figure(figsize=(10, 6))
#     plt.scatter(data['Aggregate rating'], data['Votes'])
#     plt.title("Votes vs Rating")
#     plt.xlabel("Rating")
#     plt.ylabel("Votes")
#     plt.show()

#     # 6. Count of restaurants by rating text
#     rating_counts = data['Rating text'].value_counts()
#     print("\nRestaurant count by rating category:")
#     print(rating_counts)

#     rating_counts.plot(kind='bar', figsize=(10, 6), color="skyblue")
#     plt.title("Restaurant Count by Rating Text")
#     plt.xlabel("Rating Category")
#     plt.ylabel("Number of Restaurants")
#     plt.xticks(rotation=45)
#     plt.show()


# def main():
#     print("Welcome to the Zomato Data Analyzer!")

#     file_path = input("Enter the path to your Zomato CSV file: ")
#     data = load_data(file_path)

#     if data is None:
#         return

#     data = clean_data(data)

#     analyze_data(data)


# if __name__ == "__main__":
#     main()

############################################################

# import pandas as pd
# import matplotlib.pyplot as plt


# def load_data(file_path):
#     """Load Sales Data from the CSV file"""
#     try:
#         data = pd.read_csv(file_path,encoding="latin1")
#         print("Data loaded successfully!")
#         print(df.head())
#         print("Columns in your file:", data.columns.tolist())
#         return data
#     except Exception as e:
#         print("Error loading data:", e)
#         return None


# def clean_data(data):
#     """Clean and preprocess the data"""
#     print("\nCleaning Data...")

#     # Fill missing product categories
#     data['Product_Category'] = data['Product_Category'].fillna("Unknown")

#     # Drop missing rows
#     data = data.dropna()

#     # Convert columns
#     data['Date'] = pd.to_datetime(data['Date'])
#     data['Sales_Amount'] = pd.to_numeric(data['Sales_Amount'], errors='coerce')

#     # Add Year-Month column
#     data['Year_Month'] = data['Date'].dt.to_period('M')

#     # Add Revenue column
#     if 'Quantity' in data.columns and 'Price' in data.columns:
#         data['Revenue'] = data['Quantity'] * data['Price']

#     print("Data cleaned successfully!")
#     return data


# def analyze_data(data):
#     """Analyze and display sales insights"""
#     print("\n--- Sales Insights ---")

#     # Monthly sales
#     monthly_sales = data.groupby('Year_Month')['Sales_Amount'].sum()
#     print("\nMonthly Sales:")
#     print(monthly_sales)

#     # Top 5 products by revenue
#     if 'Revenue' in data.columns:
#         top_products = (
#             data.groupby('Product_Name')['Revenue']
#             .sum()
#             .sort_values(ascending=False)
#             .head(5)
#         )
#         print("\nTop 5 Products by Revenue:")
#         print(top_products)

#     # Plot monthly sales
#     monthly_sales.plot(kind='bar', figsize=(10, 6), color='skyblue')
#     plt.title('Monthly Sales')
#     plt.xlabel("Month")
#     plt.ylabel("Total Sales")
#     plt.xticks(rotation=45)
#     plt.show()


# def main():
#     print("Welcome to the Sales Report Analyzer!")

#     # Load Data
#     file_path = input("Enter the path to your sales CSV file: ")
#     data = load_data(file_path)

#     if data is None:
#         return

#     # Clean Data
#     data = clean_data(data)

#     # Analyze Data
#     analyze_data(data)


# if __name__ == "__main__":
#     main()


# import pandas as pd 
# import matplotlib.pyplot as plt 

# def load_data(file_path):
#     """Load Sales Data from the CSV file"""
#     try:
#         data =pd.read_csv(file_path)
#         print("Data loaded Successfully!")
#         return data
#     except Exception as e:
#         print("Error Loading data:",e )
#         return None
    
# def clean_data(data):
#     """Clean and preprocess the data"""
#     print("\n Cleaning Data...")

# # Fill the missing values 
# data['Product_Category'] = data['Product_Category'].fillna("Unknown")
# data = data.dropna()

# # Convert columns 
# data['Date'] = pd.to_datetime(data['Date'])
# data['Sales_Amount']= pd.to_numeric(data['Sales_Amount'],errors = 'coerce')

# # Add New Columns
# def clean_data(data):
#     # Add New Columns
#     data['Year_Month'] = data['Date'].dt.to_period('M')

#     if 'Quantity' in data.columns and 'Price' in data.columns:
#         data['Revenue'] = data['Quantity'] * data['Price']

#     print("Data Cleaned Successfully")
#     return data

# def analyze_data(data):
#     """ Analyze and Display the insights from the data."""
#     print("\n---Sales Insights---")

# #Total sales by month
# monthly_sales = data.groupby('Year_Month')['Sales_Amount'].sum()
# print("\n Monthly Sales:")
# print(monthly_sales)

# #Top 5 Products by Revenue
# if 'Revenue' in data.columns:
#     top_products = data.groupby('Product_Name')['Revenue'].sum().sort_values(ascending = False).head(5)
#     print("\n Top 5 products by Revenue")
#     print(top_products)

# #Visualize monthly sales
# monthly_sales.plot(kind='bar',figsize=(10,6), color = 'skyblue ')
# plt.title('Monthly Sales')
# plt.xlabel("month")
# plt.ylabel("Total Sales")
# plt.xticks(rotation = 45)
# plt.show()

# def main():
#     print("Welcome to the Sales report Analyzer!")
    
#     # Load Data
#     file_path = input("Enter the path to your sales CSV file: ")
#     data = load_data(file_path)

#     if data is None:
#         return

# #Clean data 
# data = clean_data(data)

# #Analyze Data
# analyze_data(data)
# if __name__ == "__main__":
#     main()