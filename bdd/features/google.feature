#language:pt

Funcionalidade: Página de Google

    Scenario: Verificar título da página após pesquisa
        Dado que accesso a página de Google
        Quando realizo uma pesquisa
        E pesquisa e realiza
        Então o titulo da página deve ser validado