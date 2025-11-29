from django import template

register = template.Library()

@register.simple_tag
def btn_primary():
    return "inline-flex items-center justify-center px-4 py-2 bg-ctp-blue border border-transparent rounded-md font-semibold text-xs text-ctp-crust uppercase tracking-widest hover:bg-ctp-sapphire focus:outline-none focus:border-ctp-sky focus:ring focus:ring-ctp-sky active:bg-ctp-blue disabled:opacity-25 transition"

@register.simple_tag
def btn_success():
    return "inline-flex items-center justify-center px-4 py-2 bg-ctp-green border border-transparent rounded-md font-semibold text-xs text-ctp-crust uppercase tracking-widest hover:bg-ctp-teal focus:outline-none focus:border-ctp-green focus:ring focus:ring-ctp-green active:bg-ctp-green disabled:opacity-25 transition"

@register.simple_tag
def btn_danger():
    return "inline-flex items-center justify-center px-4 py-2 bg-ctp-red border border-transparent rounded-md font-semibold text-xs text-ctp-crust uppercase tracking-widest hover:bg-ctp-maroon focus:outline-none focus:border-ctp-red focus:ring focus:ring-ctp-red active:bg-ctp-red disabled:opacity-25 transition"

@register.simple_tag
def btn_warning():
    return "inline-flex items-center justify-center px-4 py-2 bg-ctp-yellow border border-transparent rounded-md font-semibold text-xs text-ctp-crust uppercase tracking-widest hover:bg-ctp-peach focus:outline-none focus:border-ctp-yellow focus:ring focus:ring-ctp-yellow active:bg-ctp-yellow disabled:opacity-25 transition"

@register.simple_tag
def btn_secondary():
    return "inline-flex items-center justify-center px-4 py-2 bg-ctp-surface1 border border-transparent rounded-md font-semibold text-xs text-ctp-text uppercase tracking-widest hover:bg-ctp-surface2 focus:outline-none focus:border-ctp-surface2 focus:ring focus:ring-ctp-surface0 active:bg-ctp-surface1 disabled:opacity-25 transition"

@register.simple_tag
def card_base():
    return "relative flex flex-col mt-6 text-ctp-text bg-ctp-surface0 shadow-sm rounded-xl w-full border border-ctp-surface1"

@register.simple_tag
def header_container():
    return "flex items-center justify-between mb-6 rounded-lg bg-ctp-surface0 p-6 shadow-sm border border-ctp-surface1"

@register.simple_tag
def header_title():
    return "text-2xl font-bold leading-none tracking-tight text-ctp-text"

@register.simple_tag
def header_mark():
    return "px-2 text-ctp-crust bg-ctp-blue rounded mr-2"

@register.simple_tag
def search_container():
    return "flex flex-col justify-start rounded-lg bg-ctp-surface0 shadow-sm border border-ctp-surface1 p-6 w-full"

@register.simple_tag
def table_container():
    return "relative overflow-x-auto shadow-sm sm:rounded-lg w-full border border-ctp-surface1 bg-ctp-surface0"

@register.simple_tag
def table_base():
    return "w-full text-sm text-left text-ctp-subtext0"

@register.simple_tag
def table_head():
    return "text-xs text-ctp-text uppercase bg-ctp-surface1 border-b border-ctp-surface2"

@register.simple_tag
def table_row():
    return "bg-ctp-surface0 border-b border-ctp-surface1 hover:bg-ctp-surface1 transition-colors"

@register.simple_tag
def input_label():
    return "block mb-2 text-sm font-medium text-ctp-text"

@register.simple_tag
def page_container():
    return "flex items-center w-full mb-6 rounded-lg bg-ctp-surface0 p-6 shadow-sm border border-ctp-surface1 gap-4 flex-wrap"

@register.simple_tag
def search_button():
    return "text-ctp-crust bg-ctp-blue hover:bg-ctp-sapphire focus:ring-4 focus:ring-ctp-sky font-medium rounded-lg text-sm px-5 py-2.5 focus:outline-none transition-colors"

@register.simple_tag
def form_container():
    return "flex flex-col justify-start rounded-lg bg-ctp-surface0 shadow-sm border border-ctp-surface1 p-6 w-full"

@register.simple_tag
def dashboard_card():
    return "flex flex-col bg-ctp-surface0 rounded-2xl shadow-sm border border-ctp-surface1 overflow-hidden w-full h-full"

@register.simple_tag
def login_container():
    return "w-full max-w-sm p-6 bg-ctp-surface0 border border-ctp-surface1 rounded-2xl shadow-md"
