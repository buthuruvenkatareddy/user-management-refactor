def validate_user_input(data, required_fields):
    errors = []

    if not data or not isinstance(data, dict):
        return ["Invalid or missing JSON data"]

    for field in required_fields:
        if field not in data or not str(data[field]).strip():
            errors.append(f"{field} is required.")
    
    return errors
