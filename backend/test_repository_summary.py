from services.repository_summary_service import (
    generate_repository_summary,
    format_repository_summary
)

summary = generate_repository_summary(
    "test_repo"
)

formatted_summary = format_repository_summary(
    summary
)

print(formatted_summary)