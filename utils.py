def parse_time(time_str):
    try:
        return datetime.strptime(time_str, "%H:%M").time()
    except ValueError:
        raise ValueError("Некорректный формат времени")
