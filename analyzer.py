import json 
from collections import defaultdict

failed_attempts = defaultdict(int)

with open("logs/sample.log", "r") as file:
    logs = file.readlines()

for line in logs:
    parts = line.strip().split()

    if len(parts) != 2:
        continue

    ip = parts[0]
    status = parts[1]

    if status == "LOGIN_FAILED":
        failed_attempts[ip] += 1

print("\n=== Suspicious IP Analysis ===\n")

report_data = []

for ip, count in failed_attempts.items():
    if count <= 2:
        risk = "LOW"
    elif count <= 5:
        risk = "MEDIUM"
    else:
        risk = "HIGH"

    print(f"IP: {ip}")
    print(f"Failed Attempts: {count}")
    print(f"Risk Level: {risk}")
    print("-" * 25)

report_data.append({
	"ip": ip, 
	"failed_attempts":
count,
	"risk":risk
})
with open("reports/security_report.json", "w") as report:
	json.dump(report_data, report, indent=4)
print("\nJSON report created successfully!")
