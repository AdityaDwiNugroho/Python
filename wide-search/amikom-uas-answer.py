import requests
from datetime import datetime, timedelta
from concurrent.futures import ThreadPoolExecutor

# --- SETTINGS ---
NIM = "250152XX"
YEAR_SEM = "20251"
START_DATE = "20260120"  # Jan 20th
DAYS_TO_CHECK = 6        # How many days to look forward
# ----------------

BASE_URL = f"https://assignment.amikom.ac.id/resp/{YEAR_SEM}/{NIM}/{NIM}_"

def check_url(timestamp):
    full_url = f"{BASE_URL}{timestamp}.pdf"
    try:
        # 'stream=True' and 'head' are faster for checking existence
        r = requests.head(full_url, timeout=2)
        if r.status_code == 200:
            return full_url
    except:
        pass
    return None

def main():
    start_dt = datetime.strptime(START_DATE, "%Y%m%d")
    print(f"Starting search for NIM {NIM}...")

    # We use a ThreadPool to check 50 links at a time so it's not slow
    with ThreadPoolExecutor(max_workers=50) as executor:
        for day in range(DAYS_TO_CHECK):
            current_date = (start_dt + timedelta(days=day)).strftime("%Y%m%d")
            print(f"Checking date: {current_date}...")

            for hour in range(24):
                timestamps = [f"{current_date}{hour:02d}{m:02d}{s:02d}" for m in range(60) for s in range(60)]
                
                # Check all 3600 seconds in this hour simultaneously
                results = executor.map(check_url, timestamps)
                
                for link in results:
                    if link:
                        print(f"\n[FOUND!] -> {link}")
                        return

if __name__ == "__main__":
    main()