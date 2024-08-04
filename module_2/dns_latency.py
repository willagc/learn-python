#!/usr/bin/env python3
import subprocess
# simple function ping three dns servers. Then calculate latency, finally prints latency.

def dns_latency(dns1,dns2,dns3):
    proc1 = subprocess.check_output(f"ping -c10 {dns1}", shell='true', capture_output=True)
    proc2 = subprocess.check_output(f"ping -c10 {dns2}", shell='true', capture_output=True)
    proc3 = subprocess.check_output(f"ping -c10 {dns3}", shell='true', capture_output=True)
        
dns_latency("8.8.8.8", "1.1.1.1", "1.1.1.2")
