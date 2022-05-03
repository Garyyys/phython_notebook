def create_class_point(name, base, attrs): #<- простейший метакласс с помощью функции
    attrs.update({'MAX_COORD': 100, 'MIN_COORD': 0}) #<- задает атрибуты поумолчанию
    return type(name, base, attrs)


class Point(metaclass=create_class_point):
    def get_coord(self):
        return (0, 0)

pt = Point()
print(pt.MAX_COORD)
print(pt.get_coord())