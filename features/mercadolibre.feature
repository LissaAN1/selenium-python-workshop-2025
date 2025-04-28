Feature: Busqueda mercadolibre
    Scenario: Lista de productos iphone
        Given el usuario esta en la pagina principal de mercadolibre
        When el usuario busca "iPhone 13"
        Then al menos 1 resultados deben contener la palabra "iPhone"