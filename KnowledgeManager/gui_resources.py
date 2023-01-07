
COLOR_EXTRA_LIGHT_GRAY = "#EEEEEE"
COLOR_LIGHT_GRAY = "#DDDDDD"
COLOR_GRAY = "#CCCCCC"
COLOR_DARK_GRAY = "#AAAAAA"
COLOR_EXTRA_DARK_GRAY = "#888888"

COLOR_MAJOR_ACTION_BUTTON = "#88DDDD" # Turquoise
COLOR_MINOR_ACTION_BUTTON = COLOR_GRAY
COLOR_BADGE_BUTTON = "#77FF77" # Green


# Frames and panels

STANDARD_FRAME_ATTRIBUTES = {
    "borderwidth":5,
    "relief":"ridge",
    "bg":COLOR_LIGHT_GRAY
}

STANDARD_PANEL_ATTRIBUTES = {
    "borderwidth":3, 
    "padx":5, 
    "pady":5, 
    "relief":"groove", 
    "bg":COLOR_LIGHT_GRAY
}

INNER_PANEL_ATTRIBUTES = {
    "bg":COLOR_LIGHT_GRAY
}


# Labels

STANDARD_LABEL_ATTRIBUTES = {
    "padx":10, 
    "pady":3, 
    "font":("SegoeUI", 12, "bold")
}

SMALL_LABEL_ATTRIBUTES = {
    "padx":3,
    "pady":3,
    "font":("SegoeUI", 10),
    "bg":COLOR_LIGHT_GRAY
}


# Buttons

PRIMARY_BUTTON_ATTRIBUTES_LARGE = {
    "borderwidth":3, 
    "padx":10, 
    "pady":3, 
    "relief":"groove", 
    "bg":COLOR_MAJOR_ACTION_BUTTON,
    "font":("SegoeUI", 12, "bold")
}

PRIMARY_BUTTON_ATTRIBUTES_MEDIUM = {
    "borderwidth":2, 
    "padx":5, 
    "pady":2, 
    "relief":"groove", 
    "bg":COLOR_MAJOR_ACTION_BUTTON,
    "font":("SegoeUI", 10, "bold")
}

SECONDARY_BUTTON_ATTRIBUTES = {
    "borderwidth":2,
    "padx":5,
    "pady":2,
    "relief":"groove",
    "bg":COLOR_MINOR_ACTION_BUTTON,
    "font":("SegoeUI", 10, "bold")
}

BADGE_BUTTON_ATTRIBUTES = {
    "borderwidth":1,
    "padx":3,
    "pady":1,
    "relief":"flat",
    "bg":COLOR_BADGE_BUTTON,
    "font":("SegoeUI", 8, "bold")
}

