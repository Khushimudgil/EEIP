from services.javascript_parser import parse_javascript_file


result = parse_javascript_file(
    "test_files/script.js"
)

print(result)