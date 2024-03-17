import reflex as rx
import plus.styles.styles as styles

def header() -> rx.Component:
    return rx.vstack(
        rx.box(
            rx.text(
                "Make it ",
                as_="span",
                size="6",
                font_weight="light",
            ),
            rx.text(
                " Plus",
                as_="span",
                font_weight="bold",
                size="6",
                text_shadow="0px 1px 10px rgba(46, 204, 250, 0.5)",
            ),
        ),
        rx.box(
            rx.text(
                "Mejora la calidad de tus canciones, vive la experiencia",
                as_="span",
                size="4"
            ),
            rx.text(
                " PLUS",
                font_weight="bold",
                as_="span",
                size="4",
                text_shadow="0px 1px 10px rgba(46, 204, 250, 0.5)",
            ),
            padding_x=styles.EMSize.DEFAULT.value,
            padding_y=styles.EMSize.SMALL.value,
           
        ),
        rx.link(
            rx.button(
                "Agenda tu sesión", 
                box_shadow="0px 1px 10px rgba(46, 204, 250, 0.5)",
                color_scheme="cyan"
            ),
            href="#servicios",
            padding_y = styles.EMSize.DEFAULT.value,
            
        ),
        height= "80vh",
        width="100%",
        style={
            "justify_content":"center",
            "align_items":"center",
            "text_align":"center",
            "background-image": "url('/header.svg')",  # Reemplaza 'ruta/al/svg.svg' con la ruta real de tu SVG
            "background-size": "cover",
            "background-position": "center",
        },
        id="inicio"
    )