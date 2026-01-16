"""
Time Conversion Utility
=======================
A comprehensive time converter based on the 200/60 example from the notebook.
Converts time between different units: seconds, minutes, hours, and days.
"""


def time_converter(value, from_unit, to_unit):
    """
    Convert time between different units.
    
    Args:
        value (float): The time value to convert
        from_unit (str): Source unit ('seconds', 'minutes', 'hours', 'days')
        to_unit (str): Target unit ('seconds', 'minutes', 'hours', 'days')
    
    Returns:
        float: Converted time value
    
    Example:
        >>> time_converter(200, 'minutes', 'hours')
        3.3333333333333335
    """
    conversions = {
        'seconds': 1,
        'minutes': 60,
        'hours': 3600,
        'days': 86400
    }
    
    # Validate units
    if from_unit not in conversions:
        raise ValueError(f"Invalid source unit: {from_unit}. Must be one of {list(conversions.keys())}")
    if to_unit not in conversions:
        raise ValueError(f"Invalid target unit: {to_unit}. Must be one of {list(conversions.keys())}")
    
    # Convert to seconds first, then to target unit
    seconds = value * conversions[from_unit]
    return seconds / conversions[to_unit]


def main():
    """Demonstrate time conversion examples"""
    
    print("Time Conversion Examples")
    print("=" * 40)
    
    # Example from the notebook: 200 minutes to hours
    result1 = time_converter(200, 'minutes', 'hours')
    print(f"200 minutes = {result1:.2f} hours")
    
    # Additional examples
    print(f"\nAdditional Examples:")
    print(f"90 minutes = {time_converter(90, 'minutes', 'hours'):.2f} hours")
    print(f"2.5 hours = {time_converter(2.5, 'hours', 'minutes'):.0f} minutes")
    print(f"1 day = {time_converter(1, 'days', 'hours'):.0f} hours")
    print(f"3600 seconds = {time_converter(3600, 'seconds', 'hours'):.1f} hours")
    print(f"45 minutes = {time_converter(45, 'minutes', 'seconds'):.0f} seconds")


if __name__ == "__main__":
    main()

