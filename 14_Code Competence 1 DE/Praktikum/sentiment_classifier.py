import pandas as pd

class SentimentAnalyzer:
    def __init__(self, data_path):
        self.data_path = data_path
        self.data = None

    def load_data(self):
        # Read data from CSV file
        self.data = pd.read_csv(self.data_path)
        print("Data loaded successfully.")

    def classify_sentiment(self):
        if self.data is None:
            print("Error: Data not loaded yet.")
            return

        # Assign sentiment labels based on existing labels
        sentiment_map = {'good': '1', 'bad': '2', 'other': '3'}
        self.data['sentiment'] = self.data['labels'].apply(lambda x: sentiment_map.get(x, '3'))
        print("Sentiment classification completed.")

    def save_sentiment_data(self):
        if self.data is None:
            print("Error: Data not loaded yet.")
            return

        # Filter data by sentiment
        sentiment_groups = {
            'positive': self.data[self.data['sentiment'] == '1'],
            'negative': self.data[self.data['sentiment'] == '2'],
            'neutral': self.data[self.data['sentiment'] == '3']
        }

        # Save each sentiment group to a separate CSV file
        for sentiment, group_data in sentiment_groups.items():
            group_data.to_csv(f'sentiment_{sentiment}.csv', index=False)

        print("Sentiment classification files saved successfully.")

    def summarize_sentiment_counts(self):
        if self.data is None:
            print("Error: Data not loaded yet.")
            return

        # Count occurrences of each sentiment
        sentiment_counts = self.data['sentiment'].value_counts().reset_index()
        sentiment_counts.columns = ['sentiment', 'count']

        # Save sentiment counts to a CSV file
        sentiment_counts.to_csv('sentiment_counts.csv', index=False)
        print("Sentiment counts file saved successfully.")

# Create an instance of the SentimentAnalyzer class
analyzer = SentimentAnalyzer("file.csv")

# Execute methods in a logical sequence
analyzer.load_data()
analyzer.classify_sentiment()
analyzer.save_sentiment_data()
analyzer.summarize_sentiment_counts()
