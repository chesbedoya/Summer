Feature: RegresiónTest Extras

  @use.chrome.browser
  @testing.regresiontest.es-CO.ApitudeExt
  Scenario: Reserva de Extras con proveedor ApitudeExtras y pago TC
    Given Hacer búsqueda de extras en MIA con fecha desde en 112 días y fecha hasta en 114 días y ocupacion 1RE
    Then Esperar que la página de resultados traiga extras en catmandú
    Then Seleccionar la opción de extra 4 de la página de resultados de extras de catmandú
    Then Esperar que la pagina de productos de catmandu cargue en su totalidad
    Then Ingresar cantidad mínima de pasajeros en la pagina de productos de extras de catmandu
    Then Hacer click en el boton comprar ahora de la pagina de productos de extras de catmandu
    Then Esperar a que se muestre la pagina de pasajeros en catmandú
    Then Llenar formulario de pasajero de extras en la página de pasajeros de catmandú
    Then Validar que el precio de pagina de resultados sea igual al precio de pagina de pasajeros en el flujo de extras
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
  @testing.regresiontest.es-CO.Omnitours
  Scenario: Reserva de Extras con proveedor ExtrasNetsuite y pago TC
    Given Hacer búsqueda de extras en BOG con fecha desde en 68 días y fecha hasta en 70 días y ocupacion 1RE
    Then Esperar que la página de resultados traiga extras en catmandú
    Then Seleccionar la opción de extra 3 de la página de resultados de extras de catmandú
    Then Esperar que la pagina de productos de catmandu cargue en su totalidad
    Then Ingresar cantidad mínima de pasajeros en la pagina de productos de extras de catmandu
    Then Hacer click en el boton comprar ahora de la pagina de productos de extras de catmandu
    Then Esperar a que se muestre la pagina de pasajeros en catmandú
    Then Llenar formulario de pasajero de extras en la página de pasajeros de catmandú
    Then Validar que el precio de pagina de resultados sea igual al precio de pagina de pasajeros en el flujo de extras
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
  @testing.regresiontest.es-CO.Civitatis
  Scenario: Reserva de Extras con proveedor Civitatis y pago TC
    Given Hacer búsqueda de extras en MAD con fecha desde en 90 días y fecha hasta en 92 días y ocupacion 1RE
    Then Esperar que la página de resultados traiga extras en catmandú
    Then Seleccionar la opción de extra 4 de la página de resultados de extras de catmandú
    Then Esperar que la pagina de productos de catmandu cargue en su totalidad
    Then Ingresar cantidad mínima de pasajeros en la pagina de productos de extras de catmandu
    Then Hacer click en el boton comprar ahora de la pagina de productos de extras de catmandu
    Then Esperar a que se muestre la pagina de pasajeros en catmandú
    Then Llenar formulario de pasajero de extras en la página de pasajeros de catmandú
    Then Validar que el precio de pagina de resultados sea igual al precio de pagina de pasajeros en el flujo de extras
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

