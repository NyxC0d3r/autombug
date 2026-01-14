#!/usr/bin/env python3
import os
import subprocess
import argparse
import sys
import shutil

VERSION = "1.0.0"

def banner():
    print(f"NYXRecon v{VERSION}")
    print("Automated Recon Engine")
    print("by NyxC0d3r\n")

def check_tool(tool):
    if not shutil.which(tool):
        print(f"❌ Required tool not found: {tool}")
        return False
    return True

def run_recon(domain, output_base):
    # Check required tools first
    required_tools = ["waybackurls", "gau"]
    for tool in required_tools:
        if not check_tool(tool):
            print("\n[!] Install missing tools and try again.")
            sys.exit(1)

    output_dir = os.path.join(output_base, domain)
    os.makedirs(output_dir, exist_ok=True)

    print(f"[+] Target : {domain}")
    print(f"[+] Output : {output_dir}\n")

    # waybackurls
    print("[*] Running waybackurls...")
    with open(f"{output_dir}/waybackurls.txt", "w") as wb:
        subprocess.run(
            ["waybackurls", domain],
            stdout=wb,
            stderr=subprocess.DEVNULL
        )

    # gau
    print("[*] Running gau...")
    with open(f"{output_dir}/gau.txt", "w") as g:
        subprocess.run(
            ["gau", domain],
            stdout=g,
            stderr=subprocess.DEVNULL
        )

    # Filter parameterized URLs
    print("[*] Filtering parameterized URLs...")
    try:
        with open(f"{output_dir}/gau.txt", "r") as f:
            urls = set(f.readlines())

        params = [u for u in urls if "=" in u]

        if params:
            with open(f"{output_dir}/urls_parameters.txt", "w") as p:
                p.writelines(params)
            print(f"[+] Saved {len(params)} parameterized URLs")
        else:
            print("[!] No parameterized URLs found")

    except Exception as e:
        print(f"[!] Error processing URLs: {e}")

    print("\n[✓] Recon completed successfully")

def main():
    parser = argparse.ArgumentParser(
        description="NYXRecon – Automated Recon Engine"
    )

    parser.add_argument(
        "-d", "--domain",
        help="Target domain (example.com)"
    )

    parser.add_argument(
        "--recon",
        action="store_true",
        help="Run full recon (wayback + gau + param filter)"
    )

    parser.add_argument(
        "-o", "--output",
        default="nyxrecon/recon",
        help="Output directory (default: nyxrecon/recon)"
    )

    parser.add_argument(
        "-v", "--version",
        action="store_true",
        help="Show version and exit"
    )

    args = parser.parse_args()
    banner()

    if args.version:
        sys.exit(0)

    if not args.domain:
        print("❌ Error: Target domain is required")
        print("👉 Example: python3 cli.py --recon -d example.com")
        sys.exit(1)

    if not args.recon:
        print("❌ Error: No action specified")
        print("👉 Use --recon to start recon")
        sys.exit(1)

    run_recon(args.domain, args.output)

if __name__ == "__main__":
    main()
