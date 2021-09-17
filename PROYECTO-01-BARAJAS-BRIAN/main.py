from lista import *
usuario = []
usuarios = [["JavierRamrez1","10"],["Adm_JuanP13","Abc123"],["Adm_Rocio12","Bre234"],["1","1"],["Prueba1","123"],["Prueba2","234"]]
usuario_invalido = True
intento = 1


nombre = input("Ingrese su nombre de usuario para entrar: ")
usuario.append(nombre)

#Creamos una interfaz de inicio que permita acceder al sistema de datos con un usuario y una contraseña con un maximo de 5 intentos
while usuario_invalido and intento < 5:
  for usuario1 in usuarios:
    if usuario[0] == usuario1[0]:
      print("Usuario correcto!!")
      contraseña = input("Ahora ingrese la contraseña de su usuario: ")
      usuario.append(contraseña)
      if usuario[1] == usuario1[1]:
        print("Contraseña correcta!!")
        print("Bienvenido " + nombre + "!! :) \n")
        usuario_invalido = False
        break
      else:
        print("Contraseña incorrecta!")
        print("Recuerde escribir correctamente las mayusculas y minisculas")
        usuario.remove(contraseña)
  #print(usuario)  
  if usuario[0] == usuario1[0]:
    if usuario[1] == usuario1[1]:
      break
  print("Usuario inexistente en la base de datos! ")
  print("Intente nuevamente")
  usuario.remove(nombre)
  nombre = input("Ingrese su nombre de usuario para entrar: ")
  usuario.append(nombre)
  #print(usuario)
  intento += 1
#Ahora empieza el procesamiento de datos
#continuar = True
if intento < 5:
  continuar = True

#Creacion de listas para contar el numero de busquedas de cada producto
  variable = 0
  suma = 0
  b_sumas = []
  b_productos = [0]
  for elemento in lifestore_searches:
    if elemento[1] == variable:
      suma += 1
    elif elemento[1] != variable:
      b_sumas.append(suma)
      # print(b_sumas)
      variable = elemento[1]
      b_productos.append(variable)
      suma = 1
  b_sumas.append(suma)
  b_productos.remove(0)
  b_sumas.remove(0)
  #print(b_sumas)
  #print(b_productos)
  # print(len(b_sumas))
  # print(len(b_productos))
 


  #En este for creamos una lista con los productos que no registran ninguna busqueda
  no_buscados = []
  for elemento in lifestore_products:
    no_buscados.append(elemento[0])
    #print(no_vendidos)
    for buscado in b_productos:
      if elemento[0] == buscado:
        #print()
        no_buscados.remove(elemento[0])
  #print(no_buscados)


  #Creamos una lista doble de los productos más buscados con el ID y la cantidad de busquedas
  contador = 0
  mas_buscados = [[0,0]]
  #m_b2 = []
  for elemento in b_productos:
    if b_sumas[contador] >= mas_buscados[0][0] and len(mas_buscados) >= 10:
      mas_buscados.remove(mas_buscados[0])
      #m_b2.remove(m_b2[0])
      mas_buscados.append([b_sumas[contador] ,elemento])
      mas_buscados.sort()
    elif b_sumas[contador] >= mas_buscados[0][0]:
      mas_buscados.append([b_sumas[contador] ,elemento])
      mas_buscados.sort()
    #print(mas_buscados)
    contador += 1
  #print(mas_buscados)



#Se hace una lista con los ID de los productos y sus ventas totales
  variable = 1
  suma = 0
  v_sumas = []
  v_productos = []
  for elemento in lifestore_sales:
    if elemento[1] == variable:
      suma += 1
    elif elemento[1] != variable:
      v_sumas.append(suma)
      #print(b_sumas)
      v_sumas.append(variable)
      variable = elemento[1]
      suma = 1
      v_productos.append(v_sumas)
      v_sumas = []
  v_sumas.append(suma)
  v_sumas.append(variable)
  v_productos.append(v_sumas)
  #print(v_productos)
  #print(len(v_productos))

  v_productos.sort()
  contador = 0
  mas_vendidos = []
  while contador < 10:
    mas_vendidos.append(v_productos[-contador -1])
    contador += 1
  #print(mas_vendidos)

  #no_vendidos = lifestore_products[0]
  no_vendidos = []
  for elemento in lifestore_products:
    no_vendidos.append(elemento[0])
    #print(no_vendidos)
    for vendido in v_productos:
      if elemento[0] == vendido[1]:
        #print()
        no_vendidos.remove(elemento[0])
        #print(no_vendidos)
  #print(no_vendidos)


