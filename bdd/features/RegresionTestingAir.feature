#Create JohanaG at 15/12/2021

Feature: Regresion Testing Aéreos

  @use.chrome.browser
  @testing.regresiontest.es-CO.amadeus
    Scenario: Flujo Amadeus 1adt
   Given Hacer búsqueda de aéreo en catmandu OW con la aerolinea AV para ocupación 1ADT saliendo desde BOG con destino MIA con fecha de salida en 110 días
   When Esperar que la página de resultados traiga aéreos en catmandú
   When Seleccionar la primera opción con upsell
   When Esperar que la página de upsell se visualice en catmandu
   When Seleccionar la opción "mas costosa" del upsell
   When Click en botón seguir
   When Esperar la página de pasajeros
   When Esperar la validación de precios en página de pasajeros de catmandú
   When Llenar formulario de pasajeros
   When Click botón continuar en página de pasajeros
   When Esperar que se muestre la página de checkout
   When Realizar pago con método de pago "Tarjeta de crédito" en página de checkout
   #Then Validar que el precio en pagina de pasajeros sea el mismo precio que en pagina de checkout
   When Esperar y dar click en ver itinerario
   Then Validar que la reserva tenga estado confirmado
   When Ingresar a netadmin ambiente testing
   When Esperar que se muestre página de login de netadmin
   When Ingresar credenciales de login ambiente testing
   When Hacer click en el boton ingresar
   When Esperar que la pagina de Netadmin cargue
   When Ingresar itinerario y buscarlo en Netadmin
   When Hacer click en el boton cancelar y validar que el estado quede en cancelado


  @use.chrome.browser
  @testing.regresiontest.es-CO.amadeusp2p
  Scenario: Reserva de vuelo RT con AV con Amadeus con upsell preincluido crosselling seleccion de silla y asistencia
   Given Hacer búsqueda de vuelo RT en la aerolínea AV en catmandu para 1ADT saliendo de BOG con destino MIA con fecha de checkin en 104 dias y checkout en 106 dias
   When Esperar que la página de resultados traiga vuelos en catmandú
   When Seleccionar la opción de vuelo que tenga habilitado upsell de la página de resultados de catmandú
   When Esperar a que se muestre la página de detalles de vuelo en catmandú
   When Seleccionar la opción "mas costosa" del upsell
   When Click en botón seguir
   #When Obtener el valor total de pagina de detalle de vuelo en catmandu
   #When Esperar que la pagina de productos de catmandu cargue en su totalidad
   #When Hacer click en el boton comprar ahora de la pagina de aereos con crosselling de catmandu
   When Esperar la página de pasajeros
   When Esperar la validación de precios en página de pasajeros de catmandú
   When Llenar formulario de pasajeros
   Then Validar que el precio de pagina de resultados sea igual al precio de pagina de pasajeros en el flujo de air
   #When Dar click en el botón seleccionar sillas en la página de pasajeros de catmandú
   #When Esperar hasta que se muestre el mapa de sillas en la página de selección de sillas de catmandú
   #When Seleccionar sillas disponibles en la página de selección de sillas de catmandú
   #When Dar click en el botón de confirmar sillas en la página de selección de sillas de catmandú
   #When Esperar 2 segundos
   #When Dar click en el botón de confirmar precios en la página de selección de sillas de catmandú
   #When Esperar a que se muestre la pagina de pagos de NFF
   When Click botón continuar en página de pasajeros
   When Esperar que se muestre la página de checkout
   When Realizar pago con método de pago "Tarjeta de crédito" en página de checkout
   Then Validar que el precio en pagina de pasajeros sea el mismo precio que en pagina de checkout
   When Esperar y dar click en ver itinerario
   Then Validar que la reserva tenga estado confirmado
   When Ingresar a netadmin ambiente testing
   When Esperar que se muestre página de login de netadmin
   When Ingresar credenciales de login ambiente testing
   When Hacer click en el boton ingresar
   When Esperar que la pagina de Netadmin cargue
   When Ingresar itinerario y buscarlo en Netadmin
   When Hacer click en el boton cancelar y validar que el estado quede en cancelado
