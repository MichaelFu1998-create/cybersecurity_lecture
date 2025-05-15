import sys

def find_sql_injection(lines):
    findings = []
    for i, line in enumerate(lines, start=1):
        if "SELECT" in line and "+" in line and "=" in line:
            findings.append((i, line.strip(), "Potential SQL Injection"))
    return findings

def analyze_file(filename):
    with open(filename) as f:
        lines = f.readlines()
    results = find_sql_injection(lines)
    print(f"🔍 Analysis Results for {filename}:")
    if results:
        for line, code, message in results:
            print(f" 💀 Line {line}: {message} → {code}")
    else:
        print("  ✅ No issues found.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python static_analyzer.py <filename>")
    else:
        analyze_file(sys.argv[1])
