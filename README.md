📘 Zomato Data Analyzer (Streamlit + Matplotlib)

A simple and interactive Streamlit web app to analyze Zomato restaurant dataset.
The app allows you to upload a CSV file, clean the data, and visualize key insights such as top cities, cuisines, rating patterns, and cost distribution.

🚀 Features
✔ Upload a Zomato CSV file

Works with any Zomato Kaggle dataset (India or global).

✔ Data Cleaning

Handles missing cuisines

Converts numeric columns

Removes invalid rows

✔ Visual Insights

This mini app includes:

📌 Top 10 cities by restaurant count
📌 Top cuisines
📌 Highest-rated restaurants
📌 Cost distribution (Matplotlib)
📌 Votes vs Rating scatter plot
📌 Restaurant count by rating text

✔ Easy to extend

You can easily add filters, maps, and advanced analytics later.

🗂️ Project Structure
zomato-basic-streamlit-app/
│
├── app.py              # Main Streamlit app
├── requirements.txt    # Required Python libraries
├── README.md           # Project documentation
└── .gitignore          # Ignore unnecessary files

📦 Installation
1. Clone the repo
git clone https://github.com/your-username/zomato-basic-streamlit-app.git
cd zomato-basic-streamlit-app

2. Install dependencies
pip install -r requirements.txt

▶️ Run the Streamlit App
streamlit run app.py


Then open the URL shown in the terminal:

http://localhost:8501

📥 How to Use

Upload your Zomato CSV file

The app will clean the data automatically

View insights and charts

Explore top restaurants and trends

📊 Dataset Requirements

Your CSV must contain these columns:

Restaurant Name

City

Cuisines

Aggregate rating

Votes

Average Cost for two

Rating text

These are standard in the Kaggle Zomato dataset.

🧩 Dependencies

Listed in requirements.txt:

streamlit
pandas
matplotlib

🤝 Contributing

Feel free to fork, raise issues, or submit pull requests.

💡 Future Enhancements

Here are ideas if you want to upgrade the project later:

Add city/cuisine filters

Add maps (Folium)

Add trend charts using Plotly

Create a universal CSV analyzer

📜 License

This project is open-source and free to use.
