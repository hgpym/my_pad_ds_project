"""Скрипт для обработки данных."""
import os

import pandas as pd


def process_data(input_path: str, output_path: str) -> str:
    """
    Обработать данные: заполнить пропуски и нормализовать числовые колонки.

    Args:
        input_path: Путь к входному CSV файлу
        output_path: Путь для сохранения обработанного CSV файла

    Returns:
        str: Путь к обработанному файлу
    """
    df = pd.read_csv(input_path)

    # Заполнить пропуски нулями
    df = df.fillna(0)

    # Нормализовать числовые колонки
    num_cols = df.select_dtypes(include="number").columns
    if len(num_cols) > 0:
        # Z-score нормализация
        means = df[num_cols].mean()
        stds = df[num_cols].std().replace(0, 1)  # Избегаем деления на 0
        df[num_cols] = (df[num_cols] - means) / stds

    # Создать директорию, если не существует
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Сохранить обработанные данные
    df.to_csv(output_path, index=False)
    print(f"Processed data saved to {output_path}")

    return output_path


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Process raw data")
    parser.add_argument("input_path", type=str, help="Path to input CSV file")
    parser.add_argument("output_path", type=str, help="Path to output CSV file")

    args = parser.parse_args()
    process_data(args.input_path, args.output_path)
