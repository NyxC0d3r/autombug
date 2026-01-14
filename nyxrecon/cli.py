#!/usr/bin/env python3
import os
import subprocess

BANNER = """
==============================================
 🚀 NYXRecon – Automated Recon Engine
 Author: Sumit (NYX)
==============================================
"""

def recon_module():
    domain = input("\nEnter Target Domain (example: example.com) >> ").strip()

    if not domain:
        print("❌ Domain cannot be empty.")
        return

    output_dir = os.path.join("nyxrecon", "recon", domain)
    os.makedirs(output_dir, exist_ok=True)

    print("\n🔍 Running waybackurls...")
    try:
        with open(f"{output_dir}/waybackurls.txt", "w") as wb:
            subprocess.run(["waybackurls", domain], stdout=wb)
    except FileNotFoundError:
        print("❌ waybackurls not installed")

    print("🔍 Running gau...")
    try:
        with open(f"{output_dir}/gau.txt", "w") as g:
            subprocess.run(["gau", domain], stdout=g)
    except FileNotFoundError:
        print("❌ gau not installed")

    print("🔍 Filtering parameterized URLs...")
    try:
        with open(f"{output_dir}/gau.txt") as f:
            urls = set(f.readlines())

        params = [u for u in urls if "=" in u]
        if params:
            with open(f"{output_dir}/urls_parameters.txt", "w") as p:
                p.writelines(params)
            print(f"✔ Saved {len(params)} parameterized URLs")
        else:
            print("→ No parameters found")

    except Exception as e:
        print(f"[!] Error: {e}")

    print(f"\n📂 Output saved in: {output_dir}\n")

def main():
    while True:
        print(BANNER)
        print("[1] Recon Module")
        print("[2] Brute-force (Labs only – Coming soon)")
        print("[3] About")
        print("[0] Exit")

        choice = input("Choose option >> ").strip()

        if choice == "1":
            recon_module()
        elif choice == "2":
            print("\n⚠️ Labs only. Feature coming soon.\n")
        elif choice == "3":
            print("\nNYXRecon – Educational recon automation tool\n")
        elif choice == "0":
            print("\n👋 Exiting...\n")
            break
        else:
            print("\n❌ Invalid choice\n")

if __name__ == "__main__":
    main()
