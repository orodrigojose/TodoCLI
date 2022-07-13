import json, argparse, os
from sys import exit
from rich.console import Console
from todoRenderer import TodoLayout, ActionsLayout
from todoRenderer.components.PanelInfo import PanelInfo
from textual.app import App
from textual.reactive import Reactive
from textual.widgets import ScrollView

parser = argparse.ArgumentParser()
parser.add_argument('--todo', type=str)
args = parser.parse_args()

class Command:
    def __init__(self, todo=dict()):
        self.todo = todo

    
    def execute(self, command, task):
        avaliables_commands = {
            'add': self.add,
            'check': self.check,
            'uncheck': self.uncheck,
            'rm': self.remove
        }

        try:
            avaliables_commands[command](task)
            self.__update_data()
        except:
            return


    def add(self, task_name):
        if not self.__find_data(task_name):
            task = {
                'name': task_name,
                'status': 'pending'
            }

            self.todo['tasks'].append(task)


    def remove(self, task_name):
        task = self.__find_data(task_name)
        self.todo['tasks'].remove(task)

    
    def check(self, task_name):
        task = self.__find_data(task_name)
        task['status'] = 'completed'


    def uncheck(self, task_name):
        task = self.__find_data(task_name)
        task['status'] = 'pending'


    def __find_data(self, find):
        for task in self.todo['tasks']:
            if task['name'] == find:
                return task


    def __update_data(self):
        todo_file = args.todo
        with open(todo_file, 'w') as file:
            json.dump(self.todo, file, indent=2)


def load_todo_file(filename: str):
    try:
        if not filename.index('.json'):
            raise Exception('File is not a json')
        todo_file = open(filename, 'r')
        todo = json.load(todo_file)
        todo_file.close()
    except:
        todo = {
            'name': args.todo.replace(r'.*', ''),
            'tasks': []
        }
        with open(args.todo, 'w') as file:
            json.dump(todo, file, indent=2)

    return todo


def load_config(file_name: str, find: bool):
    file_path = f'{os.path.dirname(os.path.realpath(__file__))}/{file_name}'

    if find:
        file = open(file_path)
        config = json.load(file)
        file.close()

        return config

    with open(file_path, 'w') as file:
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
    

class MainApp(App):

    command = Reactive('')
    show_informations_panel = Reactive('')

    async def on_load(self) -> None:
        await self.bind(config['keymapping']['exit'], 'quit', 'Quit')
        await self.bind(config['keymapping']['panel_toggle'], 'toggle_panel', 'Toggle Panel')
    

    def watch_show_informations_panel(self, panel_status: bool) -> None:
        self.panel_informations.animate(
            'layout_offset_x',
            0 if panel_status else -40
        )


    def action_toggle_panel(self) -> None:
        self.show_informations_panel = not self.show_informations_panel


    async def render_components(self) -> None:
        self.panel_informations = PanelInfo(self.get_todo_infos())
        self.panel_informations.layout_offset_x = -40

        await self.view.dock(self.panel_informations, edge='left', size=40, z=1)
        await self.view.dock(self.actions_layout, edge='bottom', size=3)
        await self.view.dock(ScrollView(TodoLayout(todo)), edge='top')


    async def handle_button_pressed(self) -> None:
        command = self.actions_layout.command_field.content
        self.actions_layout.command_field.content = ''

        if command:
            try:
                cmd, task = command.split(' ', 1)
            except:
                cmd, task = command, 'Error'
            finally:
                Command(self.todo).execute(cmd, task)

            self.view.layout.docks.clear()
            self.view.widgets.clear()

            await self.render_components()


    def get_todo_infos(self) -> str:
        list_infos = [
            f'[{config["pallete"]["primary"]}]Todo filename: [/][bold]{args.todo}[/]',
            f'[{config["pallete"]["primary"]}]Todo name: [/][bold]{self.todo["name"]}[/]',
            f'[{config["pallete"]["primary"]}]Tasks length: [/][bold]{len(self.todo["tasks"])}[/]'
        ]

        informations = '\n'.join(list_infos)
        return informations


    async def on_mount(self) -> None:
        self.todo = todo
        self.actions_layout = ActionsLayout(config['pallete']['primary'])

        await self.render_components()


if __name__ == '__main__' and args.todo:
    try: config = load_config('config.json', True)
    except (FileNotFoundError, FileExistsError): config = load_config('config.json', False)
    todo = load_todo_file(args.todo)

    MainApp.run()
    console = Console()
    console.print('[bold green]Thanks for testing...[/]')
    exit()

from home import Home
Home.run()
