@echo off
REM Скрипт для запуска MinIO контейнера (Windows)

echo Starting MinIO container...
docker-compose up -d
echo.
echo MinIO API: http://localhost:9000
echo MinIO Console: http://localhost:9001
echo Credentials: minioadmin / minioadmin
