"""
### Task 08 - Invoice Code Formatter

> 💼 **Real-world use:** Formatting IDs or codes in finance or ERP systems.
- Given an invoice number like 23, generate code in the format `INV00023`.
  - Input: "`23`"
  - Output: `Output: INV00023`
"""

invoice_num=input("Input invoice number: ")

if invoice_num.isdigit():
    invoice_num=int(invoice_num)
    print(f"INV000{invoice_num}")
else:
    print("Please input number")
