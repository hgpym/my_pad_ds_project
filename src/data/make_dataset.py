from pathlib import Path


def make_dataset() -> None:
    """Create dataset directory structure."""
    data_dir = Path("data")
    data_dir.mkdir(exist_ok=True)
    (data_dir / "raw").mkdir(exist_ok=True)
    (data_dir / "processed").mkdir(exist_ok=True)
    (data_dir / "external").mkdir(exist_ok=True)
    print("Dataset directory structure created!")


if __name__ == "__main__":
    make_dataset()
