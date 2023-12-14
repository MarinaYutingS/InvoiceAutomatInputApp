# # import tabula
# # import json

# # def extract_invoice_data(pdf_path, column_names):
# #     # Read the PDF and extract tables based on column names
# #     tables = tabula.read_pdf(pdf_path, pages='all')

# #     # Initialize a dictionary to store invoice data
# #     invoice_data = {}

# #     # Iterate through the tables
# #     for table in tables:
# #         # Extract data from the table based on column names
# #         for index, row in table.iterrows():
# #             itemId = row.get(column_names.get('ItemId'))
# #             qty = row.get(column_names.get('QTY'))
# #             boxCost = row.get(column_names.get('BOX COST'))
# #             hst = row.get(column_names.get('HST'))

# #             print (row)
            
# #             # Check if any required field is missing
# #             if itemId is not None and qty is not None and boxCost is not None:
# #                 itemId = int(itemId)
# #                 qty = int(qty)
# #                 boxCost = boxCost
# #                 hst = hst
            
# #             invoice_data[itemId] = {
# #                         'qty': qty,
# #                         'boxCost': boxCost,
# #                         'HST': hst
# #                     }


# #     return invoice_data

# # def save_to_json(invoice_data, json_path):
# #     # Write the invoice data to a JSON file
# #     with open(json_path, 'w') as json_file:
# #         json.dump(invoice_data, json_file, indent=2)

# #     print(f"Invoice data saved to '{json_path}'.")

# # if __name__ == "__main__":
# #     # Provide the path to your PDF file
# #     pdf_path = 'invoice_reading/invoices/sixFortune-w50.pdf'
    
# #     # Define column names in the PDF table
# #     column_names = {
# #         'ItemId': 'Customer No.',
# #         'QTY': 'Ord',
# #         'BOX COST': 'Unit Price',
# #         'HST':'Ext.'
# #     }

# #     # Provide the desired output JSON file path
# #     json_path = 'invoice_reading/invoices/output_sixFortune.json'

# #     # Extract data from the invoice PDF based on column names
# #     invoice_data = extract_invoice_data(pdf_path, column_names)

# #     # Save the invoice data to a JSON file
# #     save_to_json(invoice_data, json_path)

# import camelot
# import json
# import re

# def extract_invoice_data(pdf_path):
#     # Read the PDF and extract tables
#     tables = camelot.read_pdf(pdf_path, flavor='stream', pages='2',process_ocr=True)

#     # Initialize a dictionary to store invoice data
#     invoice_data = {}
#     # Initialize a variable to store the previous row
#     prev_row = None
    
#     # Get the itemId by calling the function
#     item_id_list = get_itemId(tables)


#     # for table in tables:
#     #     # print(table.df.iat[23,4])
#     #     for index, row in table.df.iterrows():
#     #         print(index)
#     #         print(row)
            
#             # if row[3]!="":
#             #     qty = row[1]
#             #     description = prev_row[4]
#             #     boxCost = prev_row[5]
#             # # Store information in the invoice_data dictionary
#             #     invoice_data[row[3]] = {
#             #             'qty': qty,
#             #             'description': description,
#             #             'boxCost': boxCost
#             #         }
#             # if row[3] == '37026':
#             #     print('y')
#             #     print(prev_row[4])
#             # if row[3] == '26030':
#             #     print('n')
#             #     print(prev_row[4])
#             # print()
            
#             # for n in range(len(item_id_list)):
#             #     if str(row[3]) == str(item_id_list[n]):
#             #         qty = row[1]
#             #         description = prev_row[4]
#             #         boxCost = prev_row[5]
#             #         # print(description)
#             #     # Store information in the invoice_data dictionary
#             #         invoice_data[item_id_list[n-1]] = {
#             #             'qty': qty,
#             #             'description': description,
#             #             'boxCost': boxCost
#             #         }
            
#             # prev_row = row
            
#             # print('pre'+prev_row[4]+prev_row[5])
#             # print
#     # return invoice_data

# def get_itemId(tables):
#     item_id_list = []

#     # Define the regex pattern for matching 5-digit ItemId
#     item_id_pattern = re.compile(r'\b\d{5}\b')

#     # Iterate through the tables
#     for table in tables:
#         # Extract data from the table
#         for row in table.df.iterrows():
#             # Find ItemId using the regex pattern
#             item_id_match = re.search(item_id_pattern, str(row))

#             if item_id_match:
#                 item_id = item_id_match.group(0)
#                 item_id_list.append(item_id)
#     return item_id_list

# def get_description(tables):
#     product_list = []
#     # Define the regex pattern for more than 10 characters
#     pattern = r'.{11,}'

# def save_to_json(invoice_data, json_path):
#     # Write the invoice data to a JSON file
#     with open(json_path, 'w') as json_file:
#         json.dump(invoice_data, json_file, indent=2)

#     print(f"Invoice data saved to '{json_path}'.")

# if __name__ == "__main__":
#     # Provide the path to your PDF file
#     pdf_path = 'invoice_reading/invoices/sixFortune-w50.pdf'

#     # Provide the desired output JSON file path
#     json_path = 'invoice_reading/invoices/output_sixFortune.json'
    
#     # Extract data from the invoice PDF based on ItemId pattern
#     invoice_data = extract_invoice_data(pdf_path)

#     # Save the invoice data to a JSON file
#     # save_to_json(invoice_data, json_path)

import camelot
import re
import json

def extract_invoice_data(pdf_path):
    # Read the PDF and extract tables using the 'stream' flavor
    tables = camelot.read_pdf(pdf_path, flavor='stream', pages='all')

    # Initialize a dictionary to store invoice data
    invoice_data = []

    # Define regex patterns for different pieces of information
    regex_patterns = {
        'item_id' : re.compile(r'\b\d{5}\b'),
        'product_name': re.compile(r'\b\w{4,}\b'),  # Adjust as needed
        'quantity': re.compile(r'\b\d+\b'),          # Adjust as needed
        'price': re.compile(r'\b\d+\.\d{2}\b'),      # Adjust as needed
        'tax': re.compile(r'\b\w{3}\b')               # Adjust as needed
    }

    # Iterate through the tables
    for table in tables:
        # Extract data from the table
        for index, row in table.df.iterrows():
            # Iterate through the row values
            extracted_info = {}
            for key, pattern in regex_patterns.items():
                # Apply regex pattern to find information
                for value in row.values:
                    match = re.search(pattern, str(value))
                    if match:
                        extracted_info[key] = match.group(0)
                        break  # Break the inner loop if a match is found

            # Append the extracted information to the invoice_data list
            invoice_data.append(extracted_info)

    return invoice_data


def save_to_json(invoice_data, json_path):
    # Write the invoice data to a JSON file
    with open(json_path, 'w') as json_file:
        json.dump(invoice_data, json_file, indent=2)

    print(f"Invoice data saved to '{json_path}'.")


if __name__ == "__main__":
    # Provide the path to your PDF file
    pdf_path = 'invoice_reading/invoices/sixFortune-w50.pdf'

    # Provide the desired output JSON file path
    json_path = 'invoice_reading/invoices/output_sixFortune.json'
    
    # Extract data from the invoice PDF based on ItemId pattern
    invoice_data = extract_invoice_data(pdf_path)

    # Save the invoice data to a JSON file
    save_to_json(invoice_data, json_path)