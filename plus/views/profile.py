import reflex as rx
import datetime
from plus.components.link_icon import link_icon
import plus.styles.styles as styles
from plus.components.info_text import info_text

def profile(details=True) -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(
                # src="/logo.jpg", 
                fallback="RX", 
                size="8",
                padding = "2px",
                border="4px",
                border_color="#2ECCFA",
                box_shadow="0px 1px 10px #00a2c7",
            ),
   
            rx.vstack(
                rx.heading(
                    "Plus Studio", 
                    size="6",
                ),
                rx.link(
                    "@plus__studio", 
                    color_scheme="cyan",
                    margin_top="0px !important",
                    href="https://www.instagram.com/plus__studio/",
                    is_external=True,
                ),
                rx.hstack(
                    link_icon(
                        "icons/ig.svg",
                        "https://www.instagram.com/plus__studio/",
                        "Instagram"
                    ),
                    link_icon(
                        "icons/wa.svg",
                        "https://api.whatsapp.com/send/?phone=56937883083&text&type=phone_number&app_absent=0",
                        "WhatsApp"
                    ),
                    link_icon(
                        "icons/tt.svg",
                        "https://x.com",
                        "YouTube"
                    ),
                    spacing="1"
                ),
                align_items="start"
            ),
            padding_y=styles.EMSize.DEFAULT.value
        ),
        rx.cond(
            details,
            rx.vstack(
                rx.flex(
                    info_text(
                        f"{experience()}+",
                        "años de experiencia"
                    ),
                    rx.spacer(),
                    info_text(
                        "10.000+", "reproducciones"
                    ),
                    rx.spacer(),
                    info_text(
                        "10+", "estilos trabajados"
                    ),
                    width="100%"
                ),
                rx.text(
                    f"""
                    En Plus Studio, transformamos tu música con pasión y tecnología de punta, 
                    elevando tus canciones al siguiente nivel. Envíanos un mensaje y juntos, 
                    haremos que tu música brille como nunca antes. Estás listo para subir?
                    """,
                    text_align="justify",
                    padding_y=styles.EMSize.DEFAULT.value
                ),
                width="100%",
                spacing="2"
            )
        ),
        max_width="500px",
        width="100%",
        padding_x=styles.EMSize.DEFAULT.value,
        padding_y=styles.EMSize.BIG.value,
        spacing="2",
        margin_bottom=styles.EMSize.BIGGER.value,
        align_items="start",
        id="contacto",        
    )


def experience() -> int:
    return datetime.date.today().year - 2018