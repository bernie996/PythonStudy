import openpyxl
workbok = openpyxl.load_workbook(filename="sample.xlsx")
sheet_prac = workbok.active
dictionary = {}
element = 1
for n in sheet_prac.iter_rows(min_row = 2, min_col = 4, max_col = 7, values_only = True):
    product_id = n[0]
    product = { "Parent": n[1], "Title": n[2], "Category": n[3] }
    dictionary.update({ product_id : product })
for key,value in dictionary.items():
    print("Element {0}: {1} = {2} \n".format(element, key, value))
    element += 1