from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

# Главное меню
main_menu_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Турниры", callback_data="tournaments"),
         InlineKeyboardButton(text="Команды", callback_data="teams")],
        [InlineKeyboardButton(text="Помощь", callback_data="help")]
    ]
)

# Меню турниров
tournament_menu_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Турнир1", callback_data="tournament1"),
         InlineKeyboardButton(text="Турнир2", callback_data="tournament2")],
        [InlineKeyboardButton(text="Назад в главное меню", callback_data="main_menu")]
    ]
)

# Меню матчей для Турнир1
tournament1_matches_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Матч Россия-Словакия", callback_data="match_russia_slovakia"),
         InlineKeyboardButton(text="Матч Украина-Белорусь", callback_data="match_ukraine_belarus")],
        [InlineKeyboardButton(text="Назад в главное меню", callback_data="main_menu")]
    ]
)

# Меню матчей для Турнир2
tournament2_matches_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Матч Люксенбург-Польша", callback_data="match_luxembourg_poland"),
         InlineKeyboardButton(text="Матч Турция-Болгария", callback_data="match_turkey_bulgaria")],
        [InlineKeyboardButton(text="Назад в главное меню", callback_data="main_menu")]
    ]
)

# Меню команд
teams_menu_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Команда России", callback_data="team_russia"),
         InlineKeyboardButton(text="Команда Словакии", callback_data="team_slovakia")],
        [InlineKeyboardButton(text="Команда Украины", callback_data="team_ukraine"),
         InlineKeyboardButton(text="Команда Белоруси", callback_data="team_belarus")],
        [InlineKeyboardButton(text="Команда Люксенбурга", callback_data="team_luxembourg"),
         InlineKeyboardButton(text="Команда Польши", callback_data="team_poland")],
        [InlineKeyboardButton(text="Команда Турции", callback_data="team_turkey"),
         InlineKeyboardButton(text="Команда Болгарии", callback_data="team_bulgaria")],
        [InlineKeyboardButton(text="Назад в главное меню", callback_data="main_menu")]
    ]
)

# Обычная клавиатура с кнопкой "Вернуться в главное меню"
back_to_main_menu_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Вернуться в главное меню")]
    ],
    resize_keyboard=True
)
