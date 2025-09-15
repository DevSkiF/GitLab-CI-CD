import subprocess

def test_program(program_path):
    # Словарь ожидаемых результатов для каждого входного значения
    expected_results = {
        "1": "Learning to Linux\n",
        "2": "Learning to work with Network\n",
        "3": "Learning to Monitoring\n",
        "4": "Learning to extra Monitoring\n",
        "5": "Learning to Docker\n",
        "6": "Learning to CI/CD\n"
    }

    all_tests_passed = True  # Флаг для отслеживания успешности всех тестов

    # Проверка корректных входных данных
    for input_value, expected_output in expected_results.items():
        result = subprocess.run([program_path, input_value], capture_output=True, text=True)
        if result.returncode != 0 or result.stdout != expected_output:
            print(f"Test failed for input {input_value}. Expected: '{expected_output}', Got: '{result.stdout.strip()}'")
            all_tests_passed = False
        else:
            print(f"Test passed for input {input_value}.")

    # Проверка некорректных входных данных
    invalid_inputs = ["0", "7", "abc", ""]
    for input_value in invalid_inputs:
        result = subprocess.run([program_path, input_value], capture_output=True, text=True)
        if result.returncode != -2 or "Bad number!" not in result.stdout:
            print(f"Test failed for invalid input {input_value}. Expected return code -2 and 'Bad number!', Got: '{result.stdout.strip()}'")
            all_tests_passed = False
        else:
            print(f"Test passed for invalid input {input_value}.")

    # Проверка отсутствия аргументов
    result = subprocess.run([program_path], capture_output=True, text=True)
    if result.returncode != -1 or "Bad number of arguments!" not in result.stdout:
        print("Test failed for missing arguments. Expected return code -1 and 'Bad number of arguments!', Got: '{result.stdout.strip()}'")
        all_tests_passed = False
    else:
        print("Test passed for missing arguments.")

    # Итоговый результат тестирования
    if all_tests_passed:
        print("All tests passed!")
    else:
        print("Some tests failed!")

program_path = "../code-samples/DO"
test_program(program_path)