import pandas as pd
import config

from datetime import datetime
from dateutil.relativedelta import relativedelta
from openpyxl import load_workbook
from openpyxl.styles import Font
from openpyxl.formatting.rule import FormulaRule

from seleccionar_ruta import seleccionar_ruta
from tratarHoras import tratarHoras
from tratar_certificaciones import tratar_certificaciones

def tratarHorasCompleto1():

  variable1=1;
  ascensores=tratarHorasCompleto()
  variable=2
  escaleras=tratarHorasEscaleras()


  