#clasificacion por calificacion promedio
  calificacion = []
  p_calificaciones = []
  suma = 0.0
  suma_devolucion = 0
  for elemento in v_productos:
    for venta in lifestore_sales:
      if elemento[1] == venta[1]:
        calificacion.append(venta[2])
        if venta[4] == 1:
          suma_devolucion += 1
    for numero in calificacion:
      suma += numero
    promedio = int(suma / len(calificacion))
    p_calificaciones.append([promedio, elemento[1], suma_devolucion])
    suma = 0
    suma_devolucion = 0
    calificacion = []
  #print(p_calificaciones)
  calif_excelentes = []
  calif_buenas = []
  calif_malas = []
  for calif in p_calificaciones:
    if calif[0] == 5:
      calif_excelentes.append(calif[1])
    elif calif[0] <= 2:
      calif_malas.append(calif[1])
    else:
      calif_buenas.append(calif[1])
  # print(calif_excelentes)
  # print(calif_malas)
  # print(calif_buenas)

#clasificacion de precios
  precios = []
  for elemento in lifestore_products:
    precios.append([elemento[2], elemento[0]])
  precios.sort()
  #print(precios)
  contador = 0
  mas_caros = []
  mas_baratos = []
  while contador < 10:
    mas_caros.append(precios[-contador -1])
    mas_baratos.append(precios[contador])
    contador += 1
  #print(mas_baratos)
  #print(mas_caros)

#organizacion del stock
  stock = []
  mayor_stock = []
  menor_stock = []
  for producto in lifestore_products:
    stock.append([producto[4], producto[0]])
  stock.sort()
  contador = 0
  while contador < 10:
    mayor_stock.append(stock[-contador -1])
    menor_stock.append(stock[contador])
    contador += 1

