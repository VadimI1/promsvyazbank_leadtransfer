from django.forms import CharField
from pydantic import BaseModel, field_validator, Field, AliasPath

class SkorozvonCall(BaseModel):

    name: str = Field(validation_alias=AliasPath("lead_name"), default="")
    phone: str = Field(validation_alias=AliasPath("lead_phones"), default="")
    inn: str = Field(validation_alias=AliasPath("lead_inn"), default="")
    city: str = Field(validation_alias=AliasPath("lead_city"), default="")
    email: str = Field(validation_alias=AliasPath("lead_emails"), default="qwer1@yandex.ru")
    comment: str = Field(validation_alias=AliasPath("lead_comment"), default="")
    scenario_id: int = Field(validation_alias=AliasPath("call_scenario_id"), default="")
