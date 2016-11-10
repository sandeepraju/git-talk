import os
import sys

comment_syntax_dict = {
  '.py': '# ',
  '.pl': '# ',
  '.rb': '# ',
  '.php': '# ',
  '.c': '// ',
  '.h': '// ',
  '.cpp': '// ',
  '.cs': '// ',
  '.go': '// ',
  '.java': '// ',
  '.js': '// ',
  '.m': '// ',
  '.mm': '// ',
  '.swift': '// ',
  '.sass': '// ',
  '.scss': '// ',
  '.lisp': '; '
}

def get_comment_syntax(filepath):
  _, extension = os.path.splitext(filepath)
  if extension in comment_syntax_dict:
    return comment_syntax_dict[extension]
  # TODO: This needs to replaced so that users can input the right inline comment 
  # syntax for unknown file types.
  return '#'

def insert_comment(filepath, line_number, comment):
  comment_syntax = get_comment_syntax(filepath)
  with open(filepath, 'r') as f:
    lines = f.readlines()
    lines.insert(line_number - 1, comment_syntax + comment + '\n')

  with open(filepath, 'w') as f:
    f.writelines(lines)

def main():
  if len(sys.argv) < 4:
    print 'USAGE:\npython insert_comment.py [file path] [line number] [comment]\n\t[file path]: path of file to insert comments into\n\t[line number]: line to insert comment before\n\t[comment]: comment to insert (wrap in quotes if multiple words)\n'
  else: 
    insert_comment(sys.argv[1], int(sys.argv[2]), sys.argv[3])

if __name__ == "__main__":
  main()
