"""
Module for generating t-shirt sales reports.
No external dependencies required.
"""

def write_report(analysis_results, insights, output_file):
    """
    Write t-shirt analysis report to file.
    
    Args:
        analysis_results (dict): Results from t-shirt analysis
        insights (dict): Dictionary containing business insights
        output_file (str): Path to the output report file
    """
    try:
        with open(output_file, 'w', encoding='utf-8') as file:
            # Write header
            file.write("T-Shirt Sales Analysis Report\n")
            file.write("============================\n\n")
            
            # Write summary
            file.write(f"Total Revenue: ${analysis_results['total_revenue']:.2f}\n")
            file.write(f"Total T-Shirts Sold: {analysis_results['total_quantity']}\n")
            file.write(f"Average Price per T-Shirt: ${analysis_results['avg_price']:.2f}\n\n")
            
            # Write size analysis
            file.write("T-Shirt Sizes by Revenue\n")
            file.write("----------------------\n")
            for i, (size, revenue) in enumerate(analysis_results['sorted_sizes'], 1):
                percentage = (revenue / analysis_results['total_revenue']) * 100
                quantity = analysis_results['size_quantity'].get(size, 0)
                file.write(f"{i}. Size {size}: ${revenue:.2f} ({percentage:.1f}%) - {quantity} units\n")
            
            file.write("\n")
            
            # Write color analysis
            file.write("T-Shirt Colors by Revenue\n")
            file.write("-----------------------\n")
            for i, (color, revenue) in enumerate(analysis_results['sorted_colors'], 1):
                percentage = (revenue / analysis_results['total_revenue']) * 100
                quantity = analysis_results['color_quantity'].get(color, 0)
                file.write(f"{i}. {color}: ${revenue:.2f} ({percentage:.1f}%) - {quantity} units\n")
            
            file.write("\n")
            
            # Write design analysis
            file.write("T-Shirt Designs by Revenue\n")
            file.write("------------------------\n")
            for i, (design, revenue) in enumerate(analysis_results['sorted_designs'], 1):
                percentage = (revenue / analysis_results['total_revenue']) * 100
                file.write(f"{i}. {design}: ${revenue:.2f} ({percentage:.1f}%)\n")
            
            file.write("\n")
            
            # Write insights
            file.write("Key Insights\n")
            file.write("-----------\n")
            
            if 'top_size_revenue' in insights:
                size, revenue = insights['top_size_revenue']
                file.write(f"Best selling size by revenue: {size} (${revenue:.2f})\n")
            
            if 'top_size_quantity' in insights:
                size, quantity = insights['top_size_quantity']
                file.write(f"Most popular size by quantity: {size} ({quantity} units)\n")
            
            if 'top_color' in insights:
                color, revenue = insights['top_color']
                file.write(f"Best selling color: {color} (${revenue:.2f})\n")
            
            if 'top_design' in insights:
                design, revenue = insights['top_design']
                file.write(f"Top performing design: {design} (${revenue:.2f})\n")
            
            file.write("\n")
            
            # Write recommendations
            file.write("Recommendations\n")
            file.write("--------------\n")
            file.write("1. Stock more inventory of top-selling sizes and colors\n")
            file.write("2. Consider promoting less popular designs with successful colors/sizes\n")
            file.write("3. Analyze seasonal trends for color preferences\n")
            file.write("4. Bundle slow-moving designs with popular ones\n")
            file.write("5. Focus marketing on best-performing size/color combinations\n")

    except Exception as e:
        print(f"Error writing report: {str(e)}")

def print_summary(analysis_results, count=3):
    """
    Print a summary of top t-shirt metrics to the console.
    
    Args:
        analysis_results (dict): Results from t-shirt analysis
        count (int): Number of top items to display
    """
    print(f"\nT-Shirt Sales Summary:")
    print(f"Total Revenue: ${analysis_results['total_revenue']:.2f}")
    print(f"Total Units Sold: {analysis_results['total_quantity']}")
    print(f"Average Price: ${analysis_results['avg_price']:.2f}")
    
    print(f"\nTop {count} Sizes by Revenue:")
    for i, (size, revenue) in enumerate(analysis_results['sorted_sizes'][:count], 1):
        percentage = (revenue / analysis_results['total_revenue']) * 100
        print(f"{i}. Size {size}: ${revenue:.2f} ({percentage:.1f}%)")
    
    print(f"\nTop {count} Colors by Revenue:")
    for i, (color, revenue) in enumerate(analysis_results['sorted_colors'][:count], 1):
        percentage = (revenue / analysis_results['total_revenue']) * 100
        print(f"{i}. {color}: ${revenue:.2f} ({percentage:.1f}%)")