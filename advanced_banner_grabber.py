#!/bin/python3

import subprocess



ip = "localhost"

print(f"[*] Starting banner grabbing for: {ip}...\n")
try:
	open_ports = subprocess.getoutput(f"nmap -sT {ip} -p- 2> /dev/null | grep open | cut -d\"/\" -f1").split("\n")
	print("[*] Open ports:", (open_ports if len(open_ports)>=1 else "0"))
	print("\n")
	if len(open_ports) > 1:
		for p in open_ports:
			subprocess.run(f"sudo ./banner.py {ip} {p}", shell=True)
	elif len(open_ports) == 1:
		subprocess.run(f"sudo ./banner.py {ip} {open_ports[0]}", shell=True)
	else:
		print(f"[-] No open port(s) for '{ip}' to banner grab!.")
except KeyboardInterrupt:
	print("Exiting...")
	quit()

