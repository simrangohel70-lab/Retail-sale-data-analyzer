import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

class RetailAnalyzer:

    def __init__(self):
        self.data = None

    # Load CSV
    def load_data(self, file_path):
        try:
            self.data = pd.read_csv(file_path)
            print("Data Loaded Successfully!")

            if self.data.empty:
                print("Dataset is Empty")
            else:
                print("Dataset Loaded Successfully")

            return True

        except FileNotFoundError:
            print("CSV File Not Found!")
            return False

    # Display Summary
    def display_summary(self):

        print("\nFirst 5 Records")
        print(self.data.head())

        print("\nLast 5 Records")
        print(self.data.tail())

        print("\nDataset Info")
        print(self.data.info())

        print("\nMissing Values")
        print(self.data.isnull().sum())

    # Calculate Metrics
    def calculate_metrics(self):

        self.data.fillna(0, inplace=True)

        total_sales = self.data["Total Sales"].sum()
        average_sales = self.data["Total Sales"].mean()
        popular_product = self.data["Product"].mode()[0]

        sales_array = np.array(self.data["Total Sales"])

        print("\n------ SALES METRICS ------")
        print("Total Sales :", total_sales)
        print("Average Sales :", average_sales)
        print("Maximum Sale :", np.max(sales_array))
        print("Minimum Sale :", np.min(sales_array))
        print("Most Popular Product :", popular_product)

    # Filter Data
    def filter_data(self, category):

        result = self.data[self.data["Category"] == category]

        if result.empty:
            print("No Data Found!")
        else:
            print(result)

    # Visualization
    def visualize_data(self):

        # Bar Chart
        plt.figure(figsize=(7,5))
        self.data.groupby("Category")["Sales"].sum().plot(kind="bar", color="skyblue")
        plt.title("Category Wise Sales")
        plt.xlabel("Category")
        plt.ylabel("Total Sales")
        plt.show()

        # Line Chart
        plt.figure(figsize=(8,5))
        self.data.groupby("Date")["Sales"].sum().plot(kind="line", marker="o", color="red")
        plt.title("Sales Over Time")
        plt.xlabel("Date")
        plt.ylabel("Sales")
        plt.xticks(rotation=45)
        plt.show()

        # Heatmap
        plt.figure(figsize=(6,4))
        sns.heatmap(self.data.corr(numeric_only=True), annot=True, cmap="coolwarm")
        plt.title("Correlation Heatmap")
        plt.show()


# Main Program

analyzer = RetailAnalyzer()

file = input("Enter CSV File Name : ")

if analyzer.load_data(file):

    analyzer.display_summary()

    analyzer.calculate_metrics()

    category = input("\nEnter Category : ")

    analyzer.filter_data(category)

    analyzer.visualize_data()

else:

    print("Please check your CSV file path.")