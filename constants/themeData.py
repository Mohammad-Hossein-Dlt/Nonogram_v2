class ThemeData():
    theme = "Light"

    controls = "#E5989B"
    buttonColor = "white"
    disableButtonText = "white"
    guidesLabels = "#EADDCA"
    
    columnGuideColor = "#FF00FB"
    rowGuideColor = "#FF8400"

    falsebuttonColor = "#FF0000"
    truebuttonColor = "#00FF3B"

    gameChanceColor = "#F3E5AB"
    providedByColor = "#CF9FFF"
    def __init__(theme) -> None:
        if theme == "Dark" :

            ThemeData.buttonColor = "#6D6875"

            ThemeData.disableButtonText = "white"
            ThemeData.guidesLabels = "#B5838D"

            ThemeData.columnGuideColor = "#073B4C"
            ThemeData.rowGuideColor = "#073B4C"


            ThemeData.falsebuttonColor = "#230903"
            ThemeData.truebuttonColor = "#74B3CE"

            ThemeData.gameChanceColor = "#9A8C98"
            ThemeData.providedByColor = "#C9ADA7"
