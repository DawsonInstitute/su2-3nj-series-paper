#!/usr/bin/env python3
"""
Generate stability figures for paper from existing sweep data.

Generates:
1. Recurrence stability vs spin (forward/backward error comparison)
2. Determinant condition vs parameter sweep

Outputs to papers/paper/figures/ as PDF for LaTeX inclusion.
"""

import json
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

# Setup paths
SCRIPT_DIR = Path(__file__).parent
REPO_ROOT = SCRIPT_DIR.parent
PAPER_FIGS = REPO_ROOT / "papers" / "paper" / "figures"
PAPER_FIGS.mkdir(parents=True, exist_ok=True)

# Data sources from sibling repos
RECURRENCE_CSV = Path.home() / "Code" / "asciimath" / "su2-3nj-recurrences" / "data" / "recurrence_stability_report.csv"
DETERMINANT_CSV = Path.home() / "Code" / "asciimath" / "su2-3nj-generating-functional" / "data" / "uq_determinant_stability.csv"

def generate_recurrence_stability_figure():
    """Generate recurrence forward/backward stability comparison."""
    
    if not RECURRENCE_CSV.exists():
        print(f"Warning: {RECURRENCE_CSV} not found; skipping recurrence figure")
        return
    
    df = pd.read_csv(RECURRENCE_CSV)
    
    # Diagnostic output
    print(f"  Loaded {len(df)} configurations from recurrence data")
    print(f"  Labels: {df['label'].tolist()}")
    print(f"  Forward error range: [{df['max_forward_error'].min():.3e}, {df['max_forward_error'].max():.3e}]")
    print(f"  Backward error range: [{df['max_backward_error'].min():.3e}, {df['max_backward_error'].max():.3e}]")
    print(f"  Condition number range: [{df['mean_condition_number'].min():.2f}, {df['mean_condition_number'].max():.2f}]")
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))
    
    # Left: Forward vs backward error by configuration (bar chart)
    configs = df['label'].values
    x = np.arange(len(configs))
    width = 0.35
    
    # Use actual data columns with clear labeling
    forward_errors = df['max_forward_error'].values
    backward_errors = df['max_backward_error'].values
    
    bars1 = ax1.bar(x - width/2, forward_errors, width, label='Forward Recursion', alpha=0.8, color='#2E86AB')
    bars2 = ax1.bar(x + width/2, backward_errors, width, label='Backward Recursion', alpha=0.8, color='#A23B72')
    
    ax1.set_xlabel('Test Configuration', fontsize=10)
    ax1.set_ylabel('Maximum Relative Error', fontsize=10)
    ax1.set_title('Recurrence Stability: Forward vs Backward', fontsize=11, fontweight='bold')
    ax1.set_xticks(x)
    ax1.set_xticklabels(configs, rotation=45, ha='right', fontsize=9)
    ax1.legend(loc='upper left', fontsize=9)
    ax1.set_yscale('log')
    ax1.grid(True, alpha=0.3, which='both', linestyle=':', linewidth=0.5)
    ax1.set_ylim(bottom=0.01)  # Ensure we can see all values
    
    # Right: Condition number by configuration (line plot)
    cond_numbers = df['mean_condition_number'].values
    
    ax2.plot(x, cond_numbers, 'o-', color='#F18F01', linewidth=2.5, markersize=8, 
             label='Mean $\\kappa$', markerfacecolor='white', markeredgewidth=2)
    ax2.set_xlabel('Test Configuration', fontsize=10)
    ax2.set_ylabel('Mean Condition Number $\\kappa$', fontsize=10)
    ax2.set_title('Recurrence Condition Numbers', fontsize=11, fontweight='bold')
    ax2.set_xticks(x)
    ax2.set_xticklabels(configs, rotation=45, ha='right', fontsize=9)
    ax2.axhline(y=1e3, color='r', linestyle='--', alpha=0.6, linewidth=1.5, label='$\\kappa = 10^3$ threshold')
    ax2.legend(loc='upper left', fontsize=9)
    ax2.grid(True, alpha=0.3, linestyle=':', linewidth=0.5)
    ax2.set_ylim(bottom=0.5, top=max(10, cond_numbers.max() * 1.2))  # Ensure visibility
    
    plt.tight_layout()
    outfile = PAPER_FIGS / "recurrence_stability.pdf"
    plt.savefig(outfile, bbox_inches='tight', dpi=300)
    print(f"✓ Saved: {outfile}")
    plt.close()


