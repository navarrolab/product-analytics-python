import pandas as pd
import numpy as np

# Данные о ежедневных продажах двух магазинов
data = {
    'day': ['Пн', 'Вт', 'Ср', 'Чт', 'Пт'],
    'shop_A': [50, 50, 50, 50, 50],
    'shop_B': [10, 90, 30, 70, 50]
}
df = pd.DataFrame(data)

print("=== Данные о продажах (тыс. руб.) ===")
print(df)

print("\n=== Статистика по магазину А ===")
print(f"Среднее: {df['shop_A'].mean():.1f}")
print(f"Дисперсия (выборочная): {df['shop_A'].var():.1f}")
print(f"Стандартное отклонение: {df['shop_A'].std():.1f}")
print(f"Коэффициент вариации: {df['shop_A'].std() / df['shop_A'].mean() * 100:.1f}%")

print("\n=== Статистика по магазину Б ===")
print(f"Среднее: {df['shop_B'].mean():.1f}")
print(f"Дисперсия (выборочная): {df['shop_B'].var():.1f}")
print(f"Стандартное отклонение: {df['shop_B'].std():.1f}")
print(f"Коэффициент вариации: {df['shop_B'].std() / df['shop_B'].mean() * 100:.1f}%")