from fastapi import APIRouter

import define
from action.siyuan import SiyuanAction
from define import NotebookMethod, BlockMethod
from entity.siyuan import Record
from interface import ISiyuan
from model.api_model import APIResponse, NoteBookModel, SiyuanIconModel, SiyuanDatabaseModel, SiyuanBlocksModel

router = APIRouter()


@router.post("/notebooks")
async def siyuan_notebooks(request: NoteBookModel):
    match request.method:
        case NotebookMethod.下载指定文档图片:
            await SiyuanAction.download_single_notebook_resource(request.notebook_id)
            Record().save()
            return APIResponse({"result": True, "message": define.IMsg.OK})
        case NotebookMethod.上传指定文档图片:
            await SiyuanAction.upload_single_notebook_resource(request.notebook_id, endpoint=request.endpoint)
            Record().save()
            return APIResponse(data={"result": True, "message": define.IMsg.OK})
        case NotebookMethod.加载文件信息:
            await ISiyuan.get_resource_record(keep_ori=True)
            return APIResponse(data={"result": True, "message": define.IMsg.OK})
        case _:
            return APIResponse(data={"result": False, "message": define.IMsg.BAN})


@router.post("/blocks")
async def siyuan_blocks(request: SiyuanBlocksModel):
    match request.method:
        case BlockMethod.上传指定块资源:
            await SiyuanAction.upload_block_resource(request.notebook_id, request.block_id, endpoint=request.endpoint)
            return APIResponse(data={"result": True, "message": define.IMsg.OK})
        case _:
            return APIResponse(data={"result": False, "message": define.IMsg.BAN})


@router.post("/database")
async def siyuan_database(request: SiyuanDatabaseModel):
    match request.method:
        case NotebookMethod.上传指定数据库中的所有资源文件:
            await SiyuanAction.upload_database_resource(request.database_id, endpoint=request.endpoint)
            Record().save()
            return APIResponse(data={"result": True, "message": define.IMsg.OK})
        case _:
            return APIResponse(data={"result": False, "message": define.IMsg.BAN})


@router.post("/icon")
async def siyuan_icon(request: SiyuanIconModel):
    await SiyuanAction.MultiReplaceDocIcon(request.old_icon, request.new_icon, hpath=request.hpath, toast=request.toast)
    return APIResponse(data={"result": True, "message": define.IMsg.OK})
