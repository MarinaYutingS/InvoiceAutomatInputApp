import tabula
import json

def extract_invoice_data(pdf_path, column_names):
    # Read the PDF and extract tables based on column names
    tables = tabula.read_pdf(pdf_path, pages='all')

    # Initialize a dictionary to store invoice data
    invoice_data = {}

    # Iterate through the tables
    for table in tables:
        # Extract data from the table based on column names
        for index, row in table.iterrows():
            product_code = row.get(column_names.get('product_code'))
            quantity = row.get(column_names.get('quantity'))
            price = row.get(column_names.get('price'))

            # Check if any required field is missing
            if product_code is not None and quantity is not None and price is not None:
                product_code = int(product_code)
                quantity = int(quantity)
                price = price
            
            invoice_data[product_code] = {
                        'quantity': quantity,
                        'price': price
                    }


    return invoice_data

def save_to_json(invoice_data, json_path):
    # Write the invoice data to a JSON file
    with open(json_path, 'w') as json_file:
        json.dump(invoice_data, json_file, indent=2)

    print(f"Invoice data saved to '{json_path}'.")

if __name__ == "__main__":
    # Provide the path to your PDF file
    pdf_path = 'invoice_reading/invoices/ttcc.pdf'
    
    # Define column names in the PDF table
    column_names = {
        'product_code': 'Item #',
        'quantity': 'Qty',
        'price': 'Price'
    }

    # Provide the desired output JSON file path
    json_path = 'invoice_reading/invoices/output_invoice.json'

    # Extract data from the invoice PDF based on column names
    invoice_data = extract_invoice_data(pdf_path, column_names)

    # Save the invoice data to a JSON file
    save_to_json(invoice_data, json_path)


# def extract_pdf_information(pdf_path, csv_path):
#     # Open the PDF file
#     with open(pdf_path, 'rb') as pdf_file:
#         # Create a PDF reader object
#         pdf_reader = PyPDF2.PdfReader(pdf_file)

#         # Get the number of pages in the PDF
#         num_pages = len(pdf_reader.pages)

#         # Initialize a CSV writer
#         with open(csv_path, 'w', newline='') as csv_file:
#             csv_writer = csv.writer(csv_file)

#             # Write header to CSV file
#             csv_writer.writerow(['Page Number', 'Text'])

#             # Iterate through all pages in the PDF
#             for page_number in range(num_pages):
#                 # Extract text from the current page
#                 page = pdf_reader.pages[page_number]
#                 text = page.extract_text()

#                 # Write page number and text to CSV file
#                 csv_writer.writerow([page_number + 1, text])

#     print(f"Information extracted from '{pdf_path}' and saved to '{csv_path}'.")

# if __name__ == "__main__":
#     # Provide the path to your PDF file
#     pdf_path = 'invoice_reading/invoices/W48.pdf'

#     # Provide the desired output CSV file path
#     csv_path = 'invoice_reading/invoices/output.csv'

#     # Call the function to extract information and save to CSV
#     extract_pdf_information(pdf_path, csv_path)
