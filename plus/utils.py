import reflex as rx

# Común

def lang() -> rx.Component:
    return rx.script("document.documentElement.lang='es'")

preview = "https://moure.dev/preview.jpg"

_meta = [
    {"name": "og:type", "content": "website"},
    {"name": "og:image", "content": preview},
    {"name": "twitter:card", "content": "summary_large_image"},
    {"name": "twitter:site", "content": "@plus__studio"}
]

# Index

index_title = "Plus Studio "
index_description = "PRODUCCIONES MUSICALES, MENTALIDAD POSITIVA"

index_meta = [
    {"name": "og:title", "content": index_title},
    {"name": "og:description", "content": index_description},
]
index_meta.extend(_meta)