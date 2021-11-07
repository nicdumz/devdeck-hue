# DevDeck - Philips Hue integration
![CI](https://github.com/nicdumz/devdeck-hue/workflows/CI/badge.svg?branch=main)

Philips Hue light controls for [DevDeck](https://github.com/jamesridgway/devdeck).

## Installing
Simply install *DevDeck - Hue* into the same python environment that you have installed DevDeck.

    pip install devdeck-hue

You can then update your DevDeck configuration to use decks and controls from this package.

## Controls

* `toggle.Toggle`

   Can be used to toggle on/off a Philips Hue lamp.

* `brightness.Increase`

   Can be use to increase light brightness by a static amount.

* `brightness.Decrease`

   Can be use to decrease light brightness by a static amount.

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
            - name: devdeck_hue.brightness.Increase
              key: 1
              settings:
                host: 192.168.1.23
                step: 20
            - name: devdeck_hue.brightness.Decrease
              key: 1
              settings:
                host: 192.168.1.23
                step: 20
