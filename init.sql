-- Создаем таблицу для хранения результатов тестов
CREATE TABLE IF NOT EXISTS test_results (
    id SERIAL PRIMARY KEY,
    test_suite_name VARCHAR(255) NOT NULL,
    test_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    passed_tests INTEGER NOT NULL,
    failed_tests INTEGER NOT NULL,
    test_duration FLOAT NOT NULL,  -- Время выполнения тестов в секундах
    code_complexity FLOAT,        -- Сложность кода
    code_coverage FLOAT          -- Покрытие кода
);

-- Пример тестовых данных для таблицы test_cases
CREATE TABLE IF NOT EXISTS test_cases (
    id SERIAL PRIMARY KEY,
    price NUMERIC NOT NULL,
    discount NUMERIC NOT NULL,
    expected NUMERIC NOT NULL
);

INSERT INTO test_cases (price, discount, expected) VALUES
(100, 10, 90),
(200, 20, 160),
(50, 5, 47.5);
