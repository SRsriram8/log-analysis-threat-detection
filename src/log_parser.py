import re
import pandas as pd

def parse_log(file_path):
    pattern = r'(?P<date>\w{3} \d+ \d+:\d+:\d+) .* (?P<status>Failed|Accepted) password for (?P<user>\w+) from (?P<ip>\d+\.\d+\.\d+\.\d+)'
    rows = []

    with open(file_path, 'r') as f:
        for line in f:
            match = re.search(pattern, line)
            if match:
                rows.append(match.groupdict())

    df = pd.DataFrame(rows)
    df.to_csv("reports/parsed_logs.csv", index=False)
    return df

if __name__ == "__main__":
    df = parse_log("data/sample_auth.log")
    print("[+] Parsed logs saved to reports/parsed_logs.csv")
    print(df.head())
