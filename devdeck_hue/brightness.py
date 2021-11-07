import abc
import logging
import os
import phue

from devdeck_core.controls.deck_control import DeckControl


class _BrightnessBase(abc.ABC, DeckControl):
    def __init__(self, key_no, **kwargs):
        self.__logger = logging.getLogger('devdeck')
        super().__init__(key_no, **kwargs)

    @property
    @abc.abstractmethod
    def image_file(self):
        'Image file to render. Relative path to assets directory.'
        ...

    def initialize(self):
        self._bridge = phue.Bridge(self.settings['host'])
        self._bridge.connect()
        with self.deck_context() as context:
            with context.renderer() as r:
                r.image(os.path.join(os.path.dirname(__file__), 'assets', self.image_file)).end()

    @property
    def brightness(self):
        return self._bridge.get_light(self.settings['light_id'], 'bri')

    @brightness.setter
    def brightness(self, value):
        if not 0 <= value <= 255:
            raise ValueError('Valid brightness values are between 0 and 255 inclusive.')
        return self._bridge.set_light(self.settings['light_id'], 'bri', value)


class Increase(_BrightnessBase):
    @property
    def image_file(self):
        return 'brightness-high.png'

    def pressed(self):
        self.brightness = min(255, self.brightness + self.settings['step'])


class Decrease(_BrightnessBase):
    @property
    def image_file(self):
        return 'brightness-low.png'

    def pressed(self):
        self.brightness = max(0, self.brightness - self.settings['step'])