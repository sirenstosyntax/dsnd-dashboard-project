from .base_component import BaseComponent
from fasthtml.common import Input, Label, Div

class Radio(BaseComponent):

    def __init__(self, values, name, hx_get="", hx_target="", selected=""):
        self.values = values
        self.name = name
        self.hx_get = hx_get
        self.hx_target = hx_target
        self.selected = selected

    def build_component(self, entity_id, model):

        children = []
        for value in self.values:
            attrs = {
                "type": "radio",
                "id": value.lower(),
                "name": self.name,
                "value": value,
            }
            if self.hx_get:
                attrs["hx_get"] = self.hx_get
            if self.hx_target:
                attrs["hx_target"] = self.hx_target
            if value == model.name.title():
                attrs["checked"] = "true"

            input_child = Input(**attrs)
            label_child = Label(value, _for=value.lower())
            children.append(input_child)
            children.append(label_child)

        return children

    def outer_div(self, component):
        return Div(*component)