

def test_get_full_config_returns_list():
    data = get_config_value()
    assert isinstance(data, list)
    assert data


def test_get_first_value_viva_staging():
    url = get_first_value("url", "Viva", "staging")
    assert url == "https://staging-api.vivaaaa.com"


def test_get_config_value_headers():
    headers = get_config_value("Viva_headers")
    assert isinstance(headers, dict)
    assert "Z-App-Info" in headers


def test_get_config_value_default_fallback():
    missing = get_config_value("url", "non_exist", default="missing")
    assert missing == "missing"
