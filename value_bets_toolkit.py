def detectar_value_bets(odd_real, odd_justa, margem=0.05):
    valor_teorico = 1 / odd_justa
    valor_real = 1 / odd_real
    return valor_teorico > valor_real * (1 + margem)
