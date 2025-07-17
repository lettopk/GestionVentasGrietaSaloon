def importe_total_pedido(request):
    total= 0
    #if request.user.is_authenticated:
    #    for key, value in request.session["pedido"].item():
    #        total=total+(int(value["precio_unitario"])*value["cantidad"])
    return {"importe_total_pedido":total}