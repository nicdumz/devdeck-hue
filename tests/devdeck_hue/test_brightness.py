import vcr
from devdeck_core.mock_deck_context import mock_context, assert_rendered
from tests.testing_utils import TestingUtils

from devdeck_hue.brightness import Increase


class TestBrightness:
    def test_simple_increase(self, bridge_ip, setup_hue):
        settings = {
            'host': bridge_ip,
            'light_id': 1,
            'step': 20,
        }
        control = Increase(0, **settings)
        with vcr.use_cassette('tests/fixtures/test_brightness/test_simple_increase.yaml',
                              before_record_response=TestingUtils.scrub_response,
                              match_on=['uri', 'method', 'body']) as cass:
            with mock_context(control) as ctx:
                control.initialize()
                assert_rendered(ctx, TestingUtils.get_filename(
                    '../devdeck_hue/assets/brightness-high.png'))
                control.pressed()
            assert cass.all_played
