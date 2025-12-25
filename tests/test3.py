"""
US-GAAP Taxonomy Analysis Script (using helper functions)

This script processes the US-GAAP 2020 taxonomy files and creates a comprehensive
DataFrame with information about each concept including:
- Labels and documentation
- Statement classification (sfp, soi, scf, notes)
- Hierarchy path within each statement

This version uses the helper functions from leanrl.taxonomy.helper instead of
defining them locally.
"""

import sys
from pathlib import Path
# Add src to path if running from repo root
sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

from leanrl import build_taxonomy_dataframe


if __name__ == '__main__':
    """Main entry point."""
    import argparse
    
    parser = argparse.ArgumentParser(
        description='Analyze US-GAAP taxonomy and build concept DataFrame'
    )
    parser.add_argument(
        'taxonomy_path',
        help='Path to US-GAAP taxonomy folder (e.g., ./us-gaap-2020-01-31)',
        default="",
    )
    parser.add_argument(
        '-o', '--output',
        default='us_gaap_taxonomy.csv',
        help='Output CSV filename (default: us_gaap_taxonomy.csv)'
    )
    try:
        args = parser.parse_args()
        base_path = str(Path(args.taxonomy_path))
        output_path = str(Path(args.output))

    except Exception as e:
        print(f"Error: {e}")
        print("No taxonomy path provided. Using default path...")
        
        base_path = "/tmp/us-gaap-2020-01-31/"
        output_path = '/tmp/us_gaap-2020-01-31-taxonomy.csv'

    # Use the helper function from taxonomy.helper
    df = build_taxonomy_dataframe(base_path, output_path)
    
    # Show some examples
    print("\n" + "=" * 60)
    print("Sample Records")
    print("=" * 60)
    
    # Show R&D expense
    rd = df[df['concept'] == 'us-gaap_ResearchAndDevelopmentExpense']
    if not rd.empty:
        print("\nResearchAndDevelopmentExpense:")
        row = rd.iloc[0]
        print(f"  Label: {row['label']}")
        print(f"  Type: {row['data_type']} | monetary={row['is_monetary']} | period={row['period_type']} | balance={row['balance']}")
        print(f"  Statements: {row['all_statements']}")
        print(f"  Path: {row['path'][:100]}..." if len(str(row['path'])) > 100 else f"  Path: {row['path']}")
    
    # Show Assets
    assets = df[df['concept'] == 'us-gaap_Assets']
    if not assets.empty:
        print("\nAssets:")
        row = assets.iloc[0]
        print(f"  Label: {row['label']}")
        print(f"  Type: {row['data_type']} | monetary={row['is_monetary']} | period={row['period_type']} | balance={row['balance']}")
        print(f"  Statements: {row['all_statements']}")
        print(f"  Path: {row['path'][:100]}..." if len(str(row['path'])) > 100 else f"  Path: {row['path']}")

