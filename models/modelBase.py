from pydantic import BaseModel


class ModelBase(BaseModel):
    def updated_copy(self, update_values: dict):
        updated_values = self.dict() | update_values
        return self.__class__(**updated_values)

    def get_relationship_fields(self) -> set[str]:
        relationship_fields = set()
        properties = self.schema().get('properties')

        for key, value in properties.items():
            if value.get('$ref'):
                field_value = getattr(self, key)
                result = issubclass(field_value.__class__, (ModelBase, BaseModel))

                if result:
                    relationship_fields.add(key)
        return relationship_fields

    @classmethod
    def from_model(cls, model: BaseModel):
        return cls(**model.dict())

    @classmethod
    def get_models_from_query(cls, query):
        return [cls.from_orm(entity) for entity in query]

    class Config(object):
        orm_mode = True
        validate_assignment = True
