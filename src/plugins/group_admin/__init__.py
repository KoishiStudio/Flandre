from . import ban_and_whitelist
from . import broadcast
from . import config
from . import group
from . import join_and_leave
from . import mute
from . import namecard
from . import sqlite

# 接入帮助系统
__usage__ = """
概念：
    群与群组：群组是多个群的集合，群组中的群之间共享黑白名单，管理员可以在群组内的多个群间进行广播，并且群组的群之间**可以**共享一些设置
    权限：默认情况下，bot超管可以通过所有权限检查；群组中任何一个群的群管/群主都被视为整个群组的管理员，因此请勿将不受信任的群加入群组
    本插件的所有功能都至少需要群管权限才能使用
使用：
黑白名单：
    黑名单用户将会被立即从群或群组中所有群踢出，并且bot会自动拒绝其加群申请；白名单用户的申请会被直接通过，并且可以无视群名片格式检查
    拉黑： ban/封禁/踢/kick @xxx 或 ban 10001  即可以使用at或者直接提供帐号，并且可以一次提供多个（空格分隔）
    解除拉黑： pardon/解封  语法同上
    白名单： trust/whitelist/白名单/信任  语法同上
    移出白名单： nowhitelist/移出白名单/不信任 语法同上
    查看黑白名单：黑名单列表/白名单列表
广播：
    广播功能需要在群组中才能起作用
    broadcast/广播 消息内容 [-a] [-n] [-g 群号]
    其中除消息内容外均为可选参数。如果消息内容较复杂，也可以在发送命令时不发送消息内容，bot会提示你在下一条消息中提供消息内容
    如果在群聊中使用该功能，则会将消息广播到该群所属的群组
    -a At全体，如果bot不能at全体，则会发送普通消息
    -n 发送群公告，不能和 -a 一起用
    -g **仅能由超管在私聊时提供**，向指定的群组广播（如果提供群号，则会广播到那个群所属的群组）
群组：
    创建和加入： 创建群组/新群组/加入群组/join/joingroup/newgroup 群组名
    所有群的群管均可以创建群组，该群会被自动加入这个群组；如果群组名称已存在，则仅当发起者是该群组中任何一个群的管理员时才能成功加入
    退出群组： 离开群组/离开
    这会使本群离开该群组
    删除群组： delgroup/删除群组 [群组名]
    这会使该群组的所有群离开该群组。注意：只有超管能指定群组名进行删除
进群验证：
    bot并不支持交互式的进群验证，不过可以使用QQ的进群问题实现类似功能。在设置中设定好自动通过的答案即可（支持正则表达式）
群名片：
    bot可以在每个成员发言时自动检查其名片是否符合规定格式（支持正则），这个功能比较消耗资源，因此默认关闭，如有需要，可以在设置中打开“群名片提醒“
    bot也可以按照管理员的需要进行检查，语法如下：
    @bot 检查群名片 [-g] [-k]
    -g表示检查整个群组，-k表示踢出不符合规定格式的成员
    所有管理员、白名单用户均会被该检查忽略
设置：
    @bot（或私聊） 设置 设置名称 [设置的值] [-g] [-group 群号]
    设置名称：有 欢迎、离开、验证答案、群名片格式、群名片提醒
    设置的值：字面意思。
        其中欢迎、离开的值中可以包含 #username 和 #userid，会被自动替换为用户的昵称/帐号
        验证答案、群名片格式的值因为可以是正则表达式，为防止错判，会要求单独提供，请勿在发送命令时提供
        群名片提醒的值是布尔值， T、t、True、Y、y 均会被判为真，其他为假
    -g：设置整个群组的设置，不包含此参数的话则是本群的设置
    -group：设置指定群的设置，需要操作者在指定群是管理员（或者是bot超管）才能生效。私聊时必须提供该参数
    特殊：将值设为"#"的话，可以让本地设置的该项为空，同时不会应用全局设置。例如，将欢迎设为“#”后，bot在本群不会发送欢迎消息，但是在本群所属的群组中的其他群会发送群组统一设定的欢迎消息
    查询设置： 查看设置/查询设置 [群号]  需要管理员权限，会返回本群和群组的设置（如果加入了群组的话）。私聊时必须提供群号。
"""

__help_version__ = '0.0.1 (Flandre)'

__help_plugin_name__ = '群管工具'
