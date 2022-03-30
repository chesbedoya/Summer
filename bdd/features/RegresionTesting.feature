#Create JohanaG at 15/12/2021

Feature: Regresion Testing Hoteles

  @use.chrome.browser
  @testing.regresiontest.es-CO.expedia
  Scenario: Flujo ExpediaRapid 1r1a
   Given Hacer búsqueda de hoteles en catmandu para ocupación 1R1A para destino iata MIA con fecha de checkin en 118 días y checkout en 120 días
    When Esperar que la página de resultados traiga hoteles en catmandú
    When Seleccionar la opción 1 del hotel 1 de la página de resultados de catmandú
    When Esperar la página de pasajeros
    When Esperar la validación de precios en página de pasajeros de catmandú
    When Llenar formulario de pasajeros
    When Click botón continuar en página de pasajeros
    When Esperar que se muestre la página de checkout
    When Realizar pago con método de pago "Tarjeta de crédito" en página de checkout
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
  @testing.regresiontest.es-CO.expedia
  Scenario: Flujo ExpediaRapid 1r2a1c
   Given Hacer búsqueda de hoteles en catmandu para ocupación 1R2A1C para destino iata MIA con fecha de checkin en 118 días y checkout en 120 días
    When Esperar que la página de resultados traiga hoteles en catmandú
    When Quitar filtro de solo hoteles con imagenes
    When Esperar 4 segundos
    When Seleccionar la opción 1 del hotel 1 de la página de resultados de catmandú
    When Esperar la página de pasajeros
    When Esperar la validación de precios en página de pasajeros de catmandú
    When Llenar formulario de pasajeros
    When Validar que el precio en la pagina de hoteles sea el mismo precio que en pagina de pasajeros
    When Click botón continuar en página de pasajeros
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


