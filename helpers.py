import owlready2


def superclasses(ent):
    for cls in ent.is_a:
        yield cls
        yield from superclasses(cls)


def is_subclass(subclass, superclass):
    if isinstance(superclass, owlready2.Or):
        return any(is_subclass(subclass, c) for c in superclass.Classes)
    if isinstance(superclass, owlready2.And):
        return all(is_subclass(subclass, c) for c in superclass.Classes)
    return superclass in superclasses(subclass)


def textual(ent):
    if hasattr(ent, 'label'):
        return ent.label[0]
    else:
        return str(ent)


def foodon() -> owlready2.Ontology:
    url = 'https://github.com/FoodOntology/foodon/blob/master/foodon.owl?raw=true'
    owlready2.onto_path.append('ontologies/')
    return owlready2.get_ontology(url).load()
