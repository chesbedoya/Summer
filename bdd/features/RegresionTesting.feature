#Create JohanaG at 15/12/2021

Feature: Regresion Testing Hoteles

  @use.chrome.browser
  @testing.regresiontest.es-CO.expedia
    Scenario: Flujo ExpediaRapid 1r1a
   Given Hacer búsqueda de hoteles en catmandu para ocupación 1R1A para destino iata MIA con fecha de checkin en 113 días y checkout en 115 días
    Then Esperar que la página de resultados traiga hoteles en catmandú
    Then Seleccionar la opción 1 del hotel 1 de la página de resultados de catmandú
    Then Esperar la página de pasajeros
    Then Esperar la validación de precios en página de pasajeros de catmandú
    Then Llenar formulario de pasajeros