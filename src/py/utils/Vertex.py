class Vertex:
    def __init__(self, val):
        self.val = val


def vals_to_vets(vals: list) -> list[Vertex]:
    return [Vertex(val) for val in vals]


def vets_to_vals(vets: list[Vertex]) -> list:
    return [vet.val for vet in vets]
