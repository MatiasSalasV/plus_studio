import reflex as rx
import plus.styles.styles as styles


def info_text(title: str, body: str) -> rx.Component:
    return rx.box(
        rx.text(
            title,
            font_weight="bold",
            as_="span",
            size="1",
            color_scheme="cyan"
        ),
        rx.text(
            f" {body}",
            size="1",
            as_="span",

        )
        
    )