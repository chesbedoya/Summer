Feature: RegresiónTest Extras

  @use.chrome.browser
  @testing.regresiontest.es-CO.ApitudeExt
  Scenario: Reserva de Extras con proveedor ApitudeExtras y pago TC
    Given Hacer búsqueda de extras en MIA con fecha desde en 112 días y fecha hasta en 114 días y ocupacion 1RE
    When Esperar que la página de resultados traiga extras en catmandú
    When Seleccionar la opción de extra 3 de la página de resultados de extras de catmandú
    When Esperar que la pagina de extras de catmandu cargue en su totalidad
    When Ingresar cantidad mínima de pasajeros en la pagina de productos de extras de catmandu
    When Hacer click en el boton comprar ahora de la pagina de productos de extras de catmandu
    When Esperar a que se muestre la pagina de pasajeros en catmandú
    When Llenar formulario de pasajero de extras en la página de pasajeros de catmandú
    When Validar que el precio de pagina de resultados sea igual al precio de pagina de pasajeros en el flujo de extras
    When Dar click en el botón continuar en la página de pasajeros de catmandú
    When Esperar que se muestre la página de checkout
    When Realizar pago con método de pago "Tarjeta de crédito" en página de checkout
    When Validar que el precio en pagina de pasajeros sea el mismo precio que en pagina de checkout
    When Esperar y dar click en ver itinerario
    When Validar que la reserva tenga estado confirmado
    When Ingresar a netadmin ambiente testing
    When Esperar que se muestre página de login de netadmin
    When Ingresar credenciales de login ambiente testing
    When Hacer click en el boton ingresar
    When Esperar que la pagina de Netadmin cargue
    When Ingresar itinerario y buscarlo en Netadmin
    When Hacer click en el boton cancelar y validar que el estado quede en cancelado


  @use.chrome.browser
  @testing.regresiontest.es-CO.Omnitours
  Scenario: Reserva de Extras con proveedor ExtrasNetsuite y pago TC
    Given Hacer búsqueda de extras en BOG con fecha desde en 68 días y fecha hasta en 70 días y ocupacion 1RE
    When Esperar que la página de resultados traiga extras en catmandú
    When Seleccionar la opción de extra 3 de la página de resultados de extras de catmandú
    When Esperar que la pagina de productos de catmandu cargue en su totalidad
    When Ingresar cantidad mínima de pasajeros en la pagina de productos de extras de catmandu
    When Hacer click en el boton comprar ahora de la pagina de productos de extras de catmandu
    When Esperar a que se muestre la pagina de pasajeros en catmandú
    When Llenar formulario de pasajero de extras en la página de pasajeros de catmandú
    When Validar que el precio de pagina de resultados sea igual al precio de pagina de pasajeros en el flujo de extras
    When Dar click en el botón continuar en la página de pasajeros de catmandú
    When Esperar que se muestre la página de checkout
    When Realizar pago con método de pago "Tarjeta de crédito" en página de checkout
    When Validar que el precio en pagina de pasajeros sea el mismo precio que en pagina de checkout
    When Esperar y dar click en ver itinerario
    When Validar que la reserva tenga estado confirmado
    When Ingresar a netadmin ambiente testing
    When Esperar que se muestre página de login de netadmin
    When Ingresar credenciales de login ambiente testing
    When Hacer click en el boton ingresar
    When Esperar que la pagina de Netadmin cargue
    When Ingresar itinerario y buscarlo en Netadmin
    When Hacer click en el boton cancelar y validar que el estado quede en cancelado


  @use.chrome.browser
  @testing.regresiontest.es-CO.Civitatis
  Scenario: Reserva de Extras con proveedor Civitatis y pago TC
    Given Hacer búsqueda de extras en MAD con fecha desde en 90 días y fecha hasta en 92 días y ocupacion 1RE
    When Esperar que la página de resultados traiga extras en catmandú
    When Seleccionar la opción de extra 4 de la página de resultados de extras de catmandú
    When Esperar que la pagina de productos de catmandu cargue en su totalidad
    When Ingresar cantidad mínima de pasajeros en la pagina de productos de extras de catmandu
    When Hacer click en el boton comprar ahora de la pagina de productos de extras de catmandu
    When Esperar a que se muestre la pagina de pasajeros en catmandú
    When Llenar formulario de pasajero de extras en la página de pasajeros de catmandú
    When Validar que el precio de pagina de resultados sea igual al precio de pagina de pasajeros en el flujo de extras
    When Dar click en el botón continuar en la página de pasajeros de catmandú
    When Esperar que se muestre la página de checkout
    When Realizar pago con método de pago "Tarjeta de crédito" en página de checkout
    When Validar que el precio en pagina de pasajeros sea el mismo precio que en pagina de checkout
    When Esperar y dar click en ver itinerario
    When Validar que la reserva tenga estado confirmado
    When Ingresar a netadmin ambiente testing
    When Esperar que se muestre página de login de netadmin
    When Ingresar credenciales de login ambiente testing
    When Hacer click en el boton ingresar
    When Esperar que la pagina de Netadmin cargue
    When Ingresar itinerario y buscarlo en Netadmin
    When Hacer click en el boton cancelar y validar que el estado quede en cancelado

