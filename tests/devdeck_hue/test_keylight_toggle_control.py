import vcr
from devdeck_core.mock_deck_context import mock_context, assert_rendered
from tests.testing_utils import TestingUtils

from devdeck_hue.toggle import Toggle


class TestKeyLightToggleControl:
    @vcr.use_cassette('tests/fixtures/test_key_light_toggle/test_initialize_sets_icon.yaml',
                      before_record_response=TestingUtils.scrub_response)
    def test_initialize_sets_icon(self, bridge_ip, setup_hue):
        settings = {
            'host': bridge_ip,
            'light_id': 1,
        }
        control = Toggle(0, **settings)
        with mock_context(control) as ctx:
            control.initialize()
            assert_rendered(ctx, TestingUtils.get_filename(
                '../devdeck_hue/assets/lightbulb-filled.png'))

    @vcr.use_cassette('tests/fixtures/test_key_light_toggle/test_initialize_sets_icon_off.yaml',
                      before_record_response=TestingUtils.scrub_response)
    def test_initialize_sets_icon_off(self, bridge_ip, setup_hue):
        settings = {
            'host': bridge_ip,
            'light_id': 1,
        }
        control = Toggle(0, **settings)
        with mock_context(control) as ctx:
            control.initialize()
            assert_rendered(ctx, TestingUtils.get_filename(
                '../devdeck_hue/assets/lightbulb-outlined.png'))
