"""
Main module for t-shirt sales analysis application.
No external dependencies required.
"""
import sys
import os
from tshirt_data_reader import read_data
from tshirt_analyzer import analyze_tshirts, generate_insights
from tshirt_report_writer import write_report, print_summary

def main():
    """Main function to run the t-shirt sales analysis."""
    # Check command line arguments
    if len(sys.argv) != 3:
        print("Usage: python tshirt_main.py <input_file> <output_file>")
        print("Example: python tshirt_main.py tshirt_sales.csv tshirt_report.txt")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Verify input file exists
    if not os.path.exists(input_file):
        print(f"Error: Input file '{input_file}' not found.")
        sys.exit(1)

    # Read and process data
    print(f"Reading t-shirt sales data from {input_file}...")
    data = read_data(input_file)
    
    if not data:
        print("No data found in input file.")
        sys.exit(1)

    print(f"\nTotal t-shirt sales records: {len(data)}")
    
    # Analyze t-shirts
    print("\nAnalyzing t-shirt performance...")
    analysis_results = analyze_tshirts(data)
    
    # Generate business insights
    insights = generate_insights(analysis_results)
    
    # Write report
    print(f"\nWriting t-shirt report to {output_file}...")
    write_report(analysis_results, insights, output_file)
    
    # Print summary to console
    print_summary(analysis_results)
    
    print("\nT-shirt analysis complete!")
    print(f"Report generated: {output_file}")

if __name__ == "__main__":
    main()