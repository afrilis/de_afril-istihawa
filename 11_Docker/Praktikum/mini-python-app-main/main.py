import os
import pandas as pd


def calculate_average(csv_file):
    # Read CSV file
    df = pd.read_csv(csv_file)

    # Calculate the average of the 'value' column
    average_value = df["value"].mean()

    return average_value


if __name__ == "__main__":
    csv_file_path = os.environ.get("CSV_FILE")

    if not csv_file_path:
        raise ValueError("CSV_FILE environment variable not set.")

    result = calculate_average(csv_file_path)
    print(f"Average value: {result}")
