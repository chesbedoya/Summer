#Create JohanaG at 15/12/2021

Feature: Regresion Testing Hoteles

  @use.chrome.browser
  @testing.regresiontest.es-CO.expedia
     Scenario: Flujo ExpediaRapid 1r1a
   Given Hacer búsqueda de hoteles en catmandu para ocupación 1R1A para destino iata MIA con fecha de checkin en 118 días y checkout en 120 días
    Then Esperar que la página de resultados traiga hoteles en catmandú
    Then Quitar filtro de solo hoteles con imagenes
    Then Seleccionar la opción 1 del hotel 1 de la página de resultados de catmandú
    Then Esperar la página de pasajeros
    Then Esperar la validación de precios en página de pasajeros de catmandú
    Then Llenar formulario de pasajeros
    Then Validar que el precio en la pagina de hoteles sea el mismo precio que en pagina de pasajeros
    Then Click botón continuar en página de pasajeros
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
  @testing.regresiontest.es-CO.expedia
    Scenario: Flujo ExpediaRapid 1r2a
   Given Hacer búsqueda de hoteles en catmandu para ocupación 1R2A para destino iata CTG con fecha de checkin en 113 días y checkout en 115 días
    Then Esperar que la página de resultados traiga hoteles en catmandú
    Then Seleccionar la opción 1 del hotel 1 de la página de resultados de catmandú
    Then Esperar la página de pasajeros
    Then Esperar la validación de precios en página de pasajeros de catmandú
    Then Llenar formulario de pasajeros
    Then Click botón continuar en página de pasajeros
    Then Esperar que se muestre la página de checkout
    Then Realizar pago con método de pago "Tarjeta de crédito" en página de checkout
    Then Esperar y dar click en ver itinerario


