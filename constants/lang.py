class Language:
    setGameScaleText = "---- Set Game Scale ----"
    scale10Text = "Scale 10"
    scale15Text = "Scale 15"
    setGameHardshipText = "---- Set Game Hardship ----"
    easyText = " Easy"
    mediumText = " Medium"
    hardText = " Hard"
    moreEasyText = "---- Make More Easy ----"
    showFalseBtnText = "Show Some 'False' Buttons"
    startText = "Start"
    #-------------------------------------------------------------------------------
    menuText = "Menu"
    restartText = "Restart"
    chanceText = "Chance :"
    noMoreChanceText = "No More Chance..."
    winText = "      You Win...      "
    loseText = "      You Lose...      "
    def __init__(lang) -> None:
        if lang == "fa":
            Language.setGameScaleText = "---- تنظیم اندازه پازل ----"
            Language.scale10Text = "تایی 10"
            Language.scale15Text = "تایی 15"
            Language.setGameHardshipText = "---- تنظیم درجه سختی بازی ----"
            Language.easyText = " آسون"
            Language.mediumText = " متوسط"
            Language.hardText = " سخت"
            Language.moreEasyText = "---- کمی آسون تر ----"
            Language.showFalseBtnText = "نمایش تعدادی کلید اشتباه"
            Language.startText = "شروع"
            #-------------------------------------------------------------------------------
            Language.menuText = "منو"
            Language.restartText = "دوباره"
            Language.chanceText = "شانس ها :"
            Language.noMoreChanceText = "...شانسی دیگه نمونده"
            Language.winText = "      هوورراا بردی      "
            Language.loseText = "    !!! ای بابا باختی که     "
