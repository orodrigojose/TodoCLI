from textual.widget import Widget
from rich.console import RenderableType
from rich.layout import Layout
from rich.panel import Panel
from rich.align import Align

class PanelInfo(Widget):
    def __init__(self, infos):
        super().__init__()
        self.infos = infos


    def render(self) -> RenderableType:
        grid = Layout()

        grid.split_column(
            Layout(Panel(Align.center('[bold green]Todo information[/]')), size=4, ratio=3),
            Layout(Align.center(self.infos)),
        )

        return Panel(grid)
