from typing import Dict, List, Optional


def calculate_sum(numbers: List[int]) -> int:
    total = 0
    for num in numbers:
        total += num
    return total


def process_data(data: Optional[str]) -> str:
    if data is None:
        return "No data"
    return f"Processed: {data}"


def create_user_dict(name: str, age: int) -> Dict[str, str]:
    return {"name": name, "age": str(age)}


def main() -> None:
    numbers = [1, 2, 3, 4, 5]
    result = calculate_sum(numbers)
    print(f"Sum: {result}")

    text_data = "Hello World"
    processed = process_data(text_data)
    print(processed)

    user = create_user_dict("Alice", 25)
    print(f"User: {user}")


if __name__ == "__main__":
    main()
