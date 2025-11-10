TGNPDCL Billing Calculator
==========================

This small Python script computes an electricity bill for TGNPDCL-style customers.

Files
- `tgnpdcl_bill.py`: main module. Exposes `calculate_bill(units, pu, cu, customer_type, other_charges=0.0)` and a CLI.

Usage

Run the script from PowerShell (example):

```powershell
python .\tgnpdcl_bill.py --units 250 --pu 7.5 --cu 100 --type domestic --other 20
```

This prints input values and the output components:
- EC: Energy Charges = units * pu
- FC: Fixed Charges = CU
- CC: Customer Charges = flat by customer type (domestic ₹30, commercial ₹75, industrial ₹150)
- ED: Electricity Duty = percentage on (EC + FC + CC) (domestic 5%, commercial 12%, industrial 18%)
- Other: Additional charges passed via --other
- Total: Sum of above

Assumptions
- Negative values for units or charges are rejected.
- Customer type must be one of: domestic, commercial, industrial (case-insensitive).

Extending
- To change CC or ED rates, edit `calculate_bill` in `tgnpdcl_bill.py`.

License: MIT
