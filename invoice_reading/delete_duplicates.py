import pandas as pd

def remove_duplicates(input_file, output_file):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(input_file)

    # Identify and remove duplicates
    df_no_duplicates = df.drop_duplicates(['ProductId','ItemId'])

    # Write the DataFrame without duplicates to a new CSV file
    df_no_duplicates.to_csv(output_file, index=False)

    print(f"Duplicates removed. Result saved to {output_file}")

# Example usage:
input_csv_file = 'invoice_reading/DB_raw/02. Suppliers - IBEX.csv'  # Replace with the path to your input CSV file
output_csv_file = 'invoice_reading/DB_output/output-IBEX.csv'  # Replace with the desired output CSV file

remove_duplicates(input_csv_file, output_csv_file)

