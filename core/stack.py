def aoi2panels(data):
    panels = data
    return panels


class Stack:
    def __init__(self, par_namelist):
        self.par_namelist = par_namelist
        self.stack = dict(zip(par_namelist, [0] * len(par_namelist)))
        self.actual = dict(zip(par_namelist, [0] * len(par_namelist)))
        self.bias = dict(zip(par_namelist, [0] * len(par_namelist)))

    def get(self, data):
        tag, data = data
        if tag == 'aoi':
            for panel in data:
                self.stack[panel] = self.actual[panel]
        elif tag == 'par':
            self.actual.update(data)

    def get_bias(self):
        diff_dict = {key: self.stack[key] - self.actual[key] for key in self.par_namelist}
        return diff_dict
