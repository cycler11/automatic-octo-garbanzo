from database import get_test_data

def calculate_discount(price, discount):
    """Рассчитывает цену после применения скидки."""
    if discount < 0 or discount > 100:
        raise ValueError("Invalid discount")
    return price - (price * discount / 100)

def main():
    """Основная логика: берет тестовые данные из БД и считает скидки."""
    test_cases = get_test_data()

    print("Рассчет скидок по тестовым данным:")
    for case in test_cases:
        price = case["price"]
        discount = case["discount"]
        result = calculate_discount(price, discount)
        print(f"Цена: {price}, Скидка: {discount}% → Итоговая цена: {result}")

if __name__ == "__main__":
    main()
