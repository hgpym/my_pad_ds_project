@echo off
REM Скрипт для запуска пайплайна обработки данных (Windows)

setlocal enabledelayedexpansion

REM Переход в корень проекта (родительская директория от scripts)
cd /d %~dp0..

REM Параметры по умолчанию
set ENDPOINT=http://localhost:9000
set ACCESS_KEY=minioadmin
set SECRET_KEY=minioadmin
set OUT_KEY=processed/data_processed.csv

REM Проверка обязательных параметров
if "%1"=="" (
    echo Usage: run_pipeline.bat BUCKET RAW_KEY [OUT_KEY] [ENDPOINT] [ACCESS_KEY] [SECRET_KEY]
    echo Example: run_pipeline.bat my-bucket raw/titanic.csv processed/titanic_processed.csv
    exit /b 1
)

set BUCKET=%1
set RAW_KEY=%2

if "%BUCKET%"=="" (
    echo Error: BUCKET is required
    exit /b 1
)

if "%RAW_KEY%"=="" (
    echo Error: RAW_KEY is required
    exit /b 1
)

REM Опциональные параметры
if not "%3"=="" set OUT_KEY=%3
if not "%4"=="" set ENDPOINT=%4
if not "%5"=="" set ACCESS_KEY=%5
if not "%6"=="" set SECRET_KEY=%6

REM Запуск скрипта
python scripts/s3_pipeline.py --endpoint %ENDPOINT% --access-key %ACCESS_KEY% --secret-key %SECRET_KEY% --bucket %BUCKET% --raw-key %RAW_KEY% --out-key %OUT_KEY%

endlocal
