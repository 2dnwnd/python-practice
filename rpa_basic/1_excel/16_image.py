from openpyxl import Workbook
from openpyxl.drawing.image import Image
wb = Workbook()
ws = wb.active

img = Image('google_movie.png')

ws.add_image(img, 'C3')

wb.save('sample_image.xlsx')