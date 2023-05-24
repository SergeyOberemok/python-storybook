
class TableHtml:
    tableHtml = '<table style="width: 100%">{}</table>'
    rowHtml = '<tr>{}</tr>'
    rowHtmlDivider = '</tr><tr>'
    columnHtml = '<td style="text-align: left">{}</td>'
    columnHtmlDivider = '</td><td style="text-align: left">'
    
    rows = []
    
    def __init__(self):
        self.rows = []
    
    def addColumns(self, columns):
        joinedColumns = self.columnHtmlDivider.join(columns)
        columnsHtml = self.columnHtml.format(joinedColumns)
        self.rows.append(columnsHtml)
    
    def __str__(self):
        joinedRows = self.rowHtmlDivider.join(row for row in self.rows)
        rowsHtml = self.rowHtml.format(joinedRows)
        return self.tableHtml.format(rowsHtml)

def tableToHtml(table):
    tableHtml = TableHtml()
    
    for row in table:
        tableHtml.addColumns(str(column) for column in row)

    return str(tableHtml)

def dictionaryToHtml(dictionary, inverseVertically: bool = False):
    tableHtml = TableHtml()

    keys = list(dictionary.keys())

    if inverseVertically:
        keys.reverse()
        
    for key in keys:
        columns = [key] + dictionary[key]
        tableHtml.addColumns(str(column) for column in columns)
        
    return str(tableHtml)