def generate_determinant_stability_figure():
    """Generate determinant stability vs parameter sweep."""
    
    if not DETERMINANT_CSV.exists():
        print(f"Warning: {DETERMINANT_CSV} not found; skipping determinant figure")
        return
    
    df = pd.read_csv(DETERMINANT_CSV)
    
    # Diagnostic output
    print(f"  Loaded {len(df)} parameter points from determinant data")
    print(f"  Parameter range: [{df['x'].min():.2f}, {df['x'].max():.2f}]")
    print(f"  Determinant range: [{df['det_numeric'].min():.3f}, {df['det_numeric'].max():.3f}]")
    print(f"  Non-zero errors: {(df['abs_error'] > 0).sum()} / {len(df)}")
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))
    
    # Left: Determinant value vs parameter
    ax1.plot(df['x'], df['det_numeric'], '-', color='#2E86AB', linewidth=2.5, label='$\\det(I - K)$ (numeric)')
    ax1.set_xlabel('Parameter $x$', fontsize=10)
    ax1.set_ylabel('Determinant Value', fontsize=10)
    ax1.set_title('Generating Functional Determinant Sweep', fontsize=11, fontweight='bold')
    ax1.grid(True, alpha=0.3, linestyle=':', linewidth=0.5)
    ax1.legend(loc='best', fontsize=9)
    
    # Right: Absolute error (log scale) - only plot non-zero errors
    nonzero_mask = df['abs_error'] > 0
    if nonzero_mask.sum() > 0:
        nonzero_error = df['abs_error'][nonzero_mask]
        x_nonzero = df['x'][nonzero_mask]
        
        ax2.semilogy(x_nonzero, nonzero_error, 'o', color='#A23B72', markersize=5, alpha=0.7, label='Numeric error')
        ax2.axhline(y=1e-15, color='r', linestyle='--', alpha=0.6, linewidth=1.5, label='Machine $\\epsilon$ ($10^{-15}$)')
        ax2.set_ylim(bottom=1e-17, top=1e-14)
    else:
        ax2.text(0.5, 0.5, 'All errors exactly zero\n(symbolic == numeric)', 
                ha='center', va='center', transform=ax2.transAxes, fontsize=10)
    
    ax2.set_xlabel('Parameter $x$', fontsize=10)
    ax2.set_ylabel('Absolute Error (log scale)', fontsize=10)
    ax2.set_title('Numerical Precision Assessment', fontsize=11, fontweight='bold')
    ax2.grid(True, alpha=0.3, which='both', linestyle=':', linewidth=0.5)
    ax2.legend(loc='best', fontsize=9)
    
    plt.tight_layout()
    outfile = PAPER_FIGS / "determinant_stability.pdf"
    plt.savefig(outfile, bbox_inches='tight', dpi=300)
    print(f"✓ Saved: {outfile}")
    plt.close()


def main():
    print("=" * 60)
    print("Generating Stability Figures for Paper")
    print("=" * 60)
    print()
    
    generate_recurrence_stability_figure()
    generate_determinant_stability_figure()
    
    print()
    print("Figures saved to:", PAPER_FIGS)
    print("Include in LaTeX with:")
    print("  \\includegraphics[width=0.9\\textwidth]{figures/recurrence_stability.pdf}")
    print("  \\includegraphics[width=0.9\\textwidth]{figures/determinant_stability.pdf}")
    print()


if __name__ == "__main__":
    main()
