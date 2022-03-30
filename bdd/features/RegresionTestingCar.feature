Feature: RegresiónTest Car

  @use.chrome.browser
  @testing.regresiontest.es-CO.RentingCarz
  Scenario: Reserva de Auto con proveedor RentingCarz y pago TC
    Given Hacer búsqueda de auto en MIA con fecha desde en 60 días y fecha hasta en 62 días
    When Esperar que la página de resultados traiga autos en catmandú
    When Seleccionar la opción de auto 3 de la página de resultados de catmandú
    When Esperar a que se muestre la página de detalles de auto en catmandú
    When Hacer click en la opcion del radio button pagar ahora de la pagina de detalle en catmandu
    When Continuar de la pagina de detalles de auto de catmandu a la pagina de pago
    When Esperar a que se muestre la pagina de pasajeros en catmandú
    When Llenar formulario de conductor en la página de pasajeros de catmandú
    Then Validar que el precio de pagina de resultados sea igual al precio de pagina de pasajeros en el flujo de car
    When Dar click en el botón continuar en la página de pasajeros de catmandú
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


  @use.chrome.browser
  @testing.regresiontest.es-CO.localiza
  Scenario: Reserva de Auto con proveedor Localiza y pago TC
    Given Hacer búsqueda de auto en MDE con fecha desde en 123 días y fecha hasta en 125 días
    When Esperar que la página de resultados traiga autos en catmandú
    When Seleccionar la opción de auto 2 de la página de resultados de catmandú
    When Esperar a que se muestre la página de detalles de auto en catmandú
    When Hacer click en la opcion del radio button pagar ahora de la pagina de detalle en catmandu
    When Continuar de la pagina de detalles de auto de catmandu a la pagina de pago
    When Esperar a que se muestre la pagina de pasajeros en catmandú
    When Llenar formulario de conductor en la página de pasajeros de catmandú
    Then Validar que el precio de pagina de resultados sea igual al precio de pagina de pasajeros en el flujo de car
    When Dar click en el botón continuar en la página de pasajeros de catmandú
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

