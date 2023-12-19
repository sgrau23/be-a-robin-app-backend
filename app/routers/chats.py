from fastapi import APIRouter

router = APIRouter()


@router.post("/chats/createConversation")
async def create_conversation():
    ...


@router.post("/chats/submitMessage")
async def submit_message():
    ...


@router.post("/chats/readConversationMessages")
async def read_conversation_message():
    ...
