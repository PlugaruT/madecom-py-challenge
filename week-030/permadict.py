from collections import UserDict


class PermaDict(UserDict):
    def __init__(self, *args, **kwargs):
        self._silent = kwargs.pop('silent', False)
        self._force = False
        super().__init__(*args, **kwargs)
        
    def __setitem__(self, key, value):
        if key in self.data and not self._force:
            if self._silent:
                return
            raise KeyError(f"'{key}' already in dictionary.")
        super().__setitem__(key, value)
        
    def update(self, *args, **kwargs):
        self._force = kwargs.pop('force', False)
        super().update(*args, **kwargs)
    
    def force_set(self, key, value):
        self.data[key] = value