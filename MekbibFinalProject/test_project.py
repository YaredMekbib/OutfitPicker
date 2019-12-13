# Testing if the number of elements in light longsleeves increases everytime there is an input
def test_lightlongsleeves():
    light_longsleeves = []
    input = 'light blue'
    second_input = 'light green'
    light_longsleeves.append(input)
    light_longsleeves.append(second_input)

    return light_longsleeves
    assert len(light_longsleeves) >= 1


# Testing if the number of elements in dark longsleeves increases everytime there is an input
def test_darklongsleeves():
    dark_longsleeves = []
    input = 'dark blue'
    second_input = 'dark green'
    dark_longsleeves.append(input)
    dark_longsleeves.append(second_input)

    return dark_longsleeves
    assert len(dark_longsleeves) >= 1
