# Python Programming Assignment: Scholarship & Pharmacy Systems

## 1. Project Introduction and Overview

This project contains two separate, console-based Python applications. Each one solves a realistic business problem and focuses on a core programming topic:

| # | Application | File | Main Topic |
|---|-------------|------|------------|
| 1 | Student Scholarship Eligibility System | `scholarship_system.py` | Conditional statements (`if`, `elif`, `else`) |
| 2 | Smart Pharmacy Inventory & Sales Management System | `pharmacy_system.py` | Loop structures (`for`, `range()`, counters, accumulators) |

Both programs share the same approach:

- Input is collected with `input()` and checked before it is used.
- Invalid values never crash the program. The user is told what is wrong and asked again.
- Results are shown as a formatted report using `print()` and f-strings.
- The code uses meaningful variable names, comments and consistent indentation.

### Project Structure

```
.
├── scholarship_system.py   # Task 1: scholarship eligibility
├── pharmacy_system.py      # Task 2: pharmacy inventory and sales
└── README.md               # This file
```

---

## 2. Explanation of the Programs

### Program 1: Student Scholarship Eligibility System (`scholarship_system.py`)

Evaluates whether a student qualifies for a university scholarship.

**Inputs collected**

- Student name
- Academic marks (%)
- Attendance (%)
- Monthly family income (Rs.)

**Validation**

- The name cannot be empty and may contain only letters and spaces.
- Marks and attendance must be numbers between 0 and 100.
- Income must be a number that is not negative.
- Any invalid entry is rejected with a clear message and the question is asked again.

**Eligibility criteria**

| Criterion | Requirement |
|-----------|-------------|
| Academic marks | At least 80% |
| Attendance | At least 85% |
| Monthly family income | Rs. 50,000 or less |

**Decision logic**

1. The program checks each criterion and records a reason for every one that fails. A student who fails several criteria sees all of the reasons.
2. If at least one reason was recorded, the student is not eligible.
3. If all criteria are met, an `if / elif / else` chain decides the award:
   - Marks of 90% or above: **Full Scholarship**
   - Marks from 80% up to below 90%: **Partial Scholarship**

**Output**

A complete report showing the student's details, a PASS/FAIL line for each criterion, the final status, the scholarship awarded (or the reasons for ineligibility) and remarks. After each report, the user can evaluate another student.

**Main functions**

| Function | Purpose |
|----------|---------|
| `get_name()` | Reads and validates the student name |
| `get_number()` | Reads and validates a numeric value within a range |
| `evaluate()` | Applies the eligibility rules and returns the result and reasons |
| `print_report()` | Prints the evaluation report |
| `main()` | Controls the program flow |

---

### Program 2: Smart Pharmacy Inventory & Sales Management System (`pharmacy_system.py`)

Processes a batch of medicines, records the sales, updates the stock and produces a daily sales report.

**Inputs collected**

- Number of different medicines to process
- For each medicine: name, available stock, price per unit and quantity sold

**Validation**

- The number of medicines must be a whole number of at least 1.
- The medicine name cannot be empty.
- Stock and quantity sold must be whole numbers of 0 or more.
- Price must be a number greater than zero.

**Processing logic**

A `for` loop with `range()` handles each medicine in turn. Inside the loop:

1. **Stock check.** If the quantity sold is more than the available stock, the sale is **rejected** and the stock stays unchanged.
2. **No sale.** If the quantity sold is 0, the medicine is marked **NO SALE** and is not counted as a sale.
3. **Successful sale.** Otherwise the program:
   - calculates the sale amount (`quantity sold × price per unit`),
   - calculates the remaining stock (`stock − quantity sold`),
   - adds the sale amount to the running revenue total.
4. **Low-stock warning.** If the remaining stock is below 10 units, a warning is shown and the medicine is counted for restocking. This also applies to a medicine whose sale was rejected or not made, because its stock is below the limit either way.

**Accumulator and counters**

