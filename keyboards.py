# Keyboards for Telegram Adult Blocker Bot

# Admin Control Panel Keyboard
admin_keyboard = {
    'inline_keyboard': [
        [{'text': 'Statistics', 'callback_data': 'statistics'}],
        [{'text': 'Manage Users', 'callback_data': 'manage_users'}],
        [{'text': 'Settings', 'callback_data': 'settings'}]
    ]
}

# User Menu Keyboard
user_menu_keyboard = {
    'inline_keyboard': [
        [{'text': 'Help', 'callback_data': 'help'}],
        [{'text': 'Settings', 'callback_data': 'user_settings'}],
        [{'text': 'Report', 'callback_data': 'report'}]
    ]
}

# Developer Panel Keyboard
developer_panel_keyboard = {
    'inline_keyboard': [
        [{'text': 'Logs', 'callback_data': 'view_logs'}],
        [{'text': 'Configuration', 'callback_data': 'config'}]
    ]
}

# Moderation Options Keyboard
moderation_options_keyboard = {
    'inline_keyboard': [
        [{'text': 'Ban User', 'callback_data': 'ban_user'}],
        [{'text': 'Unban User', 'callback_data': 'unban_user'}],
        [{'text': 'View Reports', 'callback_data': 'view_reports'}]
    ]
}

# Confirmation Keyboard Interface
confirmation_keyboard = {
    'inline_keyboard': [
        [{'text': 'Confirm', 'callback_data': 'confirm'}],
        [{'text': 'Cancel', 'callback_data': 'cancel'}]
    ]
}

# Exporting Keyboards
keyboards = {
    'admin': admin_keyboard,
    'user_menu': user_menu_keyboard,
    'developer_panel': developer_panel_keyboard,
    'moderation': moderation_options_keyboard,
    'confirmation': confirmation_keyboard
}
