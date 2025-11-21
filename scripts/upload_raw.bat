@echo off
REM Скрипт для загрузки сырых данных в S3 (Windows)

setlocal enabledelayedexpansion

REM Параметры по умолчанию
set ENDPOINT=http://localhost:9000
set ACCESS_KEY=minioadmin
set SECRET_KEY=minioadmin

REM Проверка обязательных параметров
if "%1"=="" (
    echo Usage: upload_raw.bat BUCKET KEY FILE [ENDPOINT] [ACCESS_KEY] [SECRET_KEY]
    echo Example: upload_raw.bat my-bucket raw/titanic.csv src/data/raw/Titanic-Dataset.csv
    exit /b 1
)

set BUCKET=%1
set KEY=%2
set FILE=%3

if "%BUCKET%"=="" (
    echo Error: BUCKET is required
    exit /b 1
)

if "%KEY%"=="" (
    echo Error: KEY is required
    exit /b 1
)

if "%FILE%"=="" (
    echo Error: FILE is required
    exit /b 1
)

REM Опциональные параметры
if not "%4"=="" set ENDPOINT=%4
if not "%5"=="" set ACCESS_KEY=%5
if not "%6"=="" set SECRET_KEY=%6

REM Переход в корень проекта и запуск скрипта
cd /d %~dp0..
python scripts/upload_raw.py --endpoint %ENDPOINT% --access-key %ACCESS_KEY% --secret-key %SECRET_KEY% --bucket %BUCKET% --key %KEY% --file %FILE%

endlocal
