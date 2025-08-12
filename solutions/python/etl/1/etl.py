def transform(legacy_data):
    result = {}
    for key,data in legacy_data.items():
        result.update(dict.fromkeys([data.lower() for data in data],key))
    return result
