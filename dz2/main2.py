import numpy as np
import matplotlib.pyplot as plt

dataset = np.loadtxt(
    "wine_quality.csv",
    delimiter=",",
    skiprows=1
)

alcohol = dataset[:, 0]
volatile_acidity = dataset[:, 1]
sulphates = dataset[:, 2]
pH = dataset[:, 3]
quality = dataset[:, 4]

# Task 1.1
columns = ['alcohol', 'volatile acidity', 'sulphates', 'pH', 'quality']
data_columns = [alcohol, volatile_acidity, sulphates, pH, quality]

for i, col in enumerate(columns):
    print(f"\n{col}:")
    print(f"  Mean: {data_columns[i].mean()}")
    print(f"  Median: {np.median(data_columns[i])}")
    print(f"  Variance: {data_columns[i].var(ddof=1)}")
    print(f"  Min: {data_columns[i].min()}")
    print(f"  Max: {data_columns[i].max()}")

# Task 1.2
max_qual = quality.max()
max_qual_indices = quality == max_qual
avg_pH_max_qual = pH[max_qual_indices].mean()
print(f"\nСредний pH для качества {max_qual}: {avg_pH_max_qual}")

# Task 1.3
min_qual = quality.min()
max_qual = quality.max()
quality_normalized = (quality - min_qual) / (max_qual - min_qual)
print(f"\nПервые 10 нормализованных значений quality:")
print(quality_normalized[:10])

# Task 2.1
plt.figure(figsize=(10, 6))

unique_qualities, counts = np.unique(quality, return_counts=True)

plt.subplot(1, 2, 1)
plt.pie(counts, labels=unique_qualities, autopct='%1.1f%%')
plt.title('Круговая диаграмма качества вина')

plt.subplot(1, 2, 2)
plt.bar(unique_qualities, counts, color='skyblue', edgecolor='black')
plt.xlabel('Качество вина')
plt.ylabel('Количество образцов')
plt.title('Столбчатая диаграмма качества вина')
plt.grid(axis='y', alpha=0.3)

plt.tight_layout()
plt.show()

# Task 2.2
plt.figure(figsize=(10, 6))

max_qual = quality.max()
min_qual = quality.min()

low_quality_indices = quality == min_qual
high_quality_indices = quality == max_qual

plt.scatter(x=volatile_acidity[low_quality_indices],
            y=alcohol[low_quality_indices],
            color='green', alpha=0.7, label=f'Низкое качество ({min_qual})')

plt.scatter(x=volatile_acidity[high_quality_indices],
            y=alcohol[high_quality_indices],
            color='orange', alpha=0.7, label=f'Высокое качество ({max_qual})')

plt.xlabel("Летучая кислотность (volatile acidity)")
plt.ylabel("Алкоголь (alcohol)")
plt.title("Зависимость качества вина от кислотности и алкоголя")
plt.legend()
plt.grid(alpha=0.3)
plt.show()

"Вывод: Глядя на график, можно сделать вывод о том, что:"
"- Вина высокого качества имеют тенденцию к более низкому содержанию летучей кислотности"
"- Вина высокого качества часто имеют более высокое содержание алкоголя"
"- Вина низкого качества обычно содержат больше летучей кислоты"
"- Существует обратная зависимость между летучей кислотностью и качеством вина"
"- Существует прямая зависимость между содержанием алкоголя и качеством вина"