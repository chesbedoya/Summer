# Create Jorge at 03/11/2021

Feature: Performance Hoteles

  @use.chrome.browser
  @preprod.regresion.es-CO.expedia
    Scenario: Flujo ExpediaRapid 1r1a
   Given Hacer búsqueda de hoteles en catmandu para ocupación 1R1A para destino iata MIA con fecha de checkin en 113 días y checkout en 115 días