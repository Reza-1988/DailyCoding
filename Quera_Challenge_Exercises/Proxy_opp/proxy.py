class Proxy:
    def __init__(self, obj: object) -> None:
        self._obj = obj
        self._last_accessed = None
        self._access_counts = {}

    def __getattr__(self, attr):

        if hasattr(self._obj, attr):

            self._access_counts[attr] = self._access_counts.get(attr, 0) + 1
            self._last_accessed = attr


            return getattr(self._obj, attr)


        raise AttributeError("No such attribute.")


    def last_accessed_attribute(self) -> str:
        if self._last_accessed is  None:
            raise Exception("No attribute was accessed.")
        return self._last_accessed

    def count_of_accesses(self, attribute_name: str) -> int:
        return self._access_counts.get(attribute_name, 0)

    def was_accessed(self, attribute_name: str) -> bool:
        if attribute_name not in self._access_counts:
            return False
        return True

