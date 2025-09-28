import json

SNYK_JSON = "snyk-result.json"
HTML_OUTPUT = "snyk_report.html"

def main():
    with open(SNYK_JSON, "r") as f:
        snyk_data = json.load(f)
    
    html = []
    html.append("<html><head><title>Snyk Report</title></head><body>")
    html.append("<h1>Snyk Security Report</h1>")

    vulns = snyk_data.get("vulnerabilities", [])
    if vulns:
        html.append(f"<h2>Found {len(vulns)} vulnerabilities</h2>")
        html.append("<ul>")
        for vuln in vulns:
            title = vuln.get("title", "No title")
            severity = vuln.get("severity", "unknown")
            package = vuln.get("packageName", "unknown")
            description = vuln.get("description", "")
            html.append(f"<li><b>{title}</b> ({severity}) in <code>{package}</code><br>{description}</li>")
        html.append("</ul>")
    else:
        html.append("<p>No vulnerabilities found or invalid snyk-result.json structure.</p>")

    html.append("</body></html>")

    with open(HTML_OUTPUT, "w") as hf:
        hf.write("\n".join(html))

if __name__ == "__main__":
    main()
