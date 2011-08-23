def createLevel(name, id, area, color, children=[], data={}):
    data['$area'] = area
    data['$color'] = color
    return {'name': name, 'id': id, 'data': data, 'children': children}