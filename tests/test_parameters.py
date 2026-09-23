"""Тесты функций работы с параметрами."""

from parameters import (
    add_parameter,
    check_parameter_value,
    filter_parameters_by_type,
    reset_parameter_to_default,
    sort_parameters_by_key,
    update_parameter_value,
    validate_parameter_value,
)


def test_add_parameter():
    parameters = []
    parameter = add_parameter(
        parameters, 1, "font_size", 14, "int", 12, min_value=10, max_value=24,
    )
    assert len(parameters) == 1
    assert parameter["value"] == 14


def test_validate_parameter_value_in_range():
    parameters = []
    parameter = add_parameter(
        parameters, 1, "font_size", 14, "int", 12, min_value=10, max_value=24,
    )
    assert validate_parameter_value(parameter, 20)
    assert not validate_parameter_value(parameter, 40)


def test_update_parameter_value():
    parameters = []
    add_parameter(
        parameters, 1, "font_size", 14, "int", 12, min_value=10, max_value=24,
    )
    assert update_parameter_value(parameters, 1, "font_size", 18)
    assert not update_parameter_value(parameters, 1, "font_size", 100)


def test_reset_parameter_to_default():
    parameters = []
    add_parameter(
        parameters, 1, "font_size", 14, "int", 12, min_value=10, max_value=24,
    )
    update_parameter_value(parameters, 1, "font_size", 18)
    assert reset_parameter_to_default(parameters, 1, "font_size")
    assert parameters[0]["value"] == 12


def test_check_parameter_value():
    parameters = []
    add_parameter(
        parameters, 1, "font_size", 14, "int", 12, min_value=10, max_value=24,
    )
    assert check_parameter_value(parameters, 1, "font_size", 20)
    assert not check_parameter_value(parameters, 1, "font_size", 100)
    assert not check_parameter_value(parameters, 1, "missing_key", 20)


def test_filter_parameters_by_type():
    parameters = []
    add_parameter(parameters, 1, "theme", "dark", "str", "light")
    add_parameter(
        parameters, 1, "font_size", 14, "int", 12, min_value=10, max_value=24,
    )
    result = list(filter_parameters_by_type(parameters, "int"))
    assert len(result) == 1
    assert result[0]["key"] == "font_size"


def test_sort_parameters_by_key():
    parameters = []
    add_parameter(parameters, 1, "theme", "dark", "str", "light")
    add_parameter(
        parameters, 1, "font_size", 14, "int", 12, min_value=10, max_value=24,
    )
    sorted_parameters = sort_parameters_by_key(parameters)
    assert sorted_parameters[0]["key"] == "font_size"
