import pytest
import berechnungsmodul

positive_testdata = [
    (40, 50, 80),
    (0, 50, 0),
    (50, 50, 100),
    (33, 50, 66),
    (25, 50, 50)
]

negative_testdata = [
    (" ", 1, TypeError),
    (1, "", TypeError),
    (1, 0, ValueError),
    (-1, 0, ValueError),
    (101, 100, ValueError)
]


@pytest.mark.parametrize("erreichterWert", "maxWert, expected", positive_testdata)
def test_berechne_prozente__positive(erreichterWert, maxWert, expected):
    assert berechnungsmodul.berechne_prozente(erreichterWert, maxWert) == expected


@pytest.mark.parametrize("erreichterWert", "maxWert, expected", negative_testdata)
def test_berechne_prozente__positive(erreichterWert, maxWert, expected):
    assert berechnungsmodul.berechne_prozente(erreichterWert, maxWert) == expected