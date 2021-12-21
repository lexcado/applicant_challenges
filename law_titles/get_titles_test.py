from get_titles import get_testgb_titles


def test_get_testgb_titles():
    expected_titles = [
        "Beginn der Rechtsfähigkeit",
        "Eintritt der Volljährigkeit",
        "(weggefallen)",
        "Wohnsitz; Begründung und Aufhebung",
        "Wohnsitz nicht voll Geschäftsfähiger",
        "Wohnsitz eines Soldaten",
        "(weggefallen)",
        "Wohnsitz des Kindes",
        "Namensrecht",
        "Verbraucher",
    ]
    extracted_titles = get_testgb_titles()

    assert expected_titles == extracted_titles
