import pandas as pd
import matplotlib.pyplot as plt

def visualize(file_path):
    df = pd.read_csv(file_path)
    ip_counts = df[df['status']=="Failed"]['ip'].value_counts().head(10)

    ip_counts.plot(kind="bar", title="Top 10 IPs with Failed Logins")
    plt.ylabel("Failed Attempts")
    plt.xlabel("IP Address")
    plt.tight_layout()
    plt.savefig("reports/ip_analysis.png")

    print("[+] Visualization saved to reports/ip_analysis.png")

if __name__ == "__main__":
    visualize("reports/parsed_logs.csv")
