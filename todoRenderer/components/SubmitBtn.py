from rich.console import RenderableType
from rich.align import Align
from rich.text import Text
from rich.panel import Panel
from textual.widgets import Button
from textual.reactive import Reactive

class Submit(Button):
    
    clicked = Reactive(False)

    def __init__(self, label, color):
        super().__init__(label)
        self.color = color


    def render(self) -> RenderableType:
        renderable = Align.center(Text(str(self.label), style='bold'))
        return Panel(
            renderable,
            height=3,
            style=f'black on {self.color}'
        )


    def on_click(self) -> None:
        self.clicked = True
