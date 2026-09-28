import sqlite3
import datetime
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

def setup_database():
    connection = sqlite3.connect("security_logs.db")
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS phishing_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            email_content TEXT,
            prediction_result TEXT
        )
    """)
    connection.commit()
    connection.close()
    
def load_dataset():
    print("Loading email dataset...")
    df = pd.read_csv(r"C:\Users\Hp\Desktop\phishing_texts.csv")
    print(f"Loaded {len(df)} emails successfully.")
    return df

if __name__ == "__main__":
    setup_database()
    df = load_dataset()

