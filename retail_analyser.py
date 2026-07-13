import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

class RetailAnalyzer:

    def __init__(self):
        self.data = None

    def load_data(self, file):
        try:
            self.data = pd.read_csv(file)
            print("\nDataset Loaded Successfully!")
        except:
            print("File not found!")

    def calculate_metrics(self):

        total_sales = self.data["Total Sales"].sum()
        average_sales = self.data["Total Sales"].mean()

        popular_product = self.data.groupby("Product")["Quantity Sold"].sum().idxmax()

        print("\nSALES REPORT")
        print("Total Sales :", total_sales)
        print("Average Sales :", round(average_sales,2))
        print("Most Popular Product :", popular_product)

        growth = np.mean(self.data["Total Sales"])
        print("Average Sales using NumPy :", growth)

    def filter_data(self):

        category = input("Enter Category : ")

        result = self.data[self.data["Category"].str.lower()==category.lower()]

        if len(result)==0:
            print("No Data Found")
        else:
            print(result)

    def display_summary(self):

        print("\nDataset Summary")
        print(self.data.describe())

    def bar_chart(self):

        sales = self.data.groupby("Product")["Total Sales"].sum()

        sales.plot(kind="bar")

        plt.title("Sales by Product")
        plt.xlabel("Product")
        plt.ylabel("Total Sales")
        plt.show()

    def line_chart(self):

        plt.plot(self.data["Date"],self.data["Total Sales"],marker="o")

        plt.title("Sales Trend")
        plt.xlabel("Date")
        plt.ylabel("Total Sales")
        plt.xticks(rotation=45)

        plt.show()

    def heatmap(self):

        corr=self.data[["Price","Quantity Sold","Total Sales"]].corr()

        sns.heatmap(corr,annot=True)

        plt.title("Correlation Heatmap")
        plt.show()


def menu():

    obj=RetailAnalyzer()

    while True:

        print("\nRETAIL SALES ANALYZER")
        print("1. Load Data")
        print("2. Calculate Metrics")
        print("3. Filter Data")
        print("4. Dataset Summary")
        print("5. Bar Chart")
        print("6. Line Chart")
        print("7. Heatmap")
        print("8. Exit")

        choice=input("Enter Choice : ")

        if choice=="1":
            obj.load_data("retail_sales.csv")

        elif choice=="2":
            obj.calculate_metrics()

        elif choice=="3":
            obj.filter_data()

        elif choice=="4":
            obj.display_summary()

        elif choice=="5":
            obj.bar_chart()

        elif choice=="6":
            obj.line_chart()

        elif choice=="7":
            obj.heatmap()

        elif choice=="8":
            print("Thank You")
            break

        else:
            print("Invalid Choice")


menu()
