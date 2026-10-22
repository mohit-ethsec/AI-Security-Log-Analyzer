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
