import sys


def test_environment() -> None:
    """Test that the environment is set up correctly."""
    python_version = sys.version_info
    assert python_version.major == 3
    assert python_version.minor >= 8
    print("✓ Environment is set up correctly!")


def main() -> None:
    """Main function."""
    test_environment()


if __name__ == "__main__":
    main()
