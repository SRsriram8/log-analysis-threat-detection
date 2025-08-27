import pandas as pd

def detect_bruteforce(file_path):
    df = pd.read_csv(file_path)
    alerts = []

    grouped = df[df['status']=="Failed"].groupby('ip').size()

    for ip, count in grouped.items():
        if count > 5:  # threshold
            alerts.append(f"⚠️ Brute-force attack suspected from {ip} ({count} failed attempts)")

    with open("reports/threat_report.txt", "w") as f:
        f.write("\n".join(alerts))

    print("[+] Threat report generated at reports/threat_report.txt")

if __name__ == "__main__":
    detect_bruteforce("reports/parsed_logs.csv")
