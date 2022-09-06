import openpyxl
#carregando planilha ja criada
book = openpyxl.load_workbook('PlanilhasDeOrçamentos.xlsx')
#selecinando pagina especifica para abrir
Orcamento_page = book['Orçamento']
#imprimindo os dados de cada linha
for rows in Orcamento_page.iter_rows(min_row=2,max_row=5):
    #print com formatação f
    #print(f'{rows[0].value},{rows[1].value},{rows[2].value}')
    for cell in rows:
       #print(cell.value)
       if cell.value == 'Moto e5':
          cell.value = 'Moto e8'

book.save('PlanilhasDeOrçamentos.xlsx')

        
