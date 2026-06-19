import pandas as pd

try:
    # This reads the Excel file directly, so you don't have to convert it to CSV first!
    df = pd.read_excel('schedule.xlsx')
    
    # Convert it to HTML
    html_table = df.to_html(index=False)
    
    # Save the output to table.html
    with open("table.html", "w") as f:
        f.write(html_table)
    print("Successfully generated table.html from schedule.xlsx!")
except Exception as e:
    print(f"Error: {e}")
