Supplementary Material for JMP26-AR-00306  
- data/: High-precision JSON/CSV datasets for validation.  
- scripts/: Wolfram/Python code for verification, figures, and tests. Run verify_wolfram.wls --paper-strict for full checks.  
See main manuscript for details; all open-source at https://github.com/DawsonInstitute/su2-3nj-series-paper.

```bash
$ zipinfo -1 Supplementary_Material_JMP26-AR-00306.zip
data/recurrence_stability_report.csv
data/integration_validation_report.json
data/higher_n_reference_12j.json
data/uq_determinant_stability.csv
data/higher_n_reference_9j.json
scripts/generate_stability_figures.py
scripts/generate_higher_n_references.py
scripts/verify_wolfram.wls
scripts/verify_python.py
scripts/prepare_arxiv_bundle.sh
scripts/run_integration_tests.py
```