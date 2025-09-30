import csv
import requests
from fpdf import FPDF

# Data
txid_1 = "d2679c18ebbbb5c326a45d6452bbdd1084059f58bc845667c823dc6f74f6c352"
txid_2 = "17ba9fed1ac38c69fc2b469d1e222c3032cbf209e2e22f0fee1cbf1cb32eed5d"
txid_3 = "7e1d976fc6eef52605f94765f30fbef7096aba8f2cec3153cbc444ed2d367c08"
address = "bc1qxkv98ccgaj8vmmpw595wzcw3cmgl3twq26e87x"
amount = "1.428 BTC"
timestamp = "2020-12-09 18:48:27"
flowchart_url = "https://mermaid.ink/img/CmdyYXBoIFREOwogICAgQVsiU291cmNlPGJyPihMaWtlbHkgQ3VzdG9kaWFsIFNlcnZpY2UpIl0gLS0-IEJ7IlRyYW5zYWN0aW9uPGJyPmQyNjcuLi5jMzUyIn07CiAgICBCIC0tPiBDeyJUcmFuc2FjdGlvbjxicj4xN2JhLi4uZWVkNWQ8YnI-QW1vdW50OiAxLjQyOCBCVEMifTsKICAgIEMgLS0-IERbIlVzZXIncyBBZGRyZXNzPGJyPmJjMXEuLi5lODd4Il07CiAgICBEIC0tPiBFeyJCYXRjaCBXaXRoZHJhd2FsPGJyPjdlMWQuLi43YzA4PGJyPigxMDEgaW5wdXRzLCAxNTkgb3V0cHV0cykifTsKICAgIEUgLS0-IEZbIkxpa2VseSBDdXN0b2RpYWwgU2VydmljZSJdOwo="
flowchart_filename = "flowchart.jpg"

# Download the flowchart image
response = requests.get(flowchart_url)
with open(flowchart_filename, "wb") as f:
    f.write(response.content)

# Create CSV
with open('txid_list.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['txid'])
    writer.writerow([txid_1])
    writer.writerow([txid_2])
    writer.writerow([txid_3])

# Create PDF
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)

pdf.cell(200, 10, txt="Bitcoin Transaction Analysis Report", ln=1, align="C")

pdf.set_font("Arial", 'B', 10)
pdf.cell(200, 10, txt="Address Analyzed:", ln=1)
pdf.set_font("Arial", size=10)
pdf.cell(200, 10, txt=address, ln=1)

pdf.set_font("Arial", 'B', 10)
pdf.cell(200, 10, txt="Inbound Transaction:", ln=1)
pdf.set_font("Arial", size=10)
pdf.multi_cell(0, 5, txt="The address has only one inbound transaction.")
pdf.cell(200, 10, txt=f"- {amount} (TXID: {txid_2})", ln=1)

pdf.set_font("Arial", 'B', 10)
pdf.cell(200, 10, txt="First-Hop Flow:", ln=1)
pdf.set_font("Arial", size=10)
pdf.cell(200, 10, txt=f"- Hash: {txid_2}", ln=1)
pdf.cell(200, 10, txt=f"- Amount: {amount}", ln=1)
pdf.cell(200, 10, txt=f"- Timestamp: {timestamp}", ln=1)

pdf.set_font("Arial", 'B', 10)
pdf.cell(200, 10, txt="Exchange/Custodial Service Analysis:", ln=1)
pdf.set_font("Arial", size=10)
pdf.multi_cell(0, 5, txt=f"The initial transaction ({txid_1}) showed characteristics of a custodial service withdrawal. Further analysis of the user-provided transaction ({txid_3}) confirms this. This transaction is a large batch withdrawal with 101 inputs and 159 outputs, a common practice for exchanges to save on fees. The user's address is one of the inputs to this transaction, confirming the funds were sent to a custodial service.")
pdf.cell(200, 10, txt=f"Explorer Link (Initial TX): https://www.oklink.com/btc/tx/{txid_1}", ln=1)
pdf.cell(200, 10, txt=f"Explorer Link (Batch Withdrawal): https://www.oklink.com/btc/tx/{txid_3}", ln=1)


pdf.set_font("Arial", 'B', 10)
pdf.cell(200, 10, txt="Flowchart:", ln=1)
pdf.image(flowchart_filename, w=150)

pdf.set_font("Arial", 'B', 10)
pdf.cell(200, 10, txt="Next Steps/Data Gaps:", ln=1)
pdf.set_font("Arial", size=10)
pdf.multi_cell(0, 5, txt="The analysis confirms the funds were moved to a custodial service. Identifying the specific service would require a deeper investigation into the other inputs and outputs of the batch withdrawal transaction to find links to known services. This is a complex task beyond the scope of this initial analysis.")

pdf.output("transaction_report.pdf")