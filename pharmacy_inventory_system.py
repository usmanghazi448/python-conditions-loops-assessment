"""
Smart Pharmacy Inventory & Sales Management System
Topic: Loop Structures (for loop, range(), conditions inside loops,
       counters and accumulators)

Processes a batch of medicines, records each sale, updates stock,
raises low-stock warnings and produces a final daily report.
"""

LOW_STOCK_LIMIT = 10  # remaining stock below this needs restocking


def get_text(prompt):
    """Ask for a non-empty text value (medicine name)."""
    while True:
        value = input(prompt).strip()
        if value == "":
            print("  Error: This field cannot be empty.")
        else:
            return value.title()


def get_int(prompt, minimum):
    """Ask for a whole number >= minimum; repeat until valid."""
    while True:
        text = input(prompt).strip()
        try:
            value = int(text)
        except ValueError:
            print("  Error: Please enter a whole number (e.g. 25).")
            continue
        if value < minimum:
            print(f"  Error: Value must be at least {minimum}.")
        else:
            return value


def get_price(prompt):
    """Ask for a price greater than zero; repeat until valid."""
    while True:
        text = input(prompt).strip()
        try:
            value = float(text)
        except ValueError:
            print("  Error: Please enter a valid price (e.g. 12.50).")
            continue
        if value <= 0:
            print("  Error: Price must be greater than zero.")
        else:
            return value


def main():
    print("=" * 60)
    print("   SMART PHARMACY INVENTORY & SALES MANAGEMENT SYSTEM")
    print("=" * 60)

    # Step 1: how many medicines will be processed
    total_medicines = get_int("How many different medicines to process? ", 1)

    # ---------- Accumulators and counters ----------
    total_revenue = 0.0        # accumulator: sum of all sales amounts
    successful_sales = 0       # counter: sales that went through
    rejected_sales = 0         # counter: sales rejected (not enough stock)
    restock_count = 0          # counter: medicines needing restocking
    restock_list = []          # names of medicines needing restocking
    summary_rows = []          # one line per medicine for the final table

    # Step 2: process every medicine with a for loop
    for number in range(1, total_medicines + 1):
        print(f"\n--- Medicine {number} of {total_medicines} ---")

        # Step 3: collect the details
        name = get_text("Medicine name: ")
        stock = get_int("Available stock (units): ", 0)
        price = get_price("Price per unit (Rs.): ")
        quantity_sold = get_int("Quantity sold (units): ", 0)

        # Step 4: check stock availability
        if quantity_sold > stock:
            rejected_sales += 1
            sale_amount = 0.0
            remaining = stock  # nothing was sold, stock unchanged
            status = "REJECTED"
            print(f"  Sale rejected: only {stock} unit(s) of {name} in stock, "
                  f"{quantity_sold} requested.")
        elif quantity_sold == 0:
            # Nothing was sold today: not a sale, stock stays the same
            sale_amount = 0.0
            remaining = stock
            status = "NO SALE"
            print("  No units sold for this medicine.")
        else:
            # Steps 5 and 6: sale amount and remaining stock
            sale_amount = quantity_sold * price
            remaining = stock - quantity_sold
            total_revenue += sale_amount       # Step 8: accumulate revenue
            successful_sales += 1
            status = "SOLD"
            print(f"  Sale amount     : Rs. {sale_amount:,.2f}")
            print(f"  Remaining stock : {remaining} unit(s)")

        # Step 7 and 9: low-stock warning and restock counter
        if remaining < LOW_STOCK_LIMIT:
            restock_count += 1
            restock_list.append(f"{name} ({remaining} left)")
            print(f"  WARNING: Low stock! Only {remaining} unit(s) of {name} "
                  f"left. Restocking required.")

        summary_rows.append((name, status, quantity_sold, sale_amount, remaining))

    # Step 10: final report
    line = "=" * 60
    print("\n" + line)
    print("            DAILY PHARMACY SALES REPORT")
    print(line)
    print(f"{'Medicine':<18}{'Status':<10}{'Qty':>5}{'Amount (Rs.)':>16}{'Stock Left':>11}")
    print("-" * 60)
    for name, status, qty, amount, remaining in summary_rows:
        print(f"{name:<18}{status:<10}{qty:>5}{amount:>16,.2f}{remaining:>11}")
    print("-" * 60)
    print(f"Total medicines processed    : {total_medicines}")
    print(f"Successful sales             : {successful_sales}")
    print(f"Rejected sales (low stock)   : {rejected_sales}")
    print(f"Total pharmacy revenue       : Rs. {total_revenue:,.2f}")
    print(f"Medicines requiring restock  : {restock_count}")
    if restock_count > 0:
        for item in restock_list:
            print(f"   - {item}")
    print(line)


if __name__ == "__main__":
    main()