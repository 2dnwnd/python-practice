from openpyxl import load_workbook
wb = load_workbook('sample.xlsx')
ws = wb.active

ws.delete_rows(8) # 8번째 줄에있는 7번학생 데이터 삭제

wb.save('sample_delete_row.xlsx')