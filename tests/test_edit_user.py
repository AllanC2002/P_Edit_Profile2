import pytest
from unittest.mock import patch, MagicMock
from main import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    return app.test_client()

@patch("main.jwt.decode")
@patch("services.functions.conection_accounts")
@patch("services.functions.conection_userprofile")
def test_edit_user_success(mock_userprofile, mock_accounts, mock_jwt_decode, client):
    # Simulate the JWT decode function
    mock_jwt_decode.return_value = {"user_id": 1}

    # Mock the database connections
    mock_session_accounts = MagicMock()
    mock_session_userprofile = MagicMock()
    mock_accounts.return_value = mock_session_accounts
    mock_userprofile.return_value = mock_session_userprofile

    fake_user = MagicMock()
    fake_user.Id_User = 1
    fake_user.Status = 1
    fake_profile = MagicMock()
    fake_profile.Id_User = 1
    fake_profile.Status_account = 1

    mock_session_accounts.query().filter_by().first.return_value = fake_user
    mock_session_userprofile.query().filter_by().first.return_value = fake_profile

    # Data to update
    data = {
        "Name": "Carlos",
        "Lastname": "Ramírez",
        "Password": "nuevaclave"
    }

    # TToken for authorization
    token = "false.token.jwt"

    response = client.patch(
        "/update-user",
        json=data,
        headers={"Authorization": f"Bearer {token}"}
    )

    assert response.status_code == 200
    assert response.json["message"] == "User data updated successfull"
