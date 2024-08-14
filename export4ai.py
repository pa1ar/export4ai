import os
import argparse
import sys

def parse_arguments():
  parser = argparse.ArgumentParser(description='Export files content in a folder with optional folder exclusion.')
  parser.add_argument('folders', nargs='*', default=['.'], help='Folders to include. Defaults to the current directory.')
  parser.add_argument('-x', '--exclude', nargs='+', help='Excluded folders')

  # Show help if no arguments are provided
  if len(sys.argv) == 1:
    parser.print_help(sys.stderr)
    sys.exit(1)
  
  return parser.parse_args()

def get_directory_content(folder_list, excluded_folders):
  excluded_folders = [os.path.abspath(f) for f in excluded_folders]  # Convert to absolute paths
  content = ""
  for folder_path in folder_list:
    for root, dirs, files in os.walk(folder_path):
      # Remove excluded folders from dirs
      dirs[:] = [d for d in dirs if os.path.abspath(os.path.join(root, d)) not in excluded_folders]
      for file in files:
        file_path = os.path.join(root, file)
        if any(os.path.abspath(root).startswith(excluded_folder) for excluded_folder in excluded_folders):
          continue  # Skip files in the excluded folders
        if file.endswith(('.txt', '.py', '.swift', '.js', '.html', '.css', '.json', '.xml', '.yaml', '.yml', '.md', '.entitlements', '.plist', '.ini', '.cfg', '.config', '.env', '.xcodeproj', '.xcworkspace', '.toml', '.editorconfig', '.csv', '.log', '.gradle', '.pom', '.gitignore', '.gitattributes', '.gitmodules', '.patch', '.test', '.spec', '.rst', '.doctest', '.php', '.jsp', '.asp', '.ejs', '.vue', '.jsx', '.tsx', '.scss', '.sass', '.less', '.sh', '.bat', '.svg')):
          with open(file_path, 'r') as f:
            file_content = f.read()
            content += f"--- FILE {file_path} STARTS:\n"
            content += file_content + f"--- FILE {file_path} ENDS.\n\n"
  return content

def main(list_of_folders, excluded_folders):
  content = get_directory_content(list_of_folders, excluded_folders)
  return content

if __name__ == "__main__":
  args = parse_arguments()
  included_folders = args.folders
  excluded_folders = args.exclude if args.exclude else []
  
  content = main(included_folders, excluded_folders)
  print("below are the current versions of the content in relevant files in the project, provided with corresponding paths:\n")
  print(content)
  print("---")
  print("reply OK and i'll continue the briefing")