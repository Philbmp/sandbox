import subprocess

def get_current_timezone():
    """
    Retrieves the current time zone using the 'tzutil /g' command.
    
    Returns:
        str: The current time zone as a string, or None if an error occurs.
    """
    try:
        # Run the command to get the current time zone
        result = subprocess.run(["tzutil", "/g"], capture_output=True, text=True, check=True)
        return result.stdout.strip()  # Remove any leading/trailing whitespace
    except subprocess.CalledProcessError as e:
        print(f"Error retrieving time zone: {e}")
        return None  # Return None if the command fails

def set_timezone(time_zone="Central Standard Time"):
    """
    Sets the machine's time zone to the specified value if it is not already set.
    
    Args:
        time_zone (str): The time zone to set (default is 'Central Standard Time').
    """
    # Get the current time zone
    current_tz = get_current_timezone()
    
    # Check if the current time zone is already set correctly
    if current_tz == time_zone:
        print(f"Time zone is already set to '{time_zone}'. No changes needed.")
        return  # Exit the function since no change is required
    
    try:
        # Run the command to set the new time zone
        subprocess.run(["tzutil", "/s", time_zone], check=True)
        print(f"Successfully set time zone to '{time_zone}'.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to set time zone: {e}")

if __name__ == "__main__":
    """
    Main execution block.
    Calls set_timezone() to ensure the machine is set to Central Standard Time.
    """
    set_timezone()  # Set the machine's time zone to CST by default
