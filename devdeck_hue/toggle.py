import logging
import os
import phue

from devdeck_core.controls.deck_control import DeckControl


class Toggle(DeckControl):
    def __init__(self, key_no, **kwargs):
        self.__logger = logging.getLogger('devdeck')
        super().__init__(key_no, **kwargs)

    def initialize(self):
        self._bridge = phue.Bridge(self.settings['host'])
        self._bridge.connect()
        self._render_icon(self.on)

    @property
    def on(self):
        return bool(self._bridge.get_light(self.settings['light_id'], 'on'))

    @on.setter
    def on(self, value):
        self._bridge.set_light(self.settings['light_id'], 'on', value)

    def pressed(self):
        before = self.on  # not need to get the state twice [...]
        self.on = not before
        self._render_icon(not before)

    def _render_icon(self, on):
        image_suffix = 'filled' if on else 'outlined'
        with self.deck_context() as context:
            with context.renderer() as r:
                r.image(os.path.join(os.path.dirname(__file__), 'assets',
                        'lightbulb-{}.png'.format(image_suffix))).end()
