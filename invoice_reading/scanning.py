import PyPDF2
import csv
import tabula
import json

def extract_pdf_information(pdf_path, csv_path):
    # Open the PDF file
    with open(pdf_path, 'rb') as pdf_file:
        # Create a PDF reader object
        pdf_reader = PyPDF2.PdfReader(pdf_file)

        # Get the number of pages in the PDF
        num_pages = len(pdf_reader.pages)

        # Initialize a CSV writer
        with open(csv_path, 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)

            # Write header to CSV file
            csv_writer.writerow(['Page Number', 'Text'])

            # Iterate through all pages in the PDF
            for page_number in range(num_pages):
                # Extract text from the current page
                page = pdf_reader.pages[page_number]
                text = page.extract_text()

                # Write page number and text to CSV file
                csv_writer.writerow([page_number + 1, text])

    print(f"Information extracted from '{pdf_path}' and saved to '{csv_path}'.")

if __name__ == "__main__":
    # Provide the path to your PDF file
    pdf_path = 'invoice_reading/invoices/W48.pdf'

    # Provide the desired output CSV file path
    csv_path = 'invoice_reading/invoices/output.csv'

    # Call the function to extract information and save to CSV
    extract_pdf_information(pdf_path, csv_path)
