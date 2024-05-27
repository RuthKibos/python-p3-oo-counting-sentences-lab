#!/usr/bin/env python3
class MyString:
    def __init__(self, value=''):
        if not isinstance(value, str):
            raise ValueError("The value must be a string.")
        self._value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if isinstance(new_value, str):
            self._value = new_value
        else:
            raise ValueError("The value must be a string.")

    def is_sentence(self):
        return self.value.endswith('.')

    def is_question(self):
        return self.value.endswith('?')

    def is_exclamation(self):
        return self.value.endswith('!')

    def count_sentences(self):
        import re
        sentences = re.split(r'[.!?]', self.value)
        non_empty_sentences = [s.strip() for s in sentences if s.strip()]
        return len(non_empty_sentences)