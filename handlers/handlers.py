from aiogram.filters import Command
from aiogram.types import Message
from aiogram import Dispatcher
from keyboards.keyboards import main_menu_kb, tournament_menu_kb, tournament1_matches_kb, tournament2_matches_kb, teams_menu_kb, back_to_main_menu_kb
from data.data import (
    match_info_russia_slovakia,
    match_info_ukraine_belarus,
    match_info_luxembourg_poland,
    match_info_turkey_bulgaria,
    team_info_russia,
    team_info_slovakia,
    team_info_ukraine,
    team_info_belarus,
    team_info_luxembourg,
    team_info_poland,
    team_info_turkey,
    team_info_bulgaria
)

def register_handlers(dp: Dispatcher):
    @dp.message(Command("start"))
    async def start_command(message: Message):
        await message.answer("Добро пожаловать! Выберите опцию:", reply_markup=main_menu_kb)

    @dp.message(lambda message: message.text == "Вернуться в главное меню")
    async def back_to_main_menu(message: Message):
        await message.answer("Вы вернулись в главное меню.", reply_markup=main_menu_kb)

    @dp.callback_query(lambda c: c.data == "tournaments")
    async def show_tournaments(callback_query):
        await callback_query.message.answer("Выберите турнир:", reply_markup=tournament_menu_kb)
        await callback_query.answer()
        await callback_query.message.delete()  # Удаляем сообщение с инлайн-кнопками

    @dp.callback_query(lambda c: c.data == "teams")
    async def show_teams(callback_query):
        await callback_query.message.answer("Выберите команду:", reply_markup=teams_menu_kb)
        await callback_query.answer()
        await callback_query.message.delete()  # Удаляем сообщение с инлайн-кнопками

    @dp.callback_query(lambda c: c.data == "tournament1")
    async def show_tournament1_matches(callback_query):
        await callback_query.message.answer("Выберите матч:", reply_markup=tournament1_matches_kb)
        await callback_query.answer()
        await callback_query.message.delete()  # Удаляем сообщение с инлайн-кнопками

    @dp.callback_query(lambda c: c.data == "match_russia_slovakia")
    async def show_match_info_russia_slovakia(callback_query):
        await callback_query.message.answer(match_info_russia_slovakia, parse_mode='Markdown', reply_markup=back_to_main_menu_kb)
        await callback_query.answer()
        await callback_query.message.delete()  # Удаляем сообщение с инлайн-кнопками

    @dp.callback_query(lambda c: c.data == "match_ukraine_belarus")
    async def show_match_info_ukraine_belarus(callback_query):
        await callback_query.message.answer(match_info_ukraine_belarus, parse_mode='Markdown', reply_markup=back_to_main_menu_kb)
        await callback_query.answer()
        await callback_query.message.delete()  # Удаляем сообщение с инлайн-кнопками

    @dp.callback_query(lambda c: c.data == "tournament2")
    async def show_tournament2_matches(callback_query):
        await callback_query.message.answer("Выберите матч:", reply_markup=tournament2_matches_kb)
        await callback_query.answer()
        await callback_query.message.delete()  # Удаляем сообщение с инлайн-кнопками

    @dp.callback_query(lambda c: c.data == "match_luxembourg_poland")
    async def show_match_info_luxembourg_poland(callback_query):
        await callback_query.message.answer(match_info_luxembourg_poland, parse_mode='Markdown', reply_markup=back_to_main_menu_kb)
        await callback_query.answer()
        await callback_query.message.delete()  # Удаляем сообщение с инлайн-кнопками

    @dp.callback_query(lambda c: c.data == "match_turkey_bulgaria")
    async def show_match_info_turkey_bulgaria(callback_query):
        await callback_query.message.answer(match_info_turkey_bulgaria, parse_mode='Markdown', reply_markup=back_to_main_menu_kb)
        await callback_query.answer()
        await callback_query.message.delete()  # Удаляем сообщение с инлайн-кнопками

    @dp.callback_query(lambda c: c.data == "team_russia")
    async def show_team_info_russia(callback_query):
        await callback_query.message.answer(team_info_russia, parse_mode='Markdown', reply_markup=back_to_main_menu_kb)
        await callback_query.answer()
        await callback_query.message.delete()  # Удаляем сообщение с инлайн-кнопками

    @dp.callback_query(lambda c: c.data == "team_slovakia")
    async def show_team_info_slovakia(callback_query):
        await callback_query.message.answer(team_info_slovakia, parse_mode='Markdown', reply_markup=back_to_main_menu_kb)
        await callback_query.answer()
        await callback_query.message.delete()  # Удаляем сообщение с инлайн-кнопками

    @dp.callback_query(lambda c: c.data == "team_ukraine")
    async def show_team_info_ukraine(callback_query):
        await callback_query.message.answer(team_info_ukraine, parse_mode='Markdown', reply_markup=back_to_main_menu_kb)
        await callback_query.answer()
        await callback_query.message.delete()  # Удаляем сообщение с инлайн-кнопками

    @dp.callback_query(lambda c: c.data == "team_belarus")
    async def show_team_info_belarus(callback_query):
        await callback_query.message.answer(team_info_belarus, parse_mode='Markdown', reply_markup=back_to_main_menu_kb)
        await callback_query.answer()
        await callback_query.message.delete()  # Удаляем сообщение с инлайн-кнопками

    @dp.callback_query(lambda c: c.data == "team_luxembourg")
    async def show_team_info_luxembourg(callback_query):
        await callback_query.message.answer(team_info_luxembourg, parse_mode='Markdown', reply_markup=back_to_main_menu_kb)
        await callback_query.answer()
        await callback_query.message.delete()  # Удаляем сообщение с инлайн-кнопками

    @dp.callback_query(lambda c: c.data == "team_poland")
    async def show_team_info_poland(callback_query):
        await callback_query.message.answer(team_info_poland, parse_mode='Markdown', reply_markup=back_to_main_menu_kb)
        await callback_query.answer()
        await callback_query.message.delete()  # Удаляем сообщение с инлайн-кнопками

    @dp.callback_query(lambda c: c.data == "team_turkey")
    async def show_team_info_turkey(callback_query):
        await callback_query.message.answer(team_info_turkey, parse_mode='Markdown', reply_markup=back_to_main_menu_kb)
        await callback_query.answer()
        await callback_query.message.delete()  # Удаляем сообщение с инлайн-кнопками

    @dp.callback_query(lambda c: c.data == "team_bulgaria")
    async def show_team_info_bulgaria(callback_query):
        await callback_query.message.answer(team_info_bulgaria, parse_mode='Markdown', reply_markup=back_to_main_menu_kb)
        await callback_query.answer()
        await callback_query.message.delete()  # Удаляем сообщение с инлайн-кнопками

    @dp.callback_query(lambda c: c.data == "main_menu")
    async def back_to_main_menu(callback_query):
        await callback_query.message.answer("Вы вернулись в главное меню.", reply_markup=main_menu_kb)
        await callback_query.answer()
        await callback_query.message.delete()  # Удаляем сообщение с инлайн-кнопками

