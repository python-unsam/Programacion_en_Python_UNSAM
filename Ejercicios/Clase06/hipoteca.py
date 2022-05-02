# hipoteca.py

saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0
mes = 0
adelanto = 1000
pago_extra_mes_comienzo = 61
pago_extra_mes_fin = 108
pago_extra = 1000

while saldo != 0:
    mes += 1

    # 1.11 - el ultimo mes se ajusta para pagar lo adeudado (teniendo en cuenta la tasa nominal)
    if (saldo - pago_mensual) < 0:
        pago_mensual = saldo * (1 + tasa / 12)

    saldo = saldo * (1 + tasa / 12) - pago_mensual
    total_pagado = total_pagado + pago_mensual

    # 1.8 - durante los primeros 12 meses david va a pagar un adelanto de $1000
    #if mes <= 12:
    #    saldo -= adelanto
    #    total_pagado += adelanto

    # 1.9 - del 6to al 10mo año david paga un adelanto de $1000
    if mes >= pago_extra_mes_comienzo and mes <= pago_extra_mes_fin:
        saldo -= pago_extra
        total_pagado += pago_extra

    # 1.10 - se imprime la tabla
    print(f"{mes} {round(total_pagado, 2)} {round(saldo, 2)}")


print(f"Total pagado:   {round(total_pagado, 2)} \nMeses:  {mes}")
