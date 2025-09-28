import json
from fpdf import FPDF

with open('snyk-result.json', 'r') as f:
    data = json.load(f)

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, txt="Snyk Vulnerability Report", ln=True, align='C')

for vuln in data.get('vulnerabilities', []):
    pdf.cell(200, 10, txt=f"ID: {vuln['id']}", ln=True)
    pdf.cell(200, 10, txt=f"Title: {vuln['title']}", ln=True)
    pdf.cell(200, 10, txt=f"Severity: {vuln['severity']}", ln=True)
    pdf.cell(200, 10, txt=f"Package: {vuln['packageName']}", ln=True)
    pdf.cell(200, 10, txt=f"Description: {vuln['description']}", ln=True)
    pdf.ln(10)

pdf.output("snyk-report.pdf")
