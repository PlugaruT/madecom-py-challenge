from collections import UserDict


class PermaDict(UserDict):
    def __init__(self, *args, **kwargs):
        self._silent = kwargs.get('silent', False)
        super().__init__(*args, **kwargs)
        
    def __setitem__(self, key, value):
        if key in self.data and not self._silent:
            raise KeyError(f"'{key}' already in dictionary.")
        super().__setitem__(key, value)
    
    def force_set(self, key, value):
        self.data[key] = value