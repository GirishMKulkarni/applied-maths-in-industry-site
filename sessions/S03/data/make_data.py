"""
make_data.py — generate the two data files students import in Session 3.

Run from this folder:  python3 make_data.py

Produces:
  shop_sales.csv          a clean, ready-to-read shop-sales file (the first
                          successful import — a confidence win)
  shop_sales_messy.xlsx   a multi-sheet workbook the way a regional manager
                          would actually email it: several regional sheets, a
                          lookup sheet, and real-world messes (blanks, "NA" and
                          "-" and 999 markers, a duplicate row, prices stored as
                          text) — the material for the cleaning lab.

Kept in the repo and committed so the files are reproducible and reviewable.
"""
import pandas as pd

# --------------------------------------------------------------------------- #
#  1. shop_sales.csv  — clean; loads and summarises with no cleaning at all
# --------------------------------------------------------------------------- #

clean = pd.DataFrame({
    "date": ["2024-01-03", "2024-01-05", "2024-01-06", "2024-01-08",
             "2024-01-09", "2024-01-11", "2024-01-12", "2024-01-14",
             "2024-01-15", "2024-01-17", "2024-01-18", "2024-01-20"],
    "city": ["Pune", "Mumbai", "Pune", "Delhi", "Mumbai", "Pune",
             "Delhi", "Mumbai", "Pune", "Mumbai", "Delhi", "Pune"],
    "customer": ["Asha", "Ravi", "Meera", "John", "Sara", "Asha",
                 "Vikram", "Ravi", "Kiran", "Sara", "John", "Meera"],
    "units": [10, 4, 7, 2, 9, 5, 6, 8, 3, 13, 4, 6],
    "price": [250, 300, 250, 180, 300, 250, 180, 300, 250, 300, 180, 250],
})
clean.to_csv("shop_sales.csv", index=False)
print("wrote shop_sales.csv  ", clean.shape,
      "| units per city:", clean.groupby("city")["units"].sum().to_dict())

# --------------------------------------------------------------------------- #
#  2. shop_sales_messy.xlsx  — multi-sheet, deliberately messy (the lab)
# --------------------------------------------------------------------------- #
# Messes on purpose:
#   * price stored as TEXT, with comma thousands-separators ("1,300")
#   * missing units written three different ways: "NA", "-", and the code 999
#   * one blank price cell
#   * one duplicate row (Pune / Meera, in North)

north = pd.DataFrame({
    "date": ["2024-02-01", "2024-02-03", "2024-02-03", "2024-02-05"],
    "city": ["Pune", "Pune", "Pune", "Mumbai"],
    "customer": ["Asha", "Meera", "Meera", "Ravi"],
    "units": [10, 7, 7, "NA"],               # "NA" text marker for missing
    "price": ["250", "250", "250", "1,300"],  # text, with a comma separator
})

south = pd.DataFrame({
    "date": ["2024-02-02", "2024-02-04", "2024-02-06"],
    "city": ["Delhi", "Delhi", " hyderabad"],   # messy text: leading space, lowercase
    "customer": ["John", "Vikram", "Latha"],
    "units": [2, "-", 999],                  # "-" and 999 both mean missing
    "price": ["180", "180", "1,210"],
})

west = pd.DataFrame({
    "date": ["2024-02-07", "2024-02-08", "2024-02-09"],
    "city": ["Nagpur", "Nashik", "nagpur "],    # messy text: lowercase, trailing space
    "customer": ["Kiran", "Sara", "Asha"],
    "units": [5, 8, 6],
    "price": ["220", "", "1,220"],           # one blank price
})

lookup = pd.DataFrame({
    "city": ["Pune", "Mumbai", "Delhi", "Hyderabad", "Nagpur", "Nashik"],
    "region": ["North", "North", "South", "South", "West", "West"],
})

with pd.ExcelWriter("shop_sales_messy.xlsx", engine="openpyxl") as xl:
    north.to_excel(xl, sheet_name="North", index=False)
    south.to_excel(xl, sheet_name="South", index=False)
    west.to_excel(xl, sheet_name="West", index=False)
    lookup.to_excel(xl, sheet_name="lookup", index=False)
print("wrote shop_sales_messy.xlsx  (sheets: North, South, West, lookup)")
