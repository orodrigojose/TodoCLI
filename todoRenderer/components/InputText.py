from rich.align import Align
from rich.console import RenderableType
from rich.panel import Panel
from rich.text import Text
from textual import events
from textual.reactive import Reactive
from textual.widget import Widget

class InputText(Widget):

    title: Reactive = Reactive("")
    content: Reactive = Reactive("")

    def __init__(self, title: str):
        super().__init__(title)
        self.title = title


    def on_key(self, event: events.Key) -> None:
        if event.key == 'ctrl+h':
            self.content = self.content[:-1]
            return
        self.content += event.key


    def validate_title(self, value) -> None:
        try:
            return value.lower()
        except (AttributeError, TypeError):
            raise AssertionError('Please insert a correct title')

    
    def render(self) -> RenderableType:
        return Panel(
            Align.left(Text(self.content, style='bold')),
            title=self.title,
            title_align='left',
            height=3,
            style='bold white'
        )

