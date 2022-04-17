import pandas as pd
import pdfplumber

pdf = pdfplumber.open('2022.07.pdf')
pages = pdf.pages


