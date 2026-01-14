# 🚀 NYXRecon

**NYXRecon** is a lightweight, automated reconnaissance engine built for **bug bounty hunters** and **security researchers**.  
It streamlines URL collection, historical endpoint discovery, and parameter extraction using industry‑standard tools.

> ⚡ Designed for speed, clarity, and real‑world recon workflows.

---

## ✨ Features

- 🔍 Collects historical URLs using:
  - `waybackurls`
  - `gau`
- 🧹 Automatically filters **parameterized URLs**
- 📂 Clean, organized output per target
- 🧠 Dependency checks before execution
- 🖥️ Professional CLI interface
- 🎯 Built for **educational & authorized testing**

---

## 📸 Demo

```bash
python3 cli.py --recon -d example.com
```
📁 Output Structure

nyxrecon/
└── recon/
    └── example.com/
        ├── waybackurls.txt
        ├── gau.txt
        └── urls_parameters.txt

🛠 Requirements

Make sure the following tools are installed and accessible in $PATH:
     .waybackurls
     .gau
     .Python 3.8+


Install tools

go install github.com/tomnomnom/waybackurls@latest
go install github.com/lc/gau/v2/cmd/gau@latest

📦 Installation

git clone https://github.com/NyxC0d3r/autombug.git
cd autombug/nyxrecon
chmod +x cli.py



🚀 Usage
Run full recon

python3 cli.py --recon -d example.com


Custom output directory

python3 cli.py --recon -d example.com -o output/recon


Show version

python3 cli.py --version




⚠️ Legal Disclaimer

NYXRecon is intended for educational purposes and authorized security testing only.
You are fully responsible for ensuring you have explicit permission before scanning any target.
The author is not responsible for misuse, damage, or legal consequences.


🧠 Roadmap

Subdomain enumeration (subfinder, assetfinder)

Technology fingerprinting

Vulnerability‑focused URL categorization

Output formats (JSON, CSV)

Modular plugin system


👨‍💻 Author

Sumit (NyxC0d3r)
Security Researcher | Bug Bounty Hunter



⭐ Support

If this project helps you:

⭐ Star the repository

🐛 Report issues

💡 Suggest features


Happy hunting! 🐞🔥

