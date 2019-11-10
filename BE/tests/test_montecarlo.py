from BE.src.montecarlo import black_scholes


def test_black_scholes():
    output = black_scholes(100., 110., 2., 0.2, 0.03)
    assert output == 9.73983632580859
