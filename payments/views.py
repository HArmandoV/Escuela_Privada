from django.shortcuts import render

def meta_mensual(pago_sueldo_base, pago_adicional, meta_mensual):
    if meta_mensual:
        if colegio > 100:
            if promotor == "tiempo completo":
                pago_adicional = 5000
            else:
                pago_adicional = 2500
        else:
            if promotor == "tiempo completo":
                pago_adicional = 3600
            else:
                pago_adicional = 1800
        sueldo_total = pago_sueldo_base + pago_adicional
    else:
        sueldo_total = pago_sueldo_base
    return sueldo_total