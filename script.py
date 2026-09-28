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
    print("Columns in CSV:", df.columns.tolist())
    print(f"Loaded {len(df)} emails successfully.")
    return df
if __name__ == "__main__":
    setup_database()
    df = load_dataset()

def train_brain(df):
    print("Preparing data for training...")
    df = df.dropna(subset=['text', 'phishing'])
    examples = df['text'].to_numpy()
    answers = df['phishing'].to_numpy()  
    
    X_train, X_test, y_train, y_test = train_test_split(
        examples, answers, test_size=0.2, random_state=42
    )
    
    print(f"Training on {len(X_train):,} emails, testing on {len(X_test):,} emails...")
    
    counter = TfidfVectorizer(stop_words='english', max_features=5000)
    X_train_numbers = counter.fit_transform(X_train)
    X_test_numbers = counter.transform(X_test)
    
    brain = LogisticRegression(max_iter=1000)
    brain.fit(X_train_numbers, y_train)

    accuracy = brain.score(X_test_numbers, y_test) * 100
    print(f"Model Test Accuracy: {accuracy:.1f}%")
    
    return counter, brain

if __name__ == "__main__":
    setup_database()
    df = load_dataset()
    counter, brain = train_brain(df)

    