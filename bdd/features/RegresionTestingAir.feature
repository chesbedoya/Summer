#Create JohanaG at 15/12/2021

Feature: Regresion Testing Aéreos

  @use.chrome.browser
  @testing.regresiontest.es-CO.amadeus
    Scenario: Flujo Amadeus 1adt
   Given Hacer búsqueda de aéreo en catmandu OW con la aerolinea AV para ocupación 1ADT saliendo desde BOG con destino MIA con fecha de salida en 110 días
   Then Esperar que la página de resultados traiga aéreos en catmandú
   Then Seleccionar la primera opción con upsell
   Then Esperar que la página de upsell se visualice en catmandu
   Then Seleccionar la opción "mas costosa" del upsell
   Then Click en botón seguir
   Then Esperar la página de pasajeros
   Then Esperar la validación de precios en página de pasajeros de catmandú
   Then Llenar formulario de pasajeros
   Then Click botón continuar en página de pasajeros
   Then Esperar que se muestre la página de checkout
   Then Realizar pago con método de pago "Tarjeta de crédito" en página de checkout
   Then Esperar y dar click en ver itinerario
   Then Validar que la reserva tenga estado confirmado
   Then Ingresar a netadmin ambiente testing
   Then Esperar que se muestre página de login de netadmin
   Then Ingresar credenciales de login ambiente testing
   Then Hacer click en el boton ingresar
   Then Ingresar itinerario en el buscador
   Then Hacer click en el boton search
   Then Hacer click en el boton cancelar



   @use.chrome.browser
  @testing.regresiontest.es-CO.amadeus
    Scenario: Flujo Amadeus 2adt 1chd
   Given Hacer búsqueda de aéreo en catmandu RT con la aerolinea AV para ocupación 2ADT 1 CHD saliendo desde BOG con destino MIA con fecha de salida en 110 días
   Then Esperar que la página de resultados traiga aéreos en catmandú
   Then Seleccionar la primera opción con upsell