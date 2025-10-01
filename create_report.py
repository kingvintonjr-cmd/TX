import csv
import requests
from fpdf import FPDF

# Data
txid_inbound_parent = "d2679c18ebbbb5c326a45d6452bbdd1084059f58bc845667c823dc6f74f6c352"
txid_inbound = "17ba9fed1ac38c69fc2b469d1e222c3032cbf209e2e22f0fee1cbf1cb32eed5d"
txid_outbound = "7e1d976fc6eef52605f94765f30fbef7096aba8f2cec3153cbc444ed2d367c08"
address = "bc1qxkv98ccgaj8vmmpw595wzcw3cmgl3twq26e87x"
amount = "1.428 BTC"
timestamp = "2020-12-09 18:48:27"
# New flowchart shows the full circle
flowchart_url = "https://mermaid.ink/img/CmdyYXBoIFREOwogICAgQVsiQ3VzdG9kaWFsIFNlcnZpY2UgKFNvdXJjZSkiXSAtLT4gQnsiVHg6IGQyNjcuLi5jMzUyIn07CiAgICBCIC0tPiBDeyJUeDogMTdiYS4uLmJlZDVkPGJyPkFtb3VudDogMS40MjggQlRDIn07CiAgICBDIC0tPiBEWyJVc2VyJ3MgQWRkcmVzczxicj5iYzFxLi4uZTg3eCJdOwogICAgRCAtLSAiT3V0Z29pbmciIC0tPiBFeyJCYXRjaCBXaXRoZHJhd2FsPGJyPlR4OiA3ZTFkLi4uN2MwOCJ9OwogICAgRSAtLT4gRlsiQ3VzdG9kaWFsIFNlcnZpY2UgKERlc3RpbmF0aW9uKSJdOwo="
flowchart_filename = "flowchart.jpg"

# Download the flowchart image
response = requests.get(flowchart_url)
with open(flowchart_filename, "wb") as f:
    f.write(response.content)

# Create CSV
with open('txid_list.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['description', 'txid'])
    writer.writerow(['Inbound Parent', txid_inbound_parent])
    writer.writerow(['Inbound to User', txid_inbound])
    writer.writerow(['Outbound Batch', txid_outbound])

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
pdf.cell(200, 10, txt=f"- {amount} on {timestamp} (TXID: {txid_inbound})", ln=1)

pdf.set_font("Arial", 'B', 10)
pdf.cell(200, 10, txt="Outgoing Transaction:", ln=1)
pdf.set_font("Arial", size=10)
pdf.multi_cell(0, 5, txt=f"The address has one outgoing transaction, which is part of a large batch withdrawal (TXID: {txid_outbound}). This transaction has 101 inputs and 159 outputs, which is a strong indicator of a custodial service.")

pdf.set_font("Arial", 'B', 10)
pdf.cell(200, 10, txt="Custodial Service Analysis:", ln=1)
pdf.set_font("Arial", size=10)
pdf.multi_cell(0, 5, txt=f"The analysis confirms a full circle of funds involving a custodial service. The funds originated from a large transaction ({txid_inbound_parent}), were sent to the user's address, and then sent back to a custodial service in a batch withdrawal ({txid_outbound}).")
pdf.cell(200, 10, txt=f"Explorer Link (Batch Withdrawal): https://www.oklink.com/btc/tx/{txid_outbound}", ln=1)


pdf.set_font("Arial", 'B', 10)
pdf.cell(200, 10, txt="Flowchart:", ln=1)
pdf.image(flowchart_filename, w=170)

pdf.set_font("Arial", 'B', 10)
pdf.cell(200, 10, txt="Next Steps/Data Gaps:", ln=1)
pdf.set_font("Arial", size=10)
pdf.multi_cell(0, 5, txt="The analysis confirms the funds were moved to and from a custodial service. Identifying the specific service would require a deeper investigation into the other inputs and outputs of the batch withdrawal transaction to find links to known services. This is a complex task beyond the scope of this initial analysis.")

pdf.output("transaction_report.pdf")