| Variable | Type | Role |
|----------|------|------|
| `total_revenue` | Accumulator | Running total of all successful sales |
| `successful_sales` | Counter | Number of sales completed |
| `rejected_sales` | Counter | Number of sales rejected for insufficient stock |
| `restock_count` | Counter | Number of medicines needing restocking |

**Output**

A final report containing a table of every medicine (status, quantity, amount, stock left), the total medicines processed, successful and rejected sales, **total pharmacy revenue**, and the **medicines requiring restocking** with their remaining stock.

**Main functions**

| Function | Purpose |
|----------|---------|
| `get_text()` | Reads a non-empty text value |
| `get_int()` | Reads a whole number above a minimum |
| `get_price()` | Reads a price greater than zero |
| `main()` | Runs the loop, calculations and final report |

---

## 3. Python Concepts Covered

### Program 1: Scholarship System

- Variables and data types (`str`, `int`, `float`)
- `input()` and `print()` with f-string formatting
- Type conversion with `float()`
- Comparison operators (`>=`, `<=`, `<`, `>`)
- Conditional statements: `if`, `elif`, `else`
- Lists, used to collect the ineligibility reasons
- `while True` loops for input validation
- `try` / `except ValueError` for error handling
- Functions with parameters and return values
- String methods: `strip()`, `isalpha()`, `replace()`, `title()`, `lower()`

### Program 2: Pharmacy System

- Variables, constants and data types (`str`, `int`, `float`)
- `input()` and `print()` with formatted output (alignment, thousands separators, decimals)
- Arithmetic operators (`*`, `-`, `+=`)
- `for` loop with `range()`
- Conditions inside loops: `if`, `elif`, `else`
- Counters and an accumulator
- Lists, used to store restock names and report rows
- Tuples, used for each row of the final report
- `while True` loops for input validation
- `try` / `except ValueError` for error handling
- Functions with parameters and return values

---

## 4. Instructions for Executing the Programs

### Requirements

- Python 3.6 or later (f-strings are required)
- No external libraries are needed

Check your Python version:

```bash
python --version
```

On some systems the command is `python3` instead of `python`.

### Run Program 1: Scholarship System

```bash
python scholarship_system.py
```

Follow the prompts. After each report, enter `y` to evaluate another student or anything else to exit.

### Run Program 2: Pharmacy System

```bash
python pharmacy_system.py
```

Enter the number of medicines, then the details for each one. The final report appears after the last medicine.

---

## 5. Sample Input and Output

### Program 1: Scholarship System

**Sample A: Full Scholarship**

Input:

```
Enter student name: ali khan
Enter academic marks (0-100%): 95
Enter attendance percentage (0-100%): 90
Enter monthly family income (Rs.): 40000
```

Output:

```
========================================================
        SCHOLARSHIP EVALUATION REPORT
========================================================
Student Name           : Ali Khan
Academic Marks         : 95.00%
Attendance             : 90.00%
Monthly Family Income  : Rs. 40,000.00
--------------------------------------------------------
Criteria Check:
  Marks >= 80%            : PASS
  Attendance >= 85%      : PASS
  Income <= Rs. 50,000   : PASS
--------------------------------------------------------
Status                 : ELIGIBLE
Scholarship Awarded    : Full Scholarship
Remarks                : Outstanding performance (90% or above).
========================================================
```

**Sample B: Not Eligible (several reasons)**

Input:

```
Enter student name: bilal ahmed
Enter academic marks (0-100%): 75
Enter attendance percentage (0-100%): 80
Enter monthly family income (Rs.): 60000
```

Output:

```
========================================================
        SCHOLARSHIP EVALUATION REPORT
========================================================
Student Name           : Bilal Ahmed
Academic Marks         : 75.00%
Attendance             : 80.00%
Monthly Family Income  : Rs. 60,000.00
--------------------------------------------------------
Criteria Check:
  Marks >= 80%            : FAIL
  Attendance >= 85%      : FAIL
  Income <= Rs. 50,000   : FAIL
--------------------------------------------------------
Status                 : NOT ELIGIBLE
Reason(s) for ineligibility:
  1. Academic marks (75.00%) are below the required 80%.
  2. Attendance (80.00%) is below the required 85%.
  3. Monthly family income (Rs. 60,000.00) exceeds the limit of Rs. 50,000.
========================================================
```

