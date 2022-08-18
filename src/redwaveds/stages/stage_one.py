from cosmicds.phases import CDSState, Stage
from cosmicds.registries import register_stage
from cosmicds.utils import load_template
from echo import CallbackProperty
from traitlets import default


# Stage state that stores information for this specific stage. Attributes here
# will be accessible in the front-end UI.
class StageState(CDSState):
    image_location = CallbackProperty()


@register_stage(story="redwave", index=0, steps=[
    "Example Step One",
    "Example Step Two"
])
class StageOne(Stage):

    @default('template')
    def _default_template(self):
        return load_template("stage_one.vue", __file__)

    @default('stage_icon')
    def _default_stage_icon(self):
        return "1i"

    @default('title')
    def _default_title(self):
        return "Example Stage One"

    @default('subtitle')
    def _default_subtitle(self):
        return "An Example Stage Implementation"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Set the stage state
        self.stage_state = StageState()
