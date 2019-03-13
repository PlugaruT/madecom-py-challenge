from collections.abc import Mapping

class PermaDict(Mapping):
    def __init__(self, *args, **kwargs):
        self._data = dict(*args, **kwargs)
    def __getitem__(self, key):
        return self._data[key]
    
    def __iter__(self):
        return iter(self._data)
    
    def __len__(self):
        return len(self._data)
        
    def __setitem__(self, key, value):
        if key in self._data:
            raise KeyError(f"'{key}' already in dictionary.")
        self._data[key] = value
    
    def update(self, **kwargs):
        self.__setitem__(**kwargs)
    
    def force_set(self, key, value):
        self._data[key] = value