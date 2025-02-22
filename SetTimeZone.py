import subprocess

def get_current_timezone():
    """Retrieves the current time zone using tzutil."""
    try:
        result = subprocess.run(["tzutil", "/g"], capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error retrieving time zone: {e}")
        return None

def set_timezone(time_zone="Central Standard Time"):
    """Sets the machine's time zone to the specified value if not already set."""
    current_tz = get_current_timezone()
    
    if current_tz == time_zone:
        print(f"Time zone is already set to '{time_zone}'. No changes needed.")
        return
    
    try:
        subprocess.run(["tzutil", "/s", time_zone], check=True)
        print(f"Successfully set time zone to '{time_zone}'.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to set time zone: {e}")

if __name__ == "__main__":
    set_timezone()
