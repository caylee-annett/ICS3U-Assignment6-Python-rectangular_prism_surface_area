#!/usr/bin/env python3

# Created by: Caylee Annett
# Created on: May 2021
# This program calculates the surface area of a rectangular prism


def surface_area_calculation(length, width, height):
    # This function calculates the surface area

    surface_area = 2 * (length * width + length * height + width * height)

    return surface_area


def main():
    # This function gets the length, width, and height

    # Input
    print("This program calculates the surface area of a rectangular prism.")
    print("")
    length_input_string = input("Enter the length (cm): ")
    width_input_string = input("Enter the width (cm): ")
    height_input_string = input("Enter the height (cm): ")

    # Process
    while True:
        try:
            length_input_integer = int(length_input_string)

            if length_input_integer > 0:
                break
            else:
                length_input_string = input("{} is not a positive integer. "
                                            "Enter the length (cm): ".
                                            format(length_input_integer))
        except Exception:
            length_input_string = input("{} is not a valid input. Enter the "
                                        "length (cm): ".
                                        format(length_input_string))
    while True:
        try:
            width_input_integer = int(width_input_string)

            if width_input_integer > 0:
                break
            else:
                width_input_string = input("{} is not a positive integer. "
                                           "Enter the width (cm): ".
                                           format(width_input_integer))
        except Exception:
            width_input_string = input("{} is not a valid input. Enter the "
                                       "width (cm): ".
                                       format(width_input_string))
    while True:
        try:
            height_input_integer = int(height_input_string)

            if height_input_integer > 0:
                break
            else:
                height_input_string = input("{} is not a positive integer. "
                                            "Enter the height (cm): ".
                                            format(height_input_integer))
        except Exception:
            height_input_string = input("{} is not a valid input. Enter the "
                                        "height (cm): ".
                                        format(height_input_string))

    # Call functions
    calculated_surface_area = surface_area_calculation(length_input_integer,
                                                       width_input_integer,
                                                       height_input_integer)

    # Output
    print("")
    print("The surface area of a rectangular prism with dimensions {0} cm x "
          "{1} cm x {2} cm is {3} cm².".
          format(length_input_integer, width_input_integer,
                 height_input_integer, calculated_surface_area))
    print("\nDone.")


if __name__ == "__main__":
    main()
