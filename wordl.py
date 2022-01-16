from english_words import english_words_lower_set as words

length = 6
must_contain = ''
excludes = ''
starts_with = 'endu'
ends_with = ''
in_order = ''

for word in words:
  if len(word) == 9 and word.startswith('end') and word.endswith(''):
    print(word)


class Wordl:
  def __init__(self, length, must_contain, excludes, starts_with, ends_with, in_order):
    self.length = length
    self.must_contain = must_contain
    self.excludes = excludes
    self.starts_with = starts_with
    self.ends_with = ends_with
    self.in_order = in_order


  def contains_letter(self, word):
      if len(self.must_contain) == 0:
          return True
      for letter in self.must_contain:
          if letter not in word:
              return False
      return True

  def contains_in_order(self, word):
    if len(self.in_order) == 0:
        return True
    if self.in_order in word:
      return True
    else:
      return False

  def does_not_contain_letter(self, word):
      if len(self.excludes) == 0:
          return True
      for letter in self.excludes:
          if letter in word:
              return False
      return True

  def test_word(self):
    for word in words:
        if word.startswith(starts_with) and word.endswith(ends_with) and len(word) == length and self.contains_letter(word) and self.contains_in_order(word) and self.does_not_contain_letter(word):
            print(word)

my_query = Wordl(length, must_contain, excludes, starts_with, ends_with, in_order)
# my_query.test_word()
