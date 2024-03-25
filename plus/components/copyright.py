import reflex as rx
import plus.styles.styles as styles

def copyright() -> rx.Component:
    return rx.box(
        rx.text(
            "© 2024. Diseñado y desarrollado por Matías Salas Vergara. Solicita tu página ",
            as_="span"
        ),
        rx.link(
                "aquí.",
                href="https://matiassalasvergara.com/",
                is_external=True,
                as_="span"
            ),

        text_align="center",
        bg="black",
        color="white",
        padding=styles.EMSize.SMALL.value
    )
        
    
    

