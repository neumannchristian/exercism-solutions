def proverb(*args, **kwargs):
    if not args:
        return []
    mod = kwargs["qualifier"] + " " if kwargs["qualifier"] else ""

    result = []
    for idx in range(0, len(args) - 1):
        if len(args) > 1:
            result.append(f"For want of a {args[idx]} the {args[idx + 1]} was lost.")
    result.append(f"And all for the want of a {mod}{args[0]}.")
    return result
