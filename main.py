import os
import schedule
import time

import pihole as ph

p = ph.PiHole("192.168.3.7")
# p.authenticate("p1h0l34dm1n")


# pi-hole commands
# https://docs.pi-hole.net/core/pihole-command/

def enable_domain(domain):
    os.system(f"pihole -w {domain}")

def disable_domain(domain):
    os.system(f"pihole -b {domain}")
        
# Replace 'example.com' with your domain
domain = 'taobao.com'

# Schedule the enabling and disabling
# schedule.every().day.at("09:00").do(enable_domain, domain=domain)  # Enable at 9:00
# schedule.every().day.at("18:00").do(disable_domain, domain=domain)  # Disable at 18:00

# while True:
#     schedule.run_pending()
#     time.sleep(1)