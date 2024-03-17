import reflex as rx
import plus.styles.styles as styles


def navbar() -> rx.Component:
    return rx.center(
        # rx.spacer(),

        rx.link(
            rx.heading(
                "+Plus Studio",
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
