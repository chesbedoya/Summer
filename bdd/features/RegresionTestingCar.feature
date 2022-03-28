Feature: RegresiónTest Car

  @use.chrome.browser
  @testing.regresiontest.es-CO.RentingCarz
  Scenario: Reserva de Auto con proveedor RentingCarz y pago TC
    Given Hacer búsqueda de auto en MIA con fecha desde en 60 días y fecha hasta en 62 días
    Then Esperar que la página de resultados traiga autos en catmandú
    Then Seleccionar la opción de auto 3 de la página de resultados de catmandú
    Then Esperar a que se muestre la página de detalles de auto en catmandú
    Then Hacer click en la opcion del radio button pagar ahora de la pagina de detalle en catmandu
    Then Continuar de la pagina de detalles de auto de catmandu a la pagina de pago
    Then Esperar a que se muestre la pagina de pasajeros en catmandú
    Then Llenar formulario de conductor en la página de pasajeros de catmandú
    Then Validar que el precio de pagina de resultados sea igual al precio de pagina de pasajeros en el flujo de car
    Then Dar click en el botón continuar en la página de pasajeros de catmandú
    Then Esperar que se muestre la página de checkout
    Then Realizar pago con método de pago "Tarjeta de crédito" en página de checkout
    Then Validar que el precio en pagina de pasajeros sea el mismo precio que en pagina de checkout
    Then Esperar y dar click en ver itinerario
    Then Validar que la reserva tenga estado confirmado
    Then Ingresar a netadmin ambiente testing
    Then Esperar que se muestre página de login de netadmin
    Then Ingresar credenciales de login ambiente testing
    Then Hacer click en el boton ingresar
    Then Esperar que la pagina de Netadmin cargue
    Then Ingresar itinerario y buscarlo en Netadmin
    Then Hacer click en el boton cancelar y validar que el estado quede en cancelado


  @use.chrome.browser
  @testing.regresiontest.es-CO.localiza
  Scenario: Reserva de Auto con proveedor Localiza y pago TC
    Given Hacer búsqueda de auto en MDE con fecha desde en 123 días y fecha hasta en 125 días
    Then Esperar que la página de resultados traiga autos en catmandú
    Then Seleccionar la opción de auto 2 de la página de resultados de catmandú
    Then Esperar a que se muestre la página de detalles de auto en catmandú
    Then Hacer click en la opcion del radio button pagar ahora de la pagina de detalle en catmandu
    Then Continuar de la pagina de detalles de auto de catmandu a la pagina de pago
    Then Esperar a que se muestre la pagina de pasajeros en catmandú
    Then Llenar formulario de conductor en la página de pasajeros de catmandú
    Then Validar que el precio de pagina de resultados sea igual al precio de pagina de pasajeros en el flujo de car
    Then Dar click en el botón continuar en la página de pasajeros de catmandú
    Then Esperar que se muestre la página de checkout
    Then Realizar pago con método de pago "Tarjeta de crédito" en página de checkout
    Then Validar que el precio en pagina de pasajeros sea el mismo precio que en pagina de checkout
    Then Esperar y dar click en ver itinerario
    Then Validar que la reserva tenga estado confirmado
    Then Ingresar a netadmin ambiente testing
    Then Esperar que se muestre página de login de netadmin
    Then Ingresar credenciales de login ambiente testing
    Then Hacer click en el boton ingresar
    Then Esperar que la pagina de Netadmin cargue
    Then Ingresar itinerario y buscarlo en Netadmin
    Then Hacer click en el boton cancelar y validar que el estado quede en cancelado

