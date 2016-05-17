import xlrd

def print_xls(path):
    data=xlrd.open_workbook(path)
    table = data.sheets()[1]
    nrows = table.nrows
    books = []
    for i in range(nrows):
        ss=table.row_values(i)
    for i in range(len(ss)):
        print(ss[i])
        print('++++++++++++++++++++++++++++++')
if __name__ == '__main__':
        print_xls('/tmp/123.xls')
