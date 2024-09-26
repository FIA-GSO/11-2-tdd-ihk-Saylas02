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


@pytest.mark.parametrize("erreichterWert, maxWert, expected", positive_testdata)
def test_berechne_prozente__positive(erreichterWert, maxWert, expected):
    assert berechnungsmodul.berechne_prozente(erreichterWert, maxWert) == expected


@pytest.mark.parametrize("erreichterWert, maxWert, expected", negative_testdata)
def test_berechne_prozente__negative(erreichterWert, maxWert, expected):
    assert berechnungsmodul.berechne_prozente(erreichterWert, maxWert) == expected


positive_testdata = [
    (100, "sehr gut"),
    (92, "sehr gut"),
    (91, "gut"),
    (81, "gut"),
    (80, "befriedigend"),
    (67, "befriedigend"),
    (66, "ausreichend"),
    (50, "ausreichend"),
    (49, "mangelhaft"),
    (30, "mangelhaft"),
    (29, "ungenügend"),
    (0, "ungenügend")
]

negative_testdata = [
    (" ", TypeError)
]


@pytest.mark.parametrize("erreichteProzent, expected", positive_testdata)
def test_berechne_note_von_prozent__positive(erreichteProzent, expected):
    assert berechnungsmodul.test_berechne_note_von_Prozent(erreichteProzent) == expected


@pytest.mark.parametrize("erreichteProzent, expected", negative_testdata)
def test_berechne_note_von_prozent__negative(erreichteProzent, expected):
    assert berechnungsmodul.test_berechne_note_von_Prozent(erreichteProzent) == expected