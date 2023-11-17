import pandas as pd
from sklearn.neighbors import KNeighborsClassifier

data_table = pd.read_csv('input_task_8.csv', delimiter=',', decimal='.', index_col='id')
data = pd.read_csv('input_task_8.csv').values

new_obj_coordinate = [(67, 95)]

X = data[:, 1:3]
Y = data[:, 3]

#ЕВКЛИДОВА МЕТРИКА
e_model = KNeighborsClassifier(n_neighbors=3, p=2)
e_model.fit(X, Y)

#расстояние до ближайшего соседа
e_distance_to_obj = e_model.kneighbors(new_obj_coordinate, n_neighbors=1)[0][0] 

e_obj_idx = e_model.kneighbors(new_obj_coordinate)[1][0]  
e_choose_class = e_model.predict(new_obj_coordinate)

print('ЕВКЛИДОВА МЕТРИКА')
print(f'Расстояние до ближайшего соседа: {round(float(e_distance_to_obj), 3)}')
print(f'Идентификаторы трех ближайших точек: {e_obj_idx[0] + 1}, {e_obj_idx[1] + 1}, {e_obj_idx[2] + 1}')
print(f'Предcказанный класс: {int(e_choose_class)}')

#МАНХЭТТЕНСКАЯ МЕТРИКА
m_model = KNeighborsClassifier(n_neighbors=3, p=1)
m_model.fit(X, Y)

#расстояние до ближайшего соседа
m_distance_to_obj = m_model.kneighbors(new_obj_coordinate, n_neighbors=1)[0][0]

m_obj_idx = m_model.kneighbors(new_obj_coordinate)[1][0]  
m_choose_class = m_model.predict(new_obj_coordinate)

print('\nМАНХЭТТЕНСКАЯ МЕТРИКА')
print(f'Расстояние до ближайшего соседа: {round(float(m_distance_to_obj), 3)}')
print(f'Идентификаторы трех ближайших точек: {m_obj_idx[0] + 1}, {m_obj_idx[1] + 1}, {m_obj_idx[2] + 1}')
print(f'Предcказанный класс: {int(m_choose_class)}')