# 🛍️ Retail Sales Analyzer

A Python-based Retail Sales Analyzer that loads retail sales data from a CSV file, performs data analysis, calculates sales metrics, filters data by category, and visualizes the results using charts and heatmaps.

---

## 📌 Features

✅ Load retail sales data from a CSV file

✅ Display dataset summary

✅ Check missing values

✅ Calculate sales statistics

✅ Find the most popular product

✅ Filter data by category

✅ Generate Bar Chart

✅ Generate Line Chart

✅ Generate Correlation Heatmap

---

## 🛠️ Technologies Used

- 🐍 Python
- 📊 Pandas
- 🔢 NumPy
- 📈 Matplotlib
- 🎨 Seaborn

---

## 📂 Required CSV Columns

Your CSV file should contain the following columns:

| Column Name |
|-------------|
| Date |
| Product |
| Category |
| Sales |

Example:

| Date | Product | Category | Sales |
|------|---------|----------|-------|
|2025-01-01|Laptop|Electronics|50000|
|2025-01-02|Mouse|Accessories|800|
|2025-01-03|Keyboard|Accessories|1200|

---

## ▶️ How to Run

1. Install required libraries

```bash
pip install pandas numpy matplotlib seaborn
```

2. Save your CSV file.

3. Run the program.

```bash
python retail_analyzer.py
```

4. Enter the CSV file name.

Example

```
Enter CSV File Name :
retail_data.csv
```

5. Enter a category.

Example

```
Electronics
```

---

## 📊 Output

### Data Loaded

```
Data Loaded Successfully!
```

---

### First 5 Records

```
         Date    Product      Category   Sales
0  2025-01-01     Laptop  Electronics   50000
1  2025-01-02      Mouse  Accessories     800
2  2025-01-03   Keyboard  Accessories    1200
3  2025-01-04     Mobile  Electronics   30000
4  2025-01-05    Printer    Office      9000
```

---

### Sales Metrics

```
------ SALES METRICS ------
Total Sales : 91000
Average Sales : 18200
Maximum Sale : 50000
Minimum Sale : 800
Most Popular Product : Laptop
```

---

### Filter Output

```
Enter Category :
Electronics

         Date Product      Category  Sales
0 2025-01-01 Laptop  Electronics 50000
3 2025-01-04 Mobile Electronics 30000
```

---

## 📈 Charts Generated

### 📊 Category Wise Sales (Bar Chart)

```
Electronics ███████████████
Accessories ███
Office ████
```

---

### 📉 Sales Over Time (Line Chart)

```
Sales
|
|        ●
|      ●
|    ●
|  ●
|●____________________
      Date
```

---

### 🔥 Correlation Heatmap

A heatmap is generated showing the correlation between numeric columns.

---

## 📁 Project Structure

```
Retail-Sales-Analyzer/
│
├── retail_analyzer.py
├── retail_data.csv
├── README.md
```

---

## 🎯 Learning Outcomes

- Object-Oriented Programming (OOP)
- File Handling
- Exception Handling
- Pandas Data Analysis
- NumPy Operations
- Data Visualization
- Python Classes and Functions

---

## 👩‍💻 Author

**Simran Gohel**

Python Retail Sales Analyzer Project
