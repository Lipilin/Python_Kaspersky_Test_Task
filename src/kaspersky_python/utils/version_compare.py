def parse_version(version: str) -> tuple[int, ...]:
    return tuple(int(part) for part in version.split("."))


def compare_versions(first: str, second: str) -> int:
    first_parts = parse_version(first)
    second_parts = parse_version(second)
    if first_parts < second_parts:
        return -1
    if first_parts > second_parts:
        return 1
    return 0
