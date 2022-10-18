import pandas as pd
import numpy as np
import statistics as st

'''импортируем библиотеки и определяем переменные.
в качестве переменных мы обозначаем файл с сырыми спектральными данными(input_filename)
и файл в котором будут уже обработанные спектральные данные. так же в качестве переменных указаны
начальные и конечные частоты и частота лазера'''

f1 = 'input_filename'
f2 = 'output_filename'
v1 = 19346
v2 = 19506
vl = 20483

'''определяем функцию для расчета из имеющихся данных'''


def calc():
    data = []
    with open(f1, 'r') as file:
        for line in file:
            data.append([float(x) for x in line.split()])
    df = pd.DataFrame(data, columns=['x', 'y'])
    r = df[:-1]
    dv = (v2 - v1) / (len(r) - 1)  # расчитываем шаг с которым будет изменяться частота от начальной до конечной
    result = []
    for i in np.arange(v1, v2 + dv, dv):  # с шагом dv мы увеличиваем частоту и записываем полученное в список result
        v = vl - i
        result.append(v)
    intens = []
    for j in df['y']:  # определяю цикл для интенсивности и увеличиваем ее в сто раз для лучшей видимости
        ints = j * 100
        intens.append(ints)
    if len(result) != len(intens):  # выравниваем длинну списка
        if len(result) > len(intens):
            mean_intens = st.mean(intens)
            intens += (len(result) - len(intens)) * [mean_intens]
        elif len(result) < len(intens):
            mean_result = st.mean(result)
            result += (len(intens) - len(result)) * [mean_result]
    '''записываем результат в ДатаФрейм и получаем зависимость интенсивность от волнового числа
    и записываем все в выходной файл output_file'''
    rdf = pd.DataFrame({
        'v': result,
        'y': intens
    })
    rdf.to_csv(f2, index=False, sep=' ')


def main():
    calc()


if __name__ == '__main__':
    main()
