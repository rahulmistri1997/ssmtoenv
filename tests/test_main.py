# tests/test_main.py
import pytest
from unittest.mock import patch
from ssmtoenv.main import fetch_and_add_to_env


@pytest.fixture
def mock_ssm_parameters() -> list[dict[str, str]]:
    """Mocked SSM parameters.

    Returns:
        list[dict[str, str]]: List of mocked SSM parameters.
    """
    return [
        {"Name": "/cloudflaretunnel/param1", "Value": "value1"},
        {"Name": "/cloudflaretunnel/param2", "Value": "value2"},
    ]


@patch("ssmtoenv.main.set_key")
@patch("ssmtoenv.main.find_dotenv", return_value=".env")
@patch("ssmtoenv.main.fetch_ssm_parameters")
@patch("ssmtoenv.main.typer")
def test_fetch_and_add_to_env(
    mock_typer,
    mock_fetch_ssm_parameters,
    mock_find_dotenv,
    mock_set_key,
    mock_ssm_parameters,
) -> None:
    """Test fetch_and_add_to_env function.

    Args:
        mock_typer (MagicMock): Mocked typer module.
        mock_fetch_ssm_parameters (MagicMock): Mocked fetch_ssm_parameters function.
        mock_find_dotenv (MagicMock): Mocked find_dotenv function.
        mock_set_key (MagicMock): Mocked set_key function.
        mock_ssm_parameters (list): List of mocked SSM parameters.

    """
    mock_typer.echo.side_effect = lambda x: print(x)

    mock_find_dotenv.return_value = ".env"
    mock_fetch_ssm_parameters.return_value = mock_ssm_parameters

    fetch_and_add_to_env(
        "access_key", "secret_key", "session_token", "/cloudflaretunnel/"
    )

    expected_calls = [
        "Fetching SSM parameters with prefix: /cloudflaretunnel/",
        "Added parameter: param1",
        "Added parameter: param2",
    ]

    # Make all expected calls to mock_typer.echo
    expected_calls: list[tuple[tuple[str]]] = [((call,),) for call in expected_calls]

    assert mock_typer.echo.call_args_list == expected_calls


if __name__ == "__main__":
    pytest.main()
