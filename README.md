# ReturnsCalculator

ReturnsCalculator is a Python package designed to simplify the calculation of various financial returns for assets. It provides methods to compute metrics like Compound Annual Growth Rate (CAGR), Absolute Return, Calendar Year Return, Financial Year Return, and Monthly Return from your financial data. This package is ideal for analysts, portfolio managers, or anyone working with time-series financial data.

## Key Features:

    CAGR Calculation: Easily compute the compound annual growth rate for assets over a period.
    Absolute Return: Calculate the total return on an asset from the beginning to the end of a period.
    Calendar Year and Financial Year Returns: Analyze returns on an annual or financial year basis.
    Monthly Returns: Break down asset performance month by month.

## Installation:

You can install the package directly from GitHub:
```
pip install git+https://github.com/pgvetrivel/returns_calculator.git
```
## Usage Example:

```python
import pandas as pd
from returns_calculator import ReturnsCalculator

# Example DataFrame
df = pd.DataFrame({
    'asset': ['Asset1', 'Asset1', 'Asset2', 'Asset2'],
    'date': pd.to_datetime(['2020-01-01', '2021-01-01', '2020-01-01', '2021-01-01']),
    'price': [100, 120, 200, 220]
})

# Instantiate the ReturnsCalculator
calculator = ReturnsCalculator(df, 'asset', 'date', 'price')

# Calculate CAGR
cagr_df = calculator.cagr()
print(cagr_df)
