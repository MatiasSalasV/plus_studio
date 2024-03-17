import reflex as rx
from plus.components.card_servicio import card_servicio
import plus.styles.styles as styles


def servicios() -> rx.Component:
    return rx.vstack(
        # title("Servicios disponibles"), 
        rx.heading(
            "Servicios disponibles",
            size="7",
            padding_y=styles.EMSize.DEFAULT.value
        ),
        rx.chakra.responsive_grid(
            card_servicio(
                "Grabación de voz",
                "Sesión de estudio de 2H donde gracias a nuestros equipos y estudio insonorizado podrás grabar.",
                "mic",
                "https://calendly.com/plus_studio/grabacion-de-voz?hide_gdpr_banner=1"
            ),
            card_servicio(
                "Trabajo de vocales",
                "Afinación y mezcla de vocales ya grabadas. Finalizando con la mastetizacion completa de tu canción.",
                "audio-lines",
                "https://calendly.com/plus_studio/tratamiento-vocal?hide_gdpr_banner=1"
            ),
            card_servicio(
                "PLUS Producción",
                "Sesión de estudio de 4H donde grabamos, editamos, afinamos, mezclamos y masterizamos tu canción. ",
                "plus",
                "https://calendly.com/plus_studio/produccion-plus?hide_gdpr_banner=1"),
            columns=[1,1,1, 3],
        ),
        # margin_bottom=styles.EMSize.BIGGER.value,
        # padding_y=styles.EMSize.DEFAULT.value,
        id="servicios",

        align="center",
        width="100%",
        # border_bottom = styles.border_bottom_color,
        padding_y = styles.EMSize.BIGGER.value,
        # id="features"

    )

 