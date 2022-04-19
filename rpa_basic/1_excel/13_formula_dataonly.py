from openpyxl import load_workbook
wb = load_workbook('sample_formula.xlsx', data_only=True)
ws = wb.active

# 수식 그대로 가져오기
for row in ws.values:
    for cell in row:
        print(cell)