#Relaciones de los productos 
  #print(no_vendidos)
  no_buscado_o_vendidos = []
  for producto in no_vendidos:
    for elemento in no_buscados:
      #print(elemento)
      if producto == elemento:
        no_buscado_o_vendidos.append(producto)
  #print(no_buscado_o_vendidos)
  no_vendidos_caros = []
  for producto in no_vendidos:
    for elemento in mas_caros:
      #print(elemento)
      if producto == elemento[1]:
        no_vendidos_caros.append(producto)
  #print(no_vendidos_caros)
  no_vendidos_baratos = []
  for producto in no_vendidos:
    for elemento in mas_baratos:
      #print(elemento)
      if producto == elemento[1]:
        no_vendidos_baratos.append(producto)
  #print(no_vendidos_baratos)

  #relaciones de stock
  stock_vendidos = []
  for producto in mayor_stock:
    for elemento in mas_vendidos:
      if producto[1] == elemento[1]:
        stock_vendidos.append(producto[1])
  #print(stock_vendidos)
  stock_poco = []
  for producto in menor_stock:
    # for elemento in calif_buenas:
    #   if producto[1] == elemento:
    #     stock_poco.append(elemento)
    for elemento in calif_excelentes:
      if producto[1] == elemento:
        stock_poco.append(elemento)
  #print(stock_poco)

  #vendidos relaciones
  vendidos_sin_busqueda = []
  for elemento in mas_vendidos:
    for producto in no_buscados:
      if elemento[1] == producto:
        vendidos_sin_busqueda.append(producto)
  #print(vendidos_sin_busqueda)
  vendidos_caros = []
  for elemento in mas_vendidos:
    for producto in mas_caros:
      if elemento[1] == producto[1]:
        vendidos_caros.append(producto[1])
  #print(vendidos_caros)


  #Registro anual
  anual = []
  enero = []
  febrero = []
  marzo = []
  abril = []
  mayo = []
  junio = []
  julio = []
  agosto = []
  septiembre = []
  octubre = []
  noviembre = []
  diciembre = []
  for producto in lifestore_sales:
    variable = producto[3]
    if variable[3:5] == "01":
      for elemento in lifestore_products:
        if producto[1] == elemento[0]:
          enero.append(elemento[2])
    if variable[3:5] == "02":
      for elemento in lifestore_products:
        if producto[1] == elemento[0]:
          febrero.append(elemento[2])
    if variable[3:5] == "03":
      for elemento in lifestore_products:
        if producto[1] == elemento[0]:
          marzo.append(elemento[2])
    if variable[3:5] == "04":
      for elemento in lifestore_products:
        if producto[1] == elemento[0]:
          abril.append(elemento[2])
    if variable[3:5] == "05":
      for elemento in lifestore_products:
        if producto[1] == elemento[0]:
          mayo.append(elemento[2])
    if variable[3:5] == "06":
      for elemento in lifestore_products:
        if producto[1] == elemento[0]:
          junio.append(elemento[2])
    if variable[3:5] == "07":
      for elemento in lifestore_products:
        if producto[1] == elemento[0]:
          julio.append(elemento[2])
    if variable[3:5] == "08":
      for elemento in lifestore_products:
        if producto[1] == elemento[0]:
          agosto.append(elemento[2])
    if variable[3:5] == "09":
      for elemento in lifestore_products:
        if producto[1] == elemento[0]:
          septiembre.append(elemento[2])
    if variable[3:5] == "10":
      for elemento in lifestore_products:
        if producto[1] == elemento[0]:
          octubre.append(elemento[2])
    if variable[3:5] == "11":
      for elemento in lifestore_products:
        if producto[1] == elemento[0]:
          noviembre.append(elemento[2])
    if variable[3:5] == "12":
      for elemento in lifestore_products:
        if producto[1] == elemento[0]:
          diciembre.append(elemento[2])
    
  ene = 0
  for venta in enero:
    ene += venta
  feb = 0
  for venta in febrero:
    feb += venta
  mar = 0
  for venta in marzo:
    mar += venta
  abr = 0
  for venta in abril:
    abr += venta
  may = 0
  for venta in mayo:
    may += venta
  jun = 0
  for venta in junio:
    jun += venta
  jul = 0
  for venta in julio:
    jul += venta
  ago = 0
  for venta in agosto:
    ago += venta
  sep = 0
  for venta in septiembre:
    sep += venta
  octu = 0
  for venta in octubre:
    octu += venta
  nov = 0
  for venta in noviembre:
    nov += venta
  dic = 0
  for venta in diciembre:
    dic += venta

  año = []
  año.append([ene, "enero"])
  año.append([feb, "febrero"])
  año.append([mar, "marzo"])
  año.append([abr, "abril"])
  año.append([may, "mayo"])
  año.append([jun, "junio"])
  año.append([jul, "julio"])
  año.append([ago, "agosto"])
  año.append([sep, "septiembre"])
  año.append([nov, "noviembre"])
  año.append([dic, "diciembre"])
  año.append([octu, "octubre"])


  while continuar:
    print("\n   Menu de opciones")
    consulta = input("Presione\n 1 para ver los productos más vendidos\n 2 para ver los productos menos vendidos\n 3 para ver las calificaciones promedio de los productos\n 4 para ver los productos más costosos\n 5 para ver los productos más baratos\n 6 para ver los productos más buscados\n 7 para ver los productos sin busquedas\n 8 para ver productos con mayor stock\n 9 para ver productos con menor stock\n 10 para ver los ingresos registrados\n 11 para ver las relaciones de los productos sin vender (opción recomendada) \n 12 para ver las relaciones de los productos con mayor cantidad en stock (opción recomendada) \n 13 para ver las relaciones de los productos más vendidos (opción recomendada) \n")

    if consulta == "1":
      print("Los 10 productos más vendidos son: ")
      for producto in mas_vendidos:
        for elemento in lifestore_products:
          if producto[1] == elemento[0]:
            print(elemento[0])
            print(elemento[1])
            print("con ")
            print(producto[0])
            for devolucion in p_calificaciones:
                if devolucion[1] == producto[1]:
                  print("Y con un total de devoluciones de: ")
                  print(devolucion[2])
            print("\n")
      repetir = input("¿Desea consultar otro dato? (si/no) ")
      if repetir != "si" and repetir != "Si":
        continuar = False


    elif consulta == "2":
      print("Los productos que no registran ventas son: ")
      for producto in no_vendidos:
        for elemento in lifestore_products:
          if producto == elemento[0]:
            print(elemento[0])
            print(elemento[1])
            print("\n")
      repetir = input("¿Desea consultar otro dato? (si/no) ")
      if repetir != "si" and repetir != "Si":
        continuar = False
      
    elif consulta == "3":
      print("Elija una de las siguientes listas para revisar (escribir como se indica dentro de las comillas)")
      rango_calif = input("'calificaciones excelentes' (5 estrellas)\n 'calificaciones buenas' (3-4 estrellas)\n 'calificaciones malas' (1-2 estrellas) \n")
      if rango_calif == "calificaciones excelentes":
        print("Los productos con un promedio (redondeado) de 5 estrellas son: \n")
        for calif in calif_excelentes:
          for elemento in lifestore_products:
            if calif == elemento[0]:
              print(elemento[0])
              print(elemento[1])
              for devolucion in p_calificaciones:
                if devolucion[1] == calif:
                  print("con un total de devoluciones de: ")
                  print(devolucion[2])
              
              print("\n")
        repetir = input("¿Desea consultar otro dato? (si/no) ")
        if repetir != "si" and repetir != "Si":
          continuar = False

      if rango_calif == "calificaciones buenas":
        print("Los productos con un promedio (redondeado) de 3 a 4 estrellas son: \n")
        for calif in calif_buenas:
          for elemento in lifestore_products:
            if calif == elemento[0]:
              print(elemento[0])
              print(elemento[1])
              for devolucion in p_calificaciones:
                if devolucion[1] == calif:
                  print("con un total de devoluciones de: ")
                  print(devolucion[2])
              print("\n")
        repetir = input("¿Desea consultar otro dato? (si/no) ")
        if repetir != "si" and repetir != "Si":
          continuar = False
      
      if rango_calif == "calificaciones malas":
        print("Los productos con un promedio (redondeado) de 1 a 2 estrellas son: \n")
        for calif in calif_malas:
          for elemento in lifestore_products:
            if calif == elemento[0]:
              print(elemento[0])
              print(elemento[1])
              for devolucion in p_calificaciones:
                if devolucion[1] == calif:
                  print("con un total de devoluciones de: ")
                  print(devolucion[2])
              print("\n")
        repetir = input("¿Desea consultar otro dato? (si/no) ")
        if repetir != "si" and repetir != "Si":
          continuar = False

    elif consulta == "4":
      print("Los productos más costoso son: ")
      for producto in mas_caros:
        for elemento in lifestore_products:
          if producto[1] == elemento[0]:
            print(elemento[0])
            print(elemento[1])
            print("con un precio de ")
            print(producto[0])
            print("\n")
      repetir = input("¿Desea consultar otro dato? (si/no) ")
      if repetir != "si" and repetir != "Si":
        continuar = False

    elif consulta == "5":
      print("Los productos más baratos son: ")
      for producto in mas_baratos:
        for elemento in lifestore_products:
          if producto[1] == elemento[0]:
            print(elemento[0])
            print(elemento[1])
            print("con un precio de ")
            print(producto[0])
            print("\n")
      repetir = input("¿Desea consultar otro dato? (si/no) ")
      if repetir != "si" and repetir != "Si":
        continuar = False

    elif consulta == "6":
      print("Los productos más buscados son: ")
      for producto in mas_buscados:
        for elemento in lifestore_products:
          if producto[1] == elemento[0]:
            print(elemento[0])
            print(elemento[1])
            print("con ")
            print(producto[0])
            print("\n")
      repetir = input("¿Desea consultar otro dato? (si/no) ")
      if repetir != "si" and repetir != "Si":
        continuar = False

    elif consulta == "7":
      print("Los productos que no registran busquedas son: ")
      for producto in no_buscados:
        for elemento in lifestore_products:
          if producto == elemento[0]:
            print(elemento[0])
            print(elemento[1])
            print("\n")
      repetir = input("¿Desea consultar otro dato? (si/no) ")
      if repetir != "si" and repetir != "Si":
        continuar = False


    elif consulta == "8":
      print("Los productos con más cantidad en stock son: ")
      for producto in mayor_stock:
        for elemento in lifestore_products:
          if producto[1] == elemento[0]:
            print(elemento[0])
            print(elemento[1])
            print("Con una cantidad de: ")
            print(producto[0])
            print("\n")
      repetir = input("¿Desea consultar otro dato? (si/no) ")
      if repetir != "si" and repetir != "Si":
        continuar = False
      

    elif consulta == "9":
      print("Los productos con menor cantidad en stock son: ")
      for producto in menor_stock:
        for elemento in lifestore_products:
          if producto[1] == elemento[0]:
            print(elemento[0])
            print(elemento[1])
            print("Con una cantidad de: ")
            print(producto[0])
            print("\n")
      repetir = input("¿Desea consultar otro dato? (si/no) ")
      if repetir != "si" and repetir != "Si":
        continuar = False

    elif consulta == "10":
      print("Presione el numero correspondiente a la opción a seleccionar")
      mes = input(" 1 para ver los ingresos por mes\n 2 para ver  el promedio de ingresos mensuales\n 3 para ver el total de ingresos anuales\n 4 para ver los 3 meses con más ventas\n 5 para ver los 3 meses con menos ventas  ")

      if mes == "1":
        print("El ingreso en Enero fue: ")
        print(ene)
        print("El ingreso en febrero fue: ")
        print(feb)
        print("El ingreso en marzo fue: ")
        print(mar)
        print("El ingreso en abril fue: ")
        print(abr)
        print("El ingreso en mayo fue: ")
        print(may)
        print("El ingreso en junio fue: ")
        print(jun)
        print("El ingreso en julio fue: ")
        print(jul)
        print("El ingreso en agosto fue: ")
        print(ago)
        print("El ingreso en septiembre fue: ")
        print(sep)
        print("El ingreso en octubre fue: ")
        print(octu)
        print("El ingreso en noviembre fue: ")
        print(nov)
        print("El ingreso en diciembre fue: ")
        print(dic)
        

      elif mes == "2":
        mes_promedio = (ene + feb + mar + abr + may + jun + jul + ago +sep + nov + dic + octu) / 12
        print("El promedio de ventas por mes es: ")
        print(mes_promedio)

      elif mes == "3":
        año_promedio = (ene + feb + mar + abr + may + jun + jul + ago +sep + nov + dic + octu)
        print("El promedio de ventas por anuales es: ")
        print(año_promedio)

      elif mes == "4":
        año.sort()
        contador = 0
        mejores_meses = []
        while contador < 3:
          mejores_meses.append(año[-contador-1][1])
          contador += 1
        print(mejores_meses)


      elif mes == "5":
        año.sort()
        contador = 0
        mejores_meses = []
        while contador < 3:
          mejores_meses.append(año[contador][1])
          contador += 1
        print(mejores_meses)

      repetir = input("¿Desea consultar otro dato? (si/no) ")
      if repetir != "si" and repetir != "Si":
        continuar = False

    elif consulta == "11":
      print("Los productos que fueron no buscados y no vendidos fueron")
      for producto in no_buscado_o_vendidos:
        for elemento in lifestore_products:
          if producto == elemento[0]:
            print(elemento[0])
            print(elemento[1])
            print("\n")

      print("Los productos que no fueron vendidos y estan entre los precios más accecibles son: ")
      for producto in no_vendidos_baratos:
        for elemento in lifestore_products:
          if producto == elemento[0]:
            print(elemento[0])
            print(elemento[1])
            print("\n")

      repetir = input("¿Desea consultar otro dato? (si/no) ")
      if repetir != "si" and repetir != "Si":
        continuar = False

    elif consulta == "12":
      print("Los productos con un gran acumulamiento en stock pero también de los más vendidos son: ")
      for producto in stock_vendidos:
        for elemento in lifestore_products:
          if producto == elemento[0]:
            print(elemento[0])
            print(elemento[1])
            print("\n")

      print("Los productos que tienen una calificación promedio excelente y hay poco stock son: ")
      for producto in stock_poco:
        for elemento in lifestore_products:
          if producto == elemento[0]:
            print(elemento[0])
            print(elemento[1])
            print("\n")

      repetir = input("¿Desea consultar otro dato? (si/no) ")
      if repetir != "si" and repetir != "Si":
        continuar = False
    
    elif consulta == "13":
      print("La cantidad de productos que están entre los más vendidos y a la vez entre los más caros son: ")
      print(len(vendidos_caros))
      # for producto in vendidos_caros:
      #   for elemento in lifestore_products:
      #     if producto == elemento[0]:
      #       print(elemento[0])a
      #       print(elemento[1])
      #       print("\n")

      print("\nLa cantidad de productos que están entre los más vendidos y no registran busquedas son: ")
      print(len(vendidos_sin_busqueda))
      

      repetir = input("¿Desea consultar otro dato? (si/no) ")
      if repetir != "si" and repetir != "Si":
        continuar = False

    else:
      print("\n Se debe  teclear el numero correspondiente a la opción a buscar \n")
