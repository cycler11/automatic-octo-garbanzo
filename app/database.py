from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import time

DB_URL = "postgresql://user:password@db:5432/test_db"
engine = create_engine(DB_URL)
Session = sessionmaker(bind=engine)
session = Session()

def get_test_data():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM test_cases"))
        return [dict(row._mapping) for row in result]

def save_test_results(test_suite_name, passed_tests, failed_tests, test_duration, code_complexity, code_coverage):
    test_result = {
        "test_suite_name": test_suite_name,
        "test_date": datetime.now(),
        "passed_tests": passed_tests,
        "failed_tests": failed_tests,
        "test_duration": test_duration,
        "code_complexity": code_complexity,
        "code_coverage": code_coverage
    }

    insert_query = text("""
        INSERT INTO test_results (test_suite_name, test_date, passed_tests, failed_tests, test_duration, code_complexity, code_coverage)
        VALUES (:test_suite_name, :test_date, :passed_tests, :failed_tests, :test_duration, :code_complexity, :code_coverage)
    """)
    
    with engine.connect() as conn:
        conn.execute(insert_query, test_result)

    session.commit()
