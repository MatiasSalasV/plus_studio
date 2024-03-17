import reflex as rx
import plus.utils as utils
from plus.components.navbar import navbar
from plus.components.copyright import copyright
from plus.views.header import header
from plus.views.servicios import servicios
from plus.views.profile import profile


import plus.styles.styles as styles

@rx.page(
    # route="/",
    title=utils.index_title,
    description=utils.index_description,
    meta=utils.index_meta,
)
def index() -> rx.Component:
    return rx.box(
        utils.lang(),
        navbar(),
        rx.vstack(
            header(),
        ),
        rx.center(
            rx.vstack(
                servicios(),                
                max_width = styles.MAX_WIDTH,
            ),

        ),
        rx.center(
            profile(),
        ),
        copyright()
    )



# <Theme appearance="dark" accentColor="cyan" grayColor="sand" panelBackground="solid" radius="full">

app = rx.App(
    theme=rx.theme(
        appearance="dark",
        accentColor="cyan",
        # grayColor="sand",
        radius="full",
        panelBackground="solid"
    )
)
app.add_page(index)
