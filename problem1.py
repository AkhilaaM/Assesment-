class VersionControl:
    def _init_(self):
        self.base_version = None
        self.deltas = []

    def add_version(self, content):
        if self.base_version is None:
            self.base_version = content
        else:
            delta = self._generate_delta(self.base_version, content)
            self.deltas.append(delta)

    def _generate_delta(self, base, new):
        delta = []
        for i in range(min(len(base), len(new))):
            if base[i] != new[i]:
                delta.append((i, new[i]))
        if len(new) > len(base):
            delta.extend([(i, new[i]) for i in range(len(base), len(new))])
        return delta

    def get_version(self, version_number):
        if version_number == 0:
            return self.base_version
        content = list(self.base_version)
        for delta in self.deltas[:version_number]:
            for index, value in delta:
                if index < len(content):
                    content[index] = value
                else:
                    content.append(value)
        return ''.join(content) 
# Example usage
vc = VersionControl()
vc.add_version("Hello world!")
vc.add_version("Hello world!!")
vc.add_version("Hello world!!!")
print(vc.get_version(0))  # Base version
print(vc.get_version(1))  # First version with deltas
print(vc.get_version(2))  # Second version with deltas


