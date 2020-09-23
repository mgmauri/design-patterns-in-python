class FieldBuilder:
    """Nohting"""

    def __init__(self, field_name, value):
        self.field_name = field_name
        self.value = value

    def __str__(self):
        return 'self.{} = {}'.format(self.field_name, self.value)


class ClassBuilder:
    """Nothing to comment"""

    def __init__(self, class_name):
        self.class_name = class_name
        self.fields = list()

    def __str__(self):
        lines = ['class {}:'.format(self.class_name)]
        if not self.fields:
            lines.append('  pass')
        else:
            lines.append('    def __init__(self):')
            for field in self.fields:
                lines.append('\t{}'.format(field))
        return '\n'.join(lines)


class CodeBuilder:
    """Nothing to comment"""

    def __init__(self, class_name):
        self._class = ClassBuilder(class_name)

    def add_field(self, field_name, value):
        self._class.fields.append(FieldBuilder(field_name, value))
        return self

    def __str__(self):
        return self._class.__str__()
