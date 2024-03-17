import reflex as rx 
import plus.styles.styles as styles

def link_icon(image:str,url:str, alt:str) -> rx.Component:
    return rx.link(
        rx.image(
            src=image,
            width=styles.EMSize.LARGE.value,
            height=styles.EMSize.LARGE.value,
            alt=alt
        ),
        href=url,
        is_external=True,
        # color_scheme="gray",
        padding_right="0.8em"
    )