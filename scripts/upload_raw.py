"""Скрипт для загрузки сырых данных в S3."""
import argparse
import sys
from pathlib import Path

# Добавляем директорию scripts в путь для импорта модулей
scripts_dir = Path(__file__).resolve().parent
scripts_dir_str = str(scripts_dir)
if scripts_dir_str not in sys.path:
    sys.path.insert(0, scripts_dir_str)

# Импорт модулей из scripts/ (noqa: E402 - импорт после изменения sys.path)
from s3_utils import get_s3_client, upload_to_s3  # noqa: E402


def main() -> None:
    """Загрузить сырой датасет в S3."""
    parser = argparse.ArgumentParser(description="Upload raw dataset to S3")
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
    parser.add_argument("--key", required=True, help="S3 key for the file")
    parser.add_argument("--file", required=True, help="Local path to the file to upload")

    args = parser.parse_args()

    # Создать S3 клиент
    client = get_s3_client(args.endpoint, args.access_key, args.secret_key)

    # Загрузить файл в S3
    upload_to_s3(client, args.bucket, args.key, args.file)


if __name__ == "__main__":
    main()
