#
# board = [
#     ['', '', ''],
#     ['', '', ''],
#     ['', '', '']]
#
# win = False
#
# while win is not True:
#     x = input('введите координаты через пробел:')
#     print(x[0], x[2])
#     try:
#         board[int(x[0])][int(x[2])] = 'x'
#     except Exception:
#         print('Некорректный ввод координат')
#     print(board)
#     print(x[0], x[2])
# print(board)
import numpy as np

document = f'C:/Users/Vinkle/Downloads/book1.xlsx'


import pandas as pd

df = pd.read_excel(document)

# print(df.to_string())
ndf = pd.DataFrame(columns=["idx", "a", "n", "d", "b"])

n = ''
a = ''
d = ''
b = ''
res = []
idx = -1
for row in df.iterrows():
    # print('row=', row)
    if isinstance(row[1]["number"], str):
        idx += 1
        ndf.loc[len(ndf.index)] = [f'{idx}.', a, n, d, b]
        n = str(row[1]["Название публикации"])
        a = f'Мирошниченко Е.С. (100%), {row[1]["Авторы"].replace("Мирошниченко Е.С.", "").replace(",", "")}'
        d = f"// {row[1]['Выходные данные']}"
        b = f"Баллы 1х1х1=1"
    else:
        if not isinstance(row[1]["Название публикации"], float):
            n += f' {str(row[1]["Название публикации"])}'
        # if not isinstance(row[1]["Авторы"], float):
        #     a += f' {row[1]["Авторы"]}'
        if not isinstance(row[1]["Выходные данные"], float):
            d += f' {row[1]["Выходные данные"]}'
    # print('[1]=', row[1]["number"])
    # print(type(row[1]["number"]))


x = ndf.to_string(header=False,
                  index=False,
                  index_names=False).split('\n')
vals = '\n'.join([' '.join(ele.split()) for ele in x])
print(vals)


