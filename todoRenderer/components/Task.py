from rich.panel import Panel
from textual.widget import Widget

class Task(Widget):
    def __init__(self, name, status):
        super().__init__()
        self.name = name
        self.status = status


    def render(self) -> Panel:
        status_styles = {
            'pending': '[cyan]pending[/]',
            'completed': '[bold green]completed[/]'
        }
        return Panel(f'[grey]name:[/] [bold blue]{self.name}[/]\t [grey]status:[/] {status_styles[self.status]}')
