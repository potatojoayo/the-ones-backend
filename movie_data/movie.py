import xlrd

movie = xlrd.open_workbook('movie.xls')
sh = movie.sheet_by_index(0)
sh2 = movie.sheet_by_index(1)
m = []
def extract(s):
    for i in range(5,100):
        c = s.cell_value(rowx=i, colx=6)
        y = s.cell_value(rowx=i, colx=2)
        d = list(map(str, str(s.cell_value(rowx=i, colx=7)).split(',')))
        if (c=='개봉' or c == '개봉예정' or c == '촬영진행') and d[0] != '' and y != '':
            a = {'title': s.cell_value(rowx=i, colx=0),
                 'title_en': s.cell_value(rowx=i, colx=1),
                 'year': y,
                 'directors': d 
                }
            m.append(a)

extract(sh)

for i in range(0,20):
    print(m[i])



