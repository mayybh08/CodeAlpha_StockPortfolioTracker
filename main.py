# CodeAlpha Internship
# Task 2: Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 175,
    "MSFT": 420
}

# Store portfolio details
portfolio = {}


def display_stocks():
    """Display available stocks and their prices."""
    print("\nAvailable Stocks")
    print("-" * 30)

    for stock, price in stock_prices.items():
        print(f"{stock:<10} Rs. {price}")


def add_stock():
    """Add a stock to the portfolio."""
    stock = input("\nEnter stock symbol: ").upper().strip()

    if stock not in stock_prices:
        print("Stock not available.")
        return

    try:
        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("Quantity must be greater than 0.")
            return

    except ValueError:
        print("Please enter a valid number.")
        return

    investment = stock_prices[stock] * quantity

    if stock in portfolio:
        portfolio[stock]["quantity"] += quantity
        portfolio[stock]["investment"] += investment
    else:
        portfolio[stock] = {
            "quantity": quantity,
            "investment": investment
        }

    print(f"\n{quantity} shares of {stock} added successfully.")
    print(f"Investment: Rs. {investment:,.2f}")


def display_portfolio():
    """Display the current portfolio."""
    if not portfolio:
        print("\nYour portfolio is empty.")
        return

    print("\nYour Stock Portfolio")
    print("-" * 60)
    print(
        f"{'Stock':<10}"
        f"{'Quantity':<12}"
        f"{'Price':<15}"
        f"{'Investment':<15}"
    )
    print("-" * 60)

    total_investment = 0

    for stock, details in portfolio.items():
        quantity = details["quantity"]
        price = stock_prices[stock]
        investment = details["investment"]

        total_investment += investment

        print(
            f"{stock:<10}"
            f"{quantity:<12}"
            f"Rs. {price:<11,.2f}"
            f"Rs. {investment:,.2f}"
        )

    print("-" * 60)
    print(f"Total Investment: Rs. {total_investment:,.2f}")


def save_portfolio():
    """Save portfolio details to a text file."""
    if not portfolio:
        print("\nNothing to save. Your portfolio is empty.")
        return

    total_investment = 0

    with open("portfolio.txt", "w", encoding="utf-8") as file:
        file.write("STOCK PORTFOLIO REPORT\n")
        file.write("=" * 50 + "\n\n")

        for stock, details in portfolio.items():
            quantity = details["quantity"]
            price = stock_prices[stock]
            investment = details["investment"]

            total_investment += investment

            file.write(f"Stock: {stock}\n")
            file.write(f"Quantity: {quantity}\n")
            file.write(f"Price per Share: Rs. {price:,.2f}\n")
            file.write(f"Investment: Rs. {investment:,.2f}\n")
            file.write("-" * 40 + "\n")

        file.write(
            f"\nTotal Investment: Rs. {total_investment:,.2f}\n"
        )

    print("\nPortfolio saved successfully!")
    print("File created: portfolio.txt")


def main():
    """Run the Stock Portfolio Tracker."""

    while True:
        print("\n" + "=" * 45)
        print("       STOCK PORTFOLIO TRACKER")
        print("=" * 45)

        print("1. View Available Stocks")
        print("2. Add Stock to Portfolio")
        print("3. View Portfolio")
        print("4. Save Portfolio")
        print("5. Exit")

        choice = input("\nEnter your choice (1-5): ").strip()

        if choice == "1":
            display_stocks()
            input("\nPress Enter to continue...")

        elif choice == "2":
            add_stock()
            input("\nPress Enter to continue...")

        elif choice == "3":
            display_portfolio()
            input("\nPress Enter to continue...")

        elif choice == "4":
            save_portfolio()
            input("\nPress Enter to continue...")

        elif choice == "5":
            print("\nThank you for using Stock Portfolio Tracker!")
            break

        else:
            print("\nInvalid choice. Please select 1-5.")
            input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()