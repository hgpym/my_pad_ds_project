"""Главный скрипт пайплайна обработки данных с S3."""
import argparse
import sys
from pathlib import Path

from build_features import process_data  # noqa: E402
from s3_utils import download_from_s3, get_s3_client, upload_to_s3

# Добавляем директорию scripts в путь для импорта модулей
scripts_dir = Path(__file__).resolve().parent
scripts_dir_str = str(scripts_dir)
if scripts_dir_str not in sys.path:
    sys.path.insert(0, scripts_dir_str)


def main() -> None:
    """Запуск пайплайна: скачивание из S3 -> обработка -> загрузка в S3."""
    parser = argparse.ArgumentParser(
        description="Pipeline: download from S3 -> process -> upload to S3"
    )
    parser.add_argument(
        "--endpoint",
        default="http://localhost:9000",
        help="S3 endpoint URL (default: http://localhost:9000)",
    )
    parser.add_argument(
        "--access-key", default="minioadmin", help="S3 access key (default: minioadmin)"
    )
    parser.add_argument(
        "--secret-key", default="minioadmin", help="S3 secret key (default: minioadmin)"
    )
    parser.add_argument("--bucket", required=True, help="S3 bucket name")
    parser.add_argument("--raw-key", required=True, help="S3 key for raw dataset")
    parser.add_argument(
        "--out-key",
        default="processed/data_processed.csv",
        help=("S3 key for processed dataset " "(default: processed/data_processed.csv)"),
    )
    parser.add_argument(
        "--local-raw",
        default="src/data/raw/data.csv",
        help="Local path for raw data (default: src/data/raw/data.csv)",
    )
    parser.add_argument(
        "--local-processed",
        default="src/data/processed/data_processed.csv",
        help=("Local path for processed data " "(default: src/data/processed/data_processed.csv)"),
    )

    args = parser.parse_args()

    # Создать S3 клиент
    client = get_s3_client(args.endpoint, args.access_key, args.secret_key)

    # Шаг 1: Скачать сырые данные из S3
    print("Step 1: Downloading raw data from S3...")
    download_from_s3(client, args.bucket, args.raw_key, args.local_raw)

    # Шаг 2: Обработать данные
    print("Step 2: Processing data...")
    process_data(args.local_raw, args.local_processed)

    # Шаг 3: Загрузить обработанные данные в S3
    print("Step 3: Uploading processed data to S3...")
    dest = upload_to_s3(client, args.bucket, args.out_key, args.local_processed)

    print("\nPipeline completed successfully!")
    print(f"Processed file uploaded to: {dest}")


if __name__ == "__main__":
    main()
