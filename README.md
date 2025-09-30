# Bitcoin Transaction Analysis Reporter

This project contains a Python script (`create_report.py`) that generates a PDF report and a CSV file based on a hardcoded analysis of a Bitcoin address.

## How to Use

### 1. Prerequisites

- Python 3.x
- `pip` for installing packages

### 2. Installation

Before running the script, you need to install the required Python libraries. Open your terminal or command prompt and run the following command:

```bash
pip install fpdf requests
```

### 3. Running the Script

To generate the report, simply execute the `create_report.py` script from your terminal:

```bash
python create_report.py
```

This will create two files in the same directory:

- `transaction_report.pdf`: A 1-pager PDF containing the transaction analysis.
- `txid_list.csv`: A CSV file listing the transaction IDs included in the analysis.

### 4. Note on Data

The data used for the analysis (transaction IDs, amounts, etc.) is currently hardcoded within the `create_report.py` script. To analyze a different set of transactions, you will need to manually update the data variables in the script.