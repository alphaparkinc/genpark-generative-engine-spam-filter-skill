"""
example_usage.py -- Demonstrates GenerativeEngineSpamFilterClient
"""
from client import GenerativeEngineSpamFilterClient

def main():
    client = GenerativeEngineSpamFilterClient()
    result = client.filter_copy("This is the best product. We highly recommend this certified solution.")
    print("[GEO Spam Filter Result]")
    print(f"Spam Score: {result['spam_score']}/100 | Verdict: {result['verdict']}")

if __name__ == "__main__":
    main()
