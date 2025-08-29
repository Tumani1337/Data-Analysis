import numpy as np

#1
temps = np.array([15.2, 16.8, 14.5, 17.0, 16.1])

sum_temps = np.sum(temps)
mean_temps = np.mean(temps)
min_temps = np.min(temps)
max_temps = np.max(temps)

print("Сумма:", sum_temps)
print("Среднее:", mean_temps)
print("Минимум:", min_temps)
print("Максимум:", max_temps)
#2
h1 = np.array([45, 50, 47])
h2 = np.array([48, 46, 52])

elementwise_sum = h1 + h2
elementwise_product = h1 * h2
dot_product = (h1 * h2).sum()
print("Поэлементная сумма:", elementwise_sum)
print("Поэлементное произведение:", elementwise_product)
print("Скалярное произведение:", dot_product)
#3
X = np.array([
    [20.1, 20.3, 19.8],
    [21.0, 20.7, 20.2],
    [19.5, 19.8, 19.3],
    [20.8, 21.1, 20.6]
])

col_means = np.mean(X, axis=0)
print("Среднее по столбцам:", col_means)

row_sums = np.sum(X, axis=1)
print("Сумма по строкам:", row_sums)

col_variances = np.var(X, axis=0, ddof=1)
print("Дисперсия по столбцам:", col_variances)

min_var_col_index = np.argmin(col_variances)
print("Индекс столбца с мин. дисперсией:", min_var_col_index)
#4
X = np.array([
    [20.1, 20.3, 19.8],
    [21.0, 20.7, 20.2],
    [19.5, 19.8, 19.3],
    [20.8, 21.1, 20.6]
])

col_min = np.min(X, axis=0)
col_max = np.max(X, axis=0)
print("Минимумы по столбцам:", col_min)
print("Максимумы по столбцам:", col_max)

col_range = col_max - col_min
print("Размах по столбцам:", col_range)

X_normalized = (X - col_min) / col_range
print("Нормализованная матрица:\n", X_normalized)

col_sums_after_norm = np.sum(X_normalized, axis=0)
print("Сумма по столбцам после нормализации:", col_sums_after_norm)
#5
ph = np.array([
    [7.1, 7.4, 7.0],
    [6.9, 7.2, 7.1],
    [7.3, 7.5, 7.2],
    [7.0, 7.1, 6.8],
    [6.8, 6.9, 6.7],
    [7.4, 7.6, 7.3]
])

row_means = np.mean(ph, axis=1)
print("Среднее pH по пробам:", row_means)

col_sums = np.sum(ph, axis=0)
print("Сумма pH по образцам:", col_sums)

row_sums = np.sum(ph, axis=1)
print("Сумма pH по пробам:", row_sums)

col_variances = np.var(ph, axis=0, ddof=1)
print("Дисперсия по образцам:", col_variances)
#6
consumption = np.array([
    [ 8,  6,  5], # Mon
    [10,  7,  6], # Tue
    [ 9,  8,  7], # Wed
    [11, 10,  9], # Thu
    [14, 12, 11], # Fri
    [16, 15, 13], # Sat
    [12, 11, 10]  # Sun
])
days = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
houses = ['H1','H2','H3']

house_totals = np.sum(consumption, axis=0)
print("Общее потребление по домам (H1, H2, H3):", house_totals)

day_totals = np.sum(consumption, axis=1)
print("Общее потребление по дням:", day_totals)

house_means = np.mean(consumption, axis=0)
print("Среднее потребление по домам (H1, H2, H3):", house_means)

day_index_max = np.argmax(day_totals)
day_name_max = days[day_index_max]
print("День с макс. потреблением:", day_name_max)

house_variances = np.var(consumption, axis=0, ddof=1)
print("Дисперсия по домам (H1, H2, H3):", house_variances)

most_stable_house_index = np.argmin(house_variances)
most_stable_house = houses[most_stable_house_index]
print(f"\nНаиболее стабильным является дом {most_stable_house}")
#7
sensors = np.array([
    [15, 101, 20, 0.5],
    [16, 100, 21, 0.6],
    [15, 102, 19, 0.4],
    [17, 103, 22, 0.7],
    [18, 104, 23, 0.6],
    [19, 105, 24, 0.8],
    [17, 103, 22, 0.5]
])
types = ['TempSensor','PressureSensor','FlowSensor','VibrationSensor']

sensor_totals = np.sum(sensors, axis=0)
print("Сумма показаний по группам:", dict(zip(types, sensor_totals)))

sensor_means = np.mean(sensors, axis=0)
print("Среднее показание по группам:", dict(zip(types, sensor_means)))

sensor_variances = np.var(sensors, axis=0, ddof=1)
print("Дисперсия по группам:", dict(zip(types, sensor_variances)))

max_total_index = np.argmax(sensor_totals)
group_max_total = types[max_total_index]
print("Группа с наибольшей суммой:", group_max_total)

most_stable_sensor_index = np.argmin(sensor_variances)
recommended_sensor = types[most_stable_sensor_index]
print(f"\nДля приоритетного мониторинга рекомендуется группа {recommended_sensor}")