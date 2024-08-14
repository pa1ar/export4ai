import os
import argparse
import sys

def parse_arguments():
  parser = argparse.ArgumentParser(description='Export files content in a folder or specific files with optional exclusion.')
  parser.add_argument('paths', nargs='+', help='Files or folders to include. Defaults to the current directory.')
  parser.add_argument('-x', '--exclude', nargs='+', help='Excluded folders or files')

  # Show help if no arguments are provided
  if len(sys.argv) == 1:
    parser.print_help(sys.stderr)
    sys.exit(1)
  
  return parser.parse_args()

def get_directory_content(paths, excluded_paths):
  excluded_paths = [os.path.abspath(p) for p in excluded_paths]  # Convert to absolute paths
  content = ""
  
  for path in paths:
    if os.path.isfile(path):
      if os.path.abspath(path) in excluded_paths:
        continue  # Skip excluded files
      # Directly read the file if it's a file
      with open(path, 'r') as f:
        file_content = f.read()
        content += f"--- FILE {path} STARTS:\n"
        content += file_content + f"--- FILE {path} ENDS.\n\n"
    elif os.path.isdir(path):
      # Traverse directory if it's a folder
      for root, dirs, files in os.walk(path):
        # Remove excluded folders from dirs
        dirs[:] = [d for d in dirs if os.path.abspath(os.path.join(root, d)) not in excluded_paths]
        for file in files:
          file_path = os.path.join(root, file)
          if os.path.abspath(file_path) in excluded_paths:
            continue  # Skip excluded files
          if file.endswith(('.txt', '.py', '.swift', '.js', '.html', '.css', '.json', '.xml', '.yaml', '.yml', '.md', '.entitlements', '.plist', '.ini', '.cfg', '.config', '.env', '.xcodeproj', '.xcworkspace', '.toml', '.editorconfig', '.csv', '.log', '.gradle', '.pom', '.gitignore', '.gitattributes', '.gitmodules', '.patch', '.test', '.spec', '.rst', '.doctest', '.php', '.jsp', '.asp', '.ejs', '.vue', '.jsx', '.tsx', '.scss', '.sass', '.less', '.sh', '.bat', '.svg')):
            with open(file_path, 'r') as f:
              file_content = f.read()
              content += f"--- FILE {file_path} STARTS:\n"
              content += file_content + f"--- FILE {file_path} ENDS.\n\n"
  return content

def main(paths, excluded_paths):
  content = get_directory_content(paths, excluded_paths)
  return content

if __name__ == "__main__":
  args = parse_arguments()
  paths = args.paths
  excluded_paths = args.exclude if args.exclude else []
  
  content = main(paths, excluded_paths)
  print("below are the current versions of the content in relevant files in the project, provided with corresponding paths:\n")
  print(content)
  print("---")
  print("reply OK and i'll continue the briefing")