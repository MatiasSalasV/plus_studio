import reflex as rx
import plus.styles.styles as styles

def card_servicio(title: str, text: str, icon:str,url:str) -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.icon(
                tag=f"{icon}", 
                size=70,
                margin_bottom = styles.EMSize.DEFAULT.value,
            ),
            rx.heading(title),
            rx.text(
                f"{text}",
                margin_y = styles.EMSize.SMALL.value,
            ),
            rx.link(
                rx.button(
                    "Agenda ahora",
                    rx.icon(tag="arrow-right"),
                    variant="soft",
                    color_scheme="cyan",
                    margin_top=styles.EMSize.DEFAULT.value,
                    _hover={
                        "cursor": "pointer",
                        "box_shadow":"0px 1px 10px rgba(46, 204, 250, 0.5)",
                    },
                ),
                href=f"{url}",
                is_external=True
            ),
            align_items="start",  # Alinea verticalmente los elementos
            justify_content="center",  # Centra los elementos horizontalmente
            height="100%",
            width="100%",
        ),
            
        _hover={
            "bg": "#1E2D34",
        },  

        margin_bottom=styles.EMSize.SMALL.value,
        border_radius="10px",
        box_shadow="0px 1px 10px rgba(46, 204, 250, 0.5)",
        padding=styles.EMSize.BIG.value,
        margin=styles.EMSize.DEFAULT.value,
    )


