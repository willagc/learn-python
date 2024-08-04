#!/usr/bin/env python3
import subprocess
import re

# Function to ping three DNS servers, calculate latency, and print it
def dns_latency(dns1, dns2, dns3, dns4):
    dns_list = [dns1, dns2, dns3, dns4]
    
    for dns in dns_list:
        result = subprocess.run(f"ping -c 3 {dns}", shell=True)
        print()
        print()

dns_latency("8.8.8.8", "1.1.1.1", "1.1.1.2", "9.9.9.9")
