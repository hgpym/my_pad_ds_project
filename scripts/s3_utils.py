"""Утилиты для работы с S3."""
import os
from typing import Any

import boto3
from botocore.client import Config


def get_s3_client(endpoint: str, access_key: str, secret_key: str) -> Any:
    """
    Создать клиент для работы с S3.

    Args:
        endpoint: URL эндпоинта S3 (например, http://localhost:9000 для MinIO)
        access_key: Access key для аутентификации
        secret_key: Secret key для аутентификации

    Returns:
        boto3.client: Клиент S3
    """
    return boto3.client(
        "s3",
        endpoint_url=endpoint,
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key,
        config=Config(signature_version="s3v4"),
    )


def ensure_bucket(client: Any, bucket: str) -> None:
    """
    Создать бакет в S3, если он не существует.

    Args:
        client: Клиент S3
        bucket: Имя бакета
    """
    try:
        client.head_bucket(Bucket=bucket)
    except Exception:
        client.create_bucket(Bucket=bucket)


def download_from_s3(client: Any, bucket: str, key: str, local_path: str) -> str:
    """
    Скачать файл из S3.

    Args:
        client: Клиент S3
        bucket: Имя бакета
        key: Путь к файлу в S3
        local_path: Локальный путь для сохранения файла

    Returns:
        str: Путь к скачанному файлу
    """
    os.makedirs(os.path.dirname(local_path), exist_ok=True)
    client.download_file(bucket, key, local_path)
    print(f"Downloaded s3://{bucket}/{key} -> {local_path}")
    return local_path


def upload_to_s3(
    client: Any, bucket: str, key: str, local_path: str, ensure_bucket_exists: bool = True
) -> str:
    """
    Загрузить файл в S3.

    Args:
        client: Клиент S3
        bucket: Имя бакета
        key: Путь к файлу в S3
        local_path: Локальный путь к файлу
        ensure_bucket_exists: Создать бакет, если не существует

    Returns:
        str: S3 URI загруженного файла (s3://bucket/key)
    """
    if ensure_bucket_exists:
        ensure_bucket(client, bucket)
    client.upload_file(local_path, bucket, key)
    s3_uri = f"s3://{bucket}/{key}"
    print(f"Uploaded {local_path} -> {s3_uri}")
    return s3_uri
