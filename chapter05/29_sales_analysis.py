from functools import reduce
 
def main():
    months = [
        'January', 'February', 'March', 'April', 'May', 'June','July', 'August', 'September', 'October', 'November', 'December']
    sales = [12_000, 14_500, 13_200, 15_000, 20_000, 18_500,  16_000, 15_500, 14_000, 19_000, 22_500, 24_000]
   
    # Crete sales dict
    monthly_sales = dict(zip(months, sales))
    print(monthly_sales)
 
    # Filter moths with sales > 15_000
    high_sales_months = {month:value for month, value in monthly_sales.items() if value >= 15_000}
    print(high_sales_months)
 
    # Apply a discount 10% for all sales above 20_000
    discounted_sales = {
        month: value * 0.9 if value > 20_000 else value
        for month, value in monthly_sales.items()
    }
    print(discounted_sales)
 
    total_annual_sales = sum(discounted_sales.values())
    print(total_annual_sales)
 
    average_mohtly_sale = total_annual_sales / len(monthly_sales)
    print(average_mohtly_sale)
 
    best_month = max(discounted_sales, key=monthly_sales.get)
    worst_month = min(discounted_sales, key=monthly_sales.get)
 
 
 
if __name__ == "__main__":
    main()
