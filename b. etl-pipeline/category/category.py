class product:
    """Product type validation"""
    standard_product = {'Smartphone', 'Tablet', 'Laptop', 'Smartwatch', 'Headphones'}
    standard_sku = {'SKU1004', 'SKU1002', 'SKU1005', 'SKU1001', 'SKU1003', 'LTP123',
        'SMP234', 'TBL345', 'HDP456', 'SWT567'}

class order:
    """Order status validation"""
    status = {'Cancelled', 'Completed'}

class ship:
    """Shipping type validation"""
    standard_shipping = {'Standard', 'Overnight', 'Express', 'Same Day', 'Expedited'}

class payment:
    """Payment method validation"""
    method = {'Credit Card', 'PayPal', 'Cash', 'Debit Card', 'Bank Transfer'}

class sex:
    """Gender category validation"""
    gender_category = {'Male', 'Female'}

class members:
    """Loyalty membership validation"""
    membership_class = {'No', 'Yes'}