**Sample C: Input validation**

```
Enter student name: a1
  Error: Name must contain only letters and spaces.
Enter student name: fatima
Enter academic marks (0-100%): abc
  Error: Please enter a valid number.
Enter academic marks (0-100%): 150
  Error: Value cannot be greater than 100.
Enter academic marks (0-100%): 88
```

---

### Program 2: Pharmacy System

**Sample A: Sale, no sale and rejected sale**

Input and output:

```
============================================================
   SMART PHARMACY INVENTORY & SALES MANAGEMENT SYSTEM
============================================================
How many different medicines to process? 3

--- Medicine 1 of 3 ---
Medicine name: cetirizine
Available stock (units): 3
Price per unit (Rs.): 15
Quantity sold (units): 0
  No units sold for this medicine.
  WARNING: Low stock! Only 3 unit(s) of Cetirizine left. Restocking required.

--- Medicine 2 of 3 ---
Medicine name: panadol
Available stock (units): 50
Price per unit (Rs.): 5.5
Quantity sold (units): 20
  Sale amount     : Rs. 110.00
  Remaining stock : 30 unit(s)

--- Medicine 3 of 3 ---
Medicine name: brufen
Available stock (units): 8
Price per unit (Rs.): 20
Quantity sold (units): 10
  Sale rejected: only 8 unit(s) of Brufen in stock, 10 requested.
  WARNING: Low stock! Only 8 unit(s) of Brufen left. Restocking required.

============================================================
            DAILY PHARMACY SALES REPORT
============================================================
Medicine          Status      Qty    Amount (Rs.) Stock Left
------------------------------------------------------------
Cetirizine        NO SALE       0            0.00          3
Panadol           SOLD         20          110.00         30
Brufen            REJECTED     10            0.00          8
------------------------------------------------------------
Total medicines processed    : 3
Successful sales             : 1
Rejected sales (low stock)   : 1
Total pharmacy revenue       : Rs. 110.00
Medicines requiring restock  : 2
   - Cetirizine (3 left)
   - Brufen (8 left)
============================================================
```

**Sample B: Selling all the stock**

Input:

```
How many different medicines to process? 1
Medicine name: insulin
Available stock (units): 10
Price per unit (Rs.): 850
Quantity sold (units): 10
```

Output:

```
  Sale amount     : Rs. 8,500.00
  Remaining stock : 0 unit(s)
  WARNING: Low stock! Only 0 unit(s) of Insulin left. Restocking required.

Total medicines processed    : 1
Successful sales             : 1
Rejected sales (low stock)   : 0
Total pharmacy revenue       : Rs. 8,500.00
Medicines requiring restock  : 1
   - Insulin (0 left)
```

**Sample C: Input validation**

```
How many different medicines to process? 0
  Error: Value must be at least 1.
How many different medicines to process? abc
  Error: Please enter a whole number (e.g. 25).
How many different medicines to process? 2

--- Medicine 1 of 2 ---
Medicine name:
  Error: This field cannot be empty.
Medicine name: amoxil
Available stock (units): 12
Price per unit (Rs.): -5
  Error: Price must be greater than zero.
Price per unit (Rs.): 45.25
```

---

## Test Scenarios Covered

| Program | Scenarios tested |
|---------|------------------|
| Scholarship | Full scholarship; partial scholarship; exact boundaries (80%, 85%, 90%, Rs. 50,000); only one criterion failing; all criteria failing; invalid name, text and out-of-range values; evaluating multiple students in one run |
| Pharmacy | Normal sale; sale of all stock; rejected sale for insufficient stock; no sale (quantity 0); low-stock warnings; mixed batches of several medicines; invalid count, price, quantity and empty name |
