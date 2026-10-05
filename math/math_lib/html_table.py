class TableHtml:
    table_html = '<table style="width: 100%">{}</table>'
    row_html = '<tr>{}</tr>'
    row_html_divider = '</tr><tr>'
    column_html = '<td style="text-align: left">{}</td>'
    column_html_divider = '</td><td style="text-align: left">'

    def __init__(self):
        self.rows = []

    def add_columns(self, columns):
        joined_columns = self.column_html_divider.join(columns)
        columns_html = self.column_html.format(joined_columns)
        self.rows.append(columns_html)

    def __str__(self):
        joined_rows = self.row_html_divider.join(row for row in self.rows)
        rows_html = self.row_html.format(joined_rows)
        return self.table_html.format(rows_html)

    @staticmethod
    def to_html(table):
        table_html = TableHtml()

        for row in table:
            table_html.add_columns(str(column) for column in row)

        return str(table_html)
