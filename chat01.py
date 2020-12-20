import dataclasses

@dataclasses.dataclass
class Message:
    # メッセージ情報

    # ユーザ名
    username: str
    # メッセージ
    message: str
