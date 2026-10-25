from kaspersky_python.database.tables.Vulnerability import Vulnerability


def format_vulnerabilities_data(vulnerabilities: list[Vulnerability]) -> None:
    for vulnerability in vulnerabilities:
        print(f"KLA: {vulnerability.kla_id}")
        print(f"Описание: {vulnerability.description}")
        print(f"Дата публикации: {vulnerability.publish_date}")
        print(f"Уязвима с версии: {vulnerability.start_vuln_version}")
        print(f"Исправлена в версии: {vulnerability.fixed_version}")
        print()


def format_last_stable_version(version: str) -> None:
    print(f"Последняя стабильная версия: {version}")
