dz_pad_project
==============================

test homework rep

Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------

## Environment Setup

### 1. Create virtual environment (опционально)

```bash
# Linux/MacOS
python -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

### 2. Install dependencies

**Вариант А: Используя Poetry (рекомендуется)**

Установите Poetry, если еще не установлен:
```bash
# Linux/MacOS
curl -sSL https://install.python-poetry.org | python3 -

# Windows (PowerShell)
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -

# pip
pip install poetry
```


Затем установите зависимости:
```bash
poetry install
```

**Вариант Б: Используя pip (проще для Windows)**

```bash
pip install boto3 pandas python-dotenv
```

Для разработки также установите dev-зависимости:
```bash
pip install black flake8 pre-commit
```

### 3. Setup pre-commit hooks (опционально)

```bash
pre-commit install
pre-commit run --all-files
```

## Working with S3 (MinIO)

### 1. Start MinIO container

**На Linux/MacOS:**
```bash
docker-compose up -d
```

Или через Makefile:
```bash
make minio-up
```

**На Windows:**
```bash
docker-compose up -d
```

Или через bat-скрипт:
```cmd
scripts\minio_up.bat
```

MinIO будет доступен по адресу:
- API: http://localhost:9000
- Console: http://localhost:9001
- Credentials: minioadmin / minioadmin

### 2. Upload raw dataset to S3

**На Linux/MacOS:**
```bash
# С Poetry
poetry run python scripts/upload_raw.py \
    --bucket my-bucket \
    --key raw/titanic.csv \
    --file src/data/raw/Titanic-Dataset.csv

# Без Poetry
python scripts/upload_raw.py \
    --bucket my-bucket \
    --key raw/titanic.csv \
    --file src/data/raw/Titanic-Dataset.csv

# Через Makefile
make upload-raw BUCKET=my-bucket KEY=raw/titanic.csv FILE=src/data/raw/Titanic-Dataset.csv
```

**На Windows:**
```cmd
# Прямой запуск Python скрипта
python scripts/upload_raw.py --bucket my-bucket --key raw/titanic.csv --file src/data/raw/Titanic-Dataset.csv

# Через bat-скрипт (проще)
scripts\upload_raw.bat my-bucket raw/titanic.csv src/data/raw/Titanic-Dataset.csv
```

### 3. Run data processing pipeline

**На Linux/MacOS:**
```bash
# С Poetry
poetry run python scripts/s3_pipeline.py \
    --bucket my-bucket \
    --raw-key raw/titanic.csv \
    --out-key processed/titanic_processed.csv

# Без Poetry
python scripts/s3_pipeline.py \
    --bucket my-bucket \
    --raw-key raw/titanic.csv \
    --out-key processed/titanic_processed.csv

# Через Makefile
make pipeline BUCKET=my-bucket RAW_KEY=raw/titanic.csv OUT_KEY=processed/titanic_processed.csv
```

**На Windows:**
```cmd
# Прямой запуск Python скрипта
python scripts/s3_pipeline.py --bucket my-bucket --raw-key raw/titanic.csv --out-key processed/titanic_processed.csv

# Через bat-скрипт (проще)
scripts\run_pipeline.bat my-bucket raw/titanic.csv processed/titanic_processed.csv
```

### 4. Stop MinIO container

**На Linux/MacOS:**
```bash
docker-compose down
```

Или через Makefile:
```bash
make minio-down
```

**На Windows:**
```bash
docker-compose down
```

Или через bat-скрипт:
```cmd
scripts\minio_down.bat
```

## Project Structure

Сырые данные должны находиться в `src/data/raw/`, обработанные - в `src/data/processed/`.

**Важно:** Обработанные данные и временные файлы игнорируются git (см. `.gitignore`).

Модули проекта:
- `scripts/s3_utils.py` - утилиты для работы с S3
- `scripts/build_features.py` - функция обработки данных
- `scripts/upload_raw.py` - скрипт загрузки сырых данных в S3
- `scripts/s3_pipeline.py` - главный пайплайн обработки данных

## Требования для проверки

Для проверки проекта проверяющему необходимо:

1. **Клонировать репозиторий:**
   ```bash
   git clone <repository-url>
   cd my_pad_ds_project
   ```

2. **Установить зависимости:**
   ```bash
   # Вариант 1: через Poetry
   poetry install

   # Вариант 2: через pip
   pip install boto3 pandas python-dotenv
   # лучше
   pip install -r requirements.txt
   ```

3. **Запустить MinIO:**
   ```bash
   docker-compose up -d
   ```
   Проверить, что MinIO доступен: http://localhost:9001 (minioadmin/minioadmin)

4. **Загрузить сырой датасет в S3:**
   ```bash
   python scripts/upload_raw.py \
       --bucket my-bucket \
       --key raw/titanic.csv \
       --file src/data/raw/Titanic-Dataset.csv
   ```

5. **Запустить пайплайн обработки:**
   ```bash
   python scripts/s3_pipeline.py \
       --bucket my-bucket \
       --raw-key raw/titanic.csv \
       --out-key processed/titanic_processed.csv
   ```

Пайплайн должен:
- Скачать датасет из S3 в `src/data/raw/`
- Обработать данные (нормализация)
- Сохранить обработанные данные в `src/data/processed/`
- Загрузить обработанные данные обратно в S3
