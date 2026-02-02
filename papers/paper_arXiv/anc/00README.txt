Ancillary Files for "Unified Closed-Form Hypergeometric Representations of SU(2) 3n-j Symbols"
=====================================================================================

This directory contains validation data and scripts supporting the results in the manuscript.

Contents:
---------

1. Reference Validation Data (JSON files):
   - higher_n_reference_9j.json       : Pre-computed 9j reference values for validation
   - higher_n_reference_12j.json      : Pre-computed 12j reference values for validation
   - integration_validation_report.json : Comprehensive validation report from integration tests

2. Validation Scripts (Python):
   - run_integration_tests.py         : Integration test suite validating theorems against multiple backends
   - generate_validation_tables.py    : Script to generate validation tables shown in manuscript

Requirements:
-------------
The validation scripts require Python 3.8+ with the following dependencies:
  - numpy
  - sympy >= 1.12
  - mpmath
  - pytest (for run_integration_tests.py)

Additionally, the full validation suite uses the following open-source packages:
  - su2-3nj-generating-functional (https://github.com/dawsoninstitute/su2-3nj-generating-functional)
  - su2-3nj-recurrences (https://github.com/dawsoninstitute/su2-3nj-recurrences)
  - su2-3nj-closedform (https://github.com/dawsoninstitute/su2-3nj-closedform)

See Appendix C of the manuscript for complete repository information.

Usage:
------
To reproduce validation results:

1. Install dependencies (example using pip):
   pip install numpy sympy mpmath pytest

2. Run integration tests:
   python run_integration_tests.py

3. Generate validation tables:
   python generate_validation_tables.py

The JSON files can be loaded with standard JSON parsers for independent verification.

Contact:
--------
For questions about validation data or scripts, please contact the corresponding author
or open an issue at: https://github.com/dawsoninstitute/su2-3nj-series-paper
