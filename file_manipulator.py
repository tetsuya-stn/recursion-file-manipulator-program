import sys

def reverse(argv):
  with open(argv[2]) as inputFile:
    contents = inputFile.read()

  with open(argv[3], "w") as outputFile:
    outputFile.write(contents[::-1])

def copy(argv):
  with open(argv[2]) as inputFile:
    contents = inputFile.read()

  with open(argv[3], "w") as outputFile:
    outputFile.write(contents)

def duplicate_contents(argv):
  with open(argv[2]) as inputFile:
    contents = inputFile.read()

  with open(argv[2], "a") as outputFile:
    for i in range(int(argv[3])):
      outputFile.write(contents)

def replace_string(argv):
  with open(argv[2]) as inputFile:
    contents = inputFile.read()

  with open(argv[2], "w") as outputFile:
    outputFile.write(contents.replace(argv[3], argv[4]))

# 引数チェック
if (sys.argv[1] == "replace-string" and len(sys.argv) != 5) or (sys.argv[1] != "replace-string" and len(sys.argv) != 4):
  print("Parameters is not valid")
  sys.exit()


if sys.argv[1] == "reverse":
  reverse(sys.argv)
elif sys.argv[1] == "copy":
  copy(sys.argv)
elif sys.argv[1] == "duplicate-contents":
  duplicate_contents(sys.argv)
elif sys.argv[1] == "replace-string":
  replace_string(sys.argv)
else:
  print("Parameters is not valid")
  sys.exit()
