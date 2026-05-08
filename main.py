from textual.app import App, ComposeResult
from textual.widgets import Footer, Static
from textual.containers import Horizontal


class EarPanel(Static):
    pass


class FCheckApp(App):
    CSS = """
    Screen {
        height: 100%;
        width: 100%;
        layers: base;
    }

    Horizontal {
        height: 1fr;
        width: 100%;
    }

    EarPanel {
        width: 1fr;
        height: 100%;
        border: round $primary;
        scrollbar-size: 0 0;
    }

    EarPanel#left {
        border-title-align: center;
    }

    EarPanel#right {
        border-title-align: center;
    }
    """

    BINDINGS = [
        ("q", "quit", "Quit"),
    ]

    def compose(self) -> ComposeResult:
        with Horizontal():
            left = EarPanel(id="left")
            left.border_title = "Left"
            yield left

            right = EarPanel(id="right")
            right.border_title = "Right"
            yield right

        yield Footer()


if __name__ == "__main__":
    FCheckApp().run()
