# Stock Portfolio Tracker

A simple Python-based Stock Portfolio Tracker developed as part of the **CodeAlpha Python Programming Internship**.

## 📌 Project Overview

The Stock Portfolio Tracker is a menu-driven Python application that allows users to manage a simple stock portfolio. Users can view available stocks, add stocks with their desired quantity, calculate investment values, view their portfolio, and save the portfolio report to a text file.

Stock prices are predefined using a Python dictionary, as specified in the CodeAlpha internship task.

## ✨ Features

- View available stocks and their prices
- Add stocks to the portfolio
- Enter stock quantity
- Calculate individual stock investment
- View complete portfolio
- Calculate total investment value
- Save portfolio details to a text file
- Input validation and error handling
- Simple and user-friendly menu-driven interface

## 🛠️ Technologies Used

- Python 3
- Dictionaries
- Functions
- Loops
- Conditional Statements
- Exception Handling
- File Handling

## 📂 Project Structure

```text
StockPortfolioTracker/
│
├── main.py
├── portfolio.txt
└── README.md
```

## 📊 Available Stocks

The application currently uses the following predefined stock prices:

| Stock | Price |
|-------|------:|
| AAPL  | Rs. 180 |
| TSLA  | Rs. 250 |
| GOOGL | Rs. 140 |
| AMZN  | Rs. 175 |
| MSFT  | Rs. 420 |

## 🚀 How to Run

### 1. Install Python

Make sure Python 3 is installed on your computer.

### 2. Open the Project

Open the `StockPortfolioTracker` folder in VS Code.

### 3. Open the Terminal

In VS Code, select:

```text
Terminal → New Terminal
```

### 4. Run the Program

Execute the following command:

```bash
python main.py
```

## 💻 How to Use

After running the program, the following menu will appear:

```text
=============================================
       STOCK PORTFOLIO TRACKER
=============================================
1. View Available Stocks
2. Add Stock to Portfolio
3. View Portfolio
4. Save Portfolio
5. Exit

Enter your choice (1-5):
```

### Option 1 — View Available Stocks

Select option `1` to display all available stocks along with their predefined prices.

Example:

```text
Available Stocks
------------------------------
AAPL       Rs. 180
TSLA       Rs. 250
GOOGL      Rs. 140
AMZN       Rs. 175
MSFT       Rs. 420
```

### Option 2 — Add Stock to Portfolio

Select option `2` to add a stock to your portfolio.

Enter the stock symbol and quantity when prompted.

Example:

```text
Enter your choice (1-5): 2

Enter stock symbol: AAPL
Enter quantity: 10
```

The program calculates the investment value based on the stock price and quantity.

Calculation:

```text
Stock Price × Quantity

Rs. 180 × 10 = Rs. 1,800
```

Output:

```text
10 shares of AAPL added successfully.
Investment: Rs. 1,800.00
```

### Option 3 — View Portfolio

Select option `3` to view all stocks currently added to the portfolio.

The portfolio displays:

- Stock symbol
- Quantity
- Price per share
- Individual investment
- Total investment

Example:

```text
Your Stock Portfolio
------------------------------------------------------------
Stock     Quantity    Price          Investment
------------------------------------------------------------
AAPL      10          Rs. 180.00     Rs. 1,800.00
------------------------------------------------------------
Total Investment: Rs. 1,800.00
```

### Option 4 — Save Portfolio

Select option `4` to save the current portfolio details to a text file.

The file is named:

```text
portfolio.txt
```

The saved report contains:

- Stock symbol
- Quantity
- Price per share
- Individual investment
- Total investment

Example report:

```text
STOCK PORTFOLIO REPORT
==================================================

Stock: AAPL
Quantity: 10
Price per Share: Rs. 180.00
Investment: Rs. 1,800.00
----------------------------------------

Total Investment: Rs. 1,800.00
```

### Option 5 — Exit

Select option `5` to exit the Stock Portfolio Tracker.

Output:

```text
Thank you for using Stock Portfolio Tracker!
```

## 🎯 Learning Outcomes

Through this project, I practiced:

- Python programming fundamentals
- Working with dictionaries
- Creating reusable functions
- Handling user input
- Performing arithmetic calculations
- Using loops and conditional statements
- Handling invalid input using exception handling
- Working with text files
- Building a menu-driven application

## 🏢 Internship

This project was developed as part of the **CodeAlpha Python Programming Internship**.

### Task 2 — Stock Portfolio Tracker

The project follows the CodeAlpha task requirements by using user-entered stock names and quantities, predefined stock prices, investment calculations, and optional file handling for saving the portfolio.

## 👩‍💻 Author

**Mayuri Bhaladhare**

B.Tech — Artificial Intelligence & Data Science

## 📜 License

This project is created for educational and internship purposes.
