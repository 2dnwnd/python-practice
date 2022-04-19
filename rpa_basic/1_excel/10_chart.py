from openpyxl import load_workbook
wb = load_workbook('sample.xlsx')
ws = wb.active

from openpyxl.chart import BarChart, Reference
bar_value = Reference(ws,min_row=1, max_row=11, min_col=2, max_col=3)
bar_chart = BarChart() # 차트 종류 설정
bar_chart.add_data(bar_value, titles_from_data=True) # 차트 데이터 추가
bar_chart.title = '성적표' #제목
bar_chart.style = 20 # 차트 스타일
bar_chart.y_axis.title = '점수' #Y축의 제목
bar_chart.x_axis.title = '번호' #Y축의 제목


ws.add_chart(bar_chart, 'E1') # 차트넣을 위치 정의

wb.save('sample_chart.xlsx')