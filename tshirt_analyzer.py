"""
Module for analyzing t-shirt sales data.
No external dependencies required.
"""
from collections import defaultdict

def analyze_tshirts(data):
    """
    Analyze t-shirt sales data with t-shirt specific metrics.
    
    Args:
        data (list): List of dictionaries containing t-shirt sales data
        
    Returns:
        dict: Analysis results containing various metrics
    """
    # Initialize tracking dictionaries
    size_sales = defaultdict(float)
    color_sales = defaultdict(float)
    design_sales = defaultdict(float)
    size_quantity = defaultdict(int)
    color_quantity = defaultdict(int)
    
    total_revenue = 0
    total_quantity = 0
    
    # Process each row
    for row in data:
        try:
            # Convert amount and quantity, handling empty values
            amount = float(row.get('amount', 0)) if row.get('amount') else 0
            quantity = int(row.get('quantity', 1)) if row.get('quantity') else 1
            
            # Get t-shirt attributes
            size = row.get('size', 'Unknown').upper()
            color = row.get('color', 'Unknown').title()
            design = row.get('design', 'Unknown')
            
            # Update totals
            total_revenue += amount
            total_quantity += quantity
            
            # Update size metrics
            size_sales[size] += amount
            size_quantity[size] += quantity
            
            # Update color metrics
            color_sales[color] += amount
            color_quantity[color] += quantity
            
            # Update design metrics
            design_sales[design] += amount
            
        except (ValueError, KeyError) as e:
            print(f"Warning: Skipping invalid row: {row} - Error: {e}")
            continue

    # Sort results
    sorted_sizes = sorted(size_sales.items(), key=lambda x: x[1], reverse=True)
    sorted_colors = sorted(color_sales.items(), key=lambda x: x[1], reverse=True)
    sorted_designs = sorted(design_sales.items(), key=lambda x: x[1], reverse=True)
    
    # Calculate average price per unit
    avg_price = total_revenue / total_quantity if total_quantity > 0 else 0
    
    return {
        'total_revenue': total_revenue,
        'total_quantity': total_quantity,
        'avg_price': avg_price,
        'sorted_sizes': sorted_sizes,
        'sorted_colors': sorted_colors,
        'sorted_designs': sorted_designs,
        'size_quantity': dict(size_quantity),
        'color_quantity': dict(color_quantity)
    }

def generate_insights(analysis_results):
    """
    Generate t-shirt specific business insights.
    
    Args:
        analysis_results (dict): Results from analyze_tshirts function
        
    Returns:
        dict: Dictionary containing business insights
    """
    insights = {}
    
    # Most popular size by revenue and quantity
    if analysis_results['sorted_sizes']:
        top_size_revenue = analysis_results['sorted_sizes'][0]
        insights['top_size_revenue'] = top_size_revenue
        
        # Find most popular size by quantity
        size_qty = analysis_results['size_quantity']
        top_size_qty = max(size_qty.items(), key=lambda x: x[1])
        insights['top_size_quantity'] = top_size_qty
    
    # Most popular color
    if analysis_results['sorted_colors']:
        top_color = analysis_results['sorted_colors'][0]
        insights['top_color'] = top_color
    
    # Best performing design
    if analysis_results['sorted_designs']:
        top_design = analysis_results['sorted_designs'][0]
        insights['top_design'] = top_design
    
    # Size distribution analysis
    total_revenue = analysis_results['total_revenue']
    if total_revenue > 0:
        size_percentages = []
        for size, revenue in analysis_results['sorted_sizes']:
            percentage = (revenue / total_revenue) * 100
            size_percentages.append((size, percentage))
        insights['size_distribution'] = size_percentages
    
    return insights