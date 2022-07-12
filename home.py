import json
from sys import exit
from rich.layout import Layout
from rich.panel import Panel
from rich.console import RenderableType, Console
from rich.align import Align
from textual.app import App
from textual.widget import Widget

ascii_banner = '''

    sdSS_SSSSSSbs  
    YSSS~S%SSSSSP  
         S&S               __      ________    ____
         S&S    ____  ____/ /___  / ____/ /   /  _/
         S*S   / __ \/ __  / __ \/ /   / /    / /  
         S*S  / /_/ / /_/ / /_/ / /___/ /____/ /   
         S*S  \____/\____/\____/\____/_____/___/   
         S*S       
         SP        
         Y         

'''

def load_config(file_name: str, find: bool):
    if find:
        file = open(file_name)
        config = json.load(file)
        file.close()

        return config

    with open(file_name, 'w') as file:
        config = {
            "keymapping": {
                "exit": "ctrl+q",
                "panel_toggle": "ctrl+o"
            },
            "pallete": {
                "primary": "blue"
            }
        }

        json.dump(config, file, indent=2)
        return config


class Banner(Widget):
    def render(self) -> RenderableType:
        config_infos = [
            f'[{config["pallete"]["primary"]}][*] Exit key:[/] {config["keymapping"]["exit"]}',
            f'[{config["pallete"]["primary"]}][*] Toggle Panel key:[/] {config["keymapping"]["panel_toggle"]}',
            f'[{config["pallete"]["primary"]}][*] Primary color:[/] {config["pallete"]["primary"]}'
        ]

        grid = Layout()
        grid.split_column(
            Layout(
                Align.center(ascii_banner),
            ),
            Layout(
                Align.center('\n'.join(config_infos)),
                size=4
            ),
            Layout(Panel(
                Align.center('[bold red]Please inform a todo file[/]'),
                border_style=config['pallete']['primary']),
                size=3
            )
        )

        return Panel(grid, border_style=config['pallete']['primary'])


class Home(App):
    async def on_load(self):
        await self.bind(config['keymapping']['exit'], 'quit', 'Quit')
    

    async def on_mount(self):
        await self.view.dock(Banner())


if __name__ != '__main__':
    try:
        config = load_config('config.json', True)
    except (FileNotFoundError, FileExistsError):
        config = load_config('config.json', False)

    Home.run()
    console = Console()
    console.print('[bold red]Please inform todo file. Example "python3 main.py --todo <todo file>.json"[/]')
    exit()
