from textual.widget import Widget
from textual.views import GridView
from rich.console import group, RenderableType
from rich.panel import Panel
from rich.align import Align
from rich.layout import Layout
from .components.Task import Task


class TodoLayout(Widget):
    def __init__(self, todo, *args):
        super().__init__(*args)
        self.todo = todo

    def render(self) -> RenderableType:
        grid = Layout()
        grid.split_column(
            Layout(Panel(Align.center('[bold]Tasks avaliables[/]')), size=4, ratio=3),
            Layout(Panel(self.load_tasks())),
        )

        return (grid)


    @group()
    def load_tasks(self):
        for task_data in self.todo['tasks']:
            yield Task(task_data['name'], task_data['status'])


