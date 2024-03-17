import reflex as rx
import plus.styles.styles as styles


def navbar() -> rx.Component:
    return rx.center(
        # rx.spacer(),

        rx.link(
            rx.heading(
                "Plus Studio",
                text_shadow="0px 1px 10px rgba(0,0,0,0.2)",
            ),
            href="/",
            high_contrast=True,
            underline="hover",
            color_scheme="gray",
            size="6",
        ),

        
        padding = styles.EMSize.DEFAULT.value,
        position="sticky",
        z_index="999",
        top="0",
        bg="#00a2c7",
        width="100%",
        height="100%",
        align="center",
    )


def navbar2() -> rx.Component:
    return rx.hstack(
        rx.spacer(),
        rx.hstack(
            # rx.icon(tag="add"),
            rx.image(
                src="icons/logo.png", width="6em", height="auto"
            ),
            rx.heading(
                "Plus Studio",
                color="black",
                text_shadow="0px 1px 10px rgba(0,0,0,0.2)",
                size=styles.EMSize.BIG
            ),
            # rx.box(
            #     rx.span("Plus", color="blue"),
            #     rx.span(" Studio", color="white")
            # )
        ),
        rx.spacer(),
        rx.menu(
            rx.menu_button(
                rx.icon(tag="hamburger"),
                color="black",
            ),
            rx.menu_list(
                rx.menu_item(
                    rx.link(
                        "Inicio",
                        href="#inicio",
                        # color="rgb(107,99,246)",
                    ),
                ),
                rx.menu_item(
                    rx.link(
                        "Servicios",
                        href="#servicios",
                        # color="rgb(107,99,246)",
                    ),
                ),
                rx.menu_item(
                  rx.link(
                        "Agenda",
                        href="#agenda",    
                        # color="rgb(107,99,246)",        
                    ),  
                ),
                rx.menu_item(
                  rx.link(
                        "Contácto",
                        href="#contacto",    
                        # color="rgb(107,99,246)",        
                    ),  
                ),
                rx.menu_divider(),
                rx.hstack(
                    rx.spacer(),
                    rx.icon(tag="sun"),
                    rx.color_mode_switch(),
                    rx.icon(tag="moon"),
                    rx.spacer(),
                    padding_y=styles.Size.SMALL.value
                )
            ),
        ),

        padding_x = styles.Size.DEFAULT.value,
        padding_y = styles.Size.SMALL.value,
        position="sticky",
        z_index="999",
        top="0",
        bg="#2ECCFA",
        width="100%"

    )