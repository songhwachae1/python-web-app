from typing import Annotated

from fastapi import APIRouter, Query, Body

from python_web_app.auth.schema import RegisterRequest, RegisterResponse

router = APIRouter(prefix="/fast-path-op", tags=["fast-path-op"])


@router.post("")
async def request_body_param_model(request: RegisterRequest):
    """
    this errors if RegisterResponse has extra="forbid" set
    not if extra="ignore"(default)
    if extra="allow", extra data is stored in the __pydantic_extra__ dict attr of the model
    """
    RegisterResponse(**request.model_dump())
    return RegisterResponse.model_validate(request)


@router.post("/json_field_as_param_with_annotated_body_embed_set_true")
async def json_field_as_param_with_annotated_body_embed_set_true(json_key: Annotated[RegisterRequest, Body(embed=True)]):
    return RegisterResponse.model_validate(json_key)


@router.get("/do_not_accept_model")
async def get_op_do_not_accept_declaring_pydantic_model_as_param(model: RegisterRequest):
    """
    GET operation does not accept a pydantic model as a parameter.
    if the param is declared to be of the type of a pydantic model,
    it will be interpreted as a request body.
    """
    return RegisterResponse.model_validate(model)

@router.get("/accept_param_model_when_annotated")
async def get_op_accept_declaring_parm_as_model_when_annotated(model: Annotated[RegisterRequest, Query()]):
    return RegisterResponse.model_validate(model)


@router.get("/declare_list_param_with_annotated_query")
async def get_accept_declaring_list_param_with_annotated_query(q: Annotated[list[str], Query()]):
    return q
