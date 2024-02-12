import os
import schedule
import time

def enable_domain(domain):
    os.system(f"pihole --whitelist {domain}")

def disable_domain(domain):
    os.system(f"pihole --blacklist {domain}")

# Replace 'example.com' with your domain
domain = 'example.com'

# Schedule the enabling and disabling
schedule.every().day.at("09:00").do(enable_domain, domain=domain)  # Enable at 9:00
schedule.every().day.at("18:00").do(disable_domain, domain=domain)  # Disable at 18:00

while True:
    schedule.run_pending()
    time.sleep(1)