import numpy as np
import pandas as pd
import re

r1 = r'(?:здравствуйте)|(?:добрый день)|(?:добрый)'
r2 = r'(?:до свидания)|(?:хорошего вечера)'
r3 = r'(?:меня зовут)|(?:мое имя)|(?:диджитал бизнес)|(?:китобизнес)'
r4 = r'(ангелина)|(максим)|(анастасия)'


def main():
    """определяем файл для открытия и вносим данные в DataFrame"""
    dialog = pd.read_csv('test_data.csv')
    arr = np.array(dialog)
    df = pd.DataFrame(arr, columns=['dlg_id', 'line_n', 'role', 'text'])
    '''проходимся по всему DataFrame, затем перебираем строки где role = manager и забираем от туда приветствия, 
    представления и прощание '''
    manager = df.loc[df['role'] == 'manager']
    hi_list = []
    for line1 in manager['text']:
        if re.search(r1, line1):
            hi_list.append(line1)
            print(line1)
    bye_list = []
    for line2 in manager['text']:
        if re.search(r2, line2):
            bye_list.append(line2)
            print(line2)
    my_name_list = []
    for line3 in manager['text']:
        if re.search(r3, line3):
            my_name_list.append(line3)
            print(line3)
            if re.search(r4, line3):
                print('каждый менеджер назвал свое имя')
    if len(hi_list) == len(bye_list):
        print('все менеджеры поздоровались и попрощались')
    else:
        print('кто то ушел по-английски')
        bye_list.append('ах ты невежливый чурбан')

    rdf = pd.DataFrame({
        'приветствие': hi_list,
        'прощание': bye_list,
        'представились': my_name_list
    })
    rdf.to_csv('res_data.csv', index=False, sep=';')


if __name__ == '__main__':
    main()
