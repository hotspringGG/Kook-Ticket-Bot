# Kook-Ticket-Bot
## Forked from https://github.com/musnows/Kook-Ticket-Bot

![commit](https://img.shields.io/github/last-commit/hotspringGG/Kook-Ticket-Bot) [![khl server](https://www.kaiheila.cn/api/v3/badge/guild?guild_id=3986996654014459&style=0)](https://kook.top/gpbTwZ)

A ticket bot for KOOK, **自托管**表单/工单系统机器人

工作流程
* 当用户B点击卡片消息的按钮后，创建一个只有用户B可见的文字频道
* Bot会自动在该临时频道发送一条消息，并`@用户B` 和处理表单的 `@管理员`
* 当处理完毕后，点击`关闭`按钮，Bot会删除该文字频道
* 文字频道删除后，Bot会给预先`设置好的log频道`和`开启ticket的用户`发送一条记录信息，并在服务器后端保存该ticket的聊天记录；
* 管理员可以使用`/tkcm`命令，指定ticket编号对该工单发表评论

附加功能
* 通过表情回应给用户添加对应角色
* 设置Bot动态 `游戏/音乐`
