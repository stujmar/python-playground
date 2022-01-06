from contextlib import contextmanager

class Open_File():

  def __init__(self, filename, mode):
    self.filename = filename
    self.mode = mode

  def __enter__(self):
    self.file = open(self.filename, self.mode)
    return self.file

  def __exit__(self, exc_type, exc_val, traceback):
    self.file.close()


with Open_File('sample.txt', 'w') as f:
    f.write('Hello World!')

print(f.closed)

@contextmanager
def open_file(file, mode):
  try:
    f = open(file, mode)
    yield f
  finally:
    # even if we run into an exception, we want to close the file
    f.close()

# try and finally statements

with open_file('sample.txt', 'w') as f:
  f.write('Function Junction.')

print(f.closed)