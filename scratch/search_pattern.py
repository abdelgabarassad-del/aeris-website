import sys

def search_pattern(pattern, file_path='dashboard.html'):
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            for idx, line in enumerate(f, 1):
                if pattern.lower() in line.lower():
                    # Safely encode and decode to the terminal's preferred encoding
                    safe_line = line.encode(sys.stdout.encoding, errors='replace').decode(sys.stdout.encoding)
                    print(f"{idx}: {safe_line.strip()}")
    except Exception as e:
        print(f"Error reading file: {e}")

if __name__ == '__main__':
    if len(sys.argv) > 2:
        search_pattern(sys.argv[1], sys.argv[2])
    elif len(sys.argv) > 1:
        search_pattern(sys.argv[1])
    else:
        print("Please provide a search pattern.")
