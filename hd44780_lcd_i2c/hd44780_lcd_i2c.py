# SPDX-FileCopyrightText: 2023 Nimrod Abing
#
# SPDX-License-Identifier: MIT

"""
`hd44780_lcd_i2c.hd44780_lcd_i2c`
====================================================

Module for HD44780 character LCDs with a PCF8574 I2C backpack.

* Author: Nimrod Abing

Implementation Notes
--------------------

**Hardware:**

* `MakerLab 16x2 LCD Display MLE00659
  <https://www.makerlab-electronics.com/products/16x2-lcd-display-i2c-black-on-green>`_
* `MakerLab 20x4 LCD Display MLE00661
  <https://www.makerlab-electronics.com/products/20x4-lcd-display-i2c-black-on-green>`_

**Software and Dependencies:**

* Adafruit CircuitPython firmware for the supported boards:
  https://circuitpython.org/downloads

* Adafruit's Bus Device library:
  https://github.com/adafruit/Adafruit_CircuitPython_BusDevice

* Adafruit's PCF8574 library:
  https://github.com/adafruit/Adafruit_PCF8574

* Adafruit's Character LCD library:
  https://github.com/adafruit/Adafruit_CircuitPython_CharLCD

"""
import busio

from adafruit_pcf8574 import PCF8574
from adafruit_character_lcd.character_lcd import Character_LCD_Mono


# I2C pins
RS_PIN = 0
EN_PIN = 2
DB4_PIN = 4
DB5_PIN = 5
DB6_PIN = 6
DB7_PIN = 7
BACKLIGHT_PIN = 3


class HD44780_LCD_I2C(Character_LCD_Mono):
    # pylint: disable=too-few-public-methods, too-many-arguments
    """HD44780 Character LCD connected to a PCF8574 I2C/SPI backpack using its I2C
    connection. This is a subclass of `Character_LCD_Mono` and implements all the
    same functions and functionality.

    To use, import and initialise as follows:

    .. code-block:: python

        import board
        from hd44780_lcd_i2c.hd44780_lcd_i2c import HD44780_LCD_I2C as Character_LCD_I2C

        i2c = board.I2C()  # uses board.SCL and board.SDA
        lcd = Character_LCD_I2C(i2c, 16, 2)
    """

    def __init__(
        self,
        i2c: busio.I2C,
        columns: int,
        lines: int,
        address: int = 0x27,
        backlight_inverted: bool = False,
    ) -> None:
        pcf = PCF8574(i2c, address)

        super().__init__(
            rs=pcf.get_pin(RS_PIN),
            en=pcf.get_pin(EN_PIN),
            db4=pcf.get_pin(DB4_PIN),
            db5=pcf.get_pin(DB5_PIN),
            db6=pcf.get_pin(DB6_PIN),
            db7=pcf.get_pin(DB7_PIN),
            columns=columns,
            lines=lines,
            backlight_pin=pcf.get_pin(BACKLIGHT_PIN),
            backlight_inverted=backlight_inverted,
        )
