# DevDeck - Philips Hue integration

![CI](https://github.com/nicdumz/devdeck-hue/workflows/CI/badge.svg?branch=main)

Philips Hue light controls for [DevDeck](https://github.com/jamesridgway/devdeck).

## Installing

Simply install _DevDeck - Hue_ into the same python environment that you have installed DevDeck.

    pip install devdeck-hue

You can then update your DevDeck configuration to use decks and controls from this package.

## Controls

- `toggle.Toggle`

  Can be used to toggle on/off a Philips Hue lamp.

- `brightness.Increase`

  Can be use to increase light brightness by a static amount.

- `brightness.Decrease`

  Can be use to decrease light brightness by a static amount.

## One-time setup

The `phue` module which is used under the hood requires a one-time pairing with
the Hue bridge, once. Easiest way to do this is:

```
python3 -m phue --host 192.168.1.42
```

Where `--host` is the IP of the Hue bridge.

## Configuration

Example configuration:

    decks:
      - serial_number: ABC123
        name: devdeck.decks.single_page_deck_controller.SinglePageDeckController
        settings:
          controls:
            - name: devdeck_hue.toggle.Toggle
              key: 0
              settings:
                host: 192.168.1.23
                light_id: 4
              - name: devdeck_hue.brightness.Increase
                key: 1
              settings:
                host: 192.168.1.23
                light_id: 4
                step: 20
            - name: devdeck_hue.brightness.Decrease
              key: 1
              settings:
                host: 192.168.1.23
                light_id: 4
                step: 20

`light_id` is the light ID from the hue bridge. A simply way to list connected
lights by id is to run the following Python snippet:

```
python3 -c 'import phue; b=phue.Bridge(); b.connect(); print(b.get_light_objects(mode="id"))'
```
