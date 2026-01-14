# NYXRecon – Usage Guide

## Run the Tool

```bash
python nyxrecon/cli.py


Menu Options
Option	Description
1	Recon module (waybackurls + gau)
2	Brute-force (labs only – coming soon)
3	About the tool
0	Exit


Recon Module Workflow

1. Choose option 1

2. Enter target domain (example: example.com)

3. Tool collects URLs using:

   .waybackurls

   .gau

4. Parameterized URLs are filtered automatically


Output Location

nyxrecon/recon/<domain>/

Files Created

  .waybackurls.txt

   .gau.txt

  .urls_parameters.txt


Requirements

The following tools must be installed and available in $PATH:

    .waybackurls

    .gau

Notes

.Use authorized targets only

.Do not upload scan results to public repositories


---

## 2.9 Save & Exit

- `CTRL + O` → Enter  
- `CTRL + X`

---

## 2.10 Verify formatting (optional but good)

```bash
cat USAGE.md
