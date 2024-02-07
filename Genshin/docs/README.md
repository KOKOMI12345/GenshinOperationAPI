# 原神角色操作 API

欢迎使用原神角色操作 API！你可以使用我提供的 NaviaControllers.py 文件来控制娜维娅角色。当然，你也可以直接调用 CharacterOperation API 来操控游戏角色。这个实现基于模拟用户操作的 ctype 模块。

## 示例

下面是一个示例代码，演示如何使用 API 进行攻击操作：

```python
from NaviaConntrolers import navia
navia.Fire(method="TurnedATK", times=7, change=1, timeWait=1)
```

这个代码将会使用 Navia 进行攻击操作

## 调用参数说明

- `method`: 攻击方式，可以是 "TurnedATK"  "Normal" "Charged" "Skill" "Quickly"
- `times`: 每次攻击的间隔,如果攻击模式为Charged,这个就代表蓄力时间(max:5)
- `change`: 攻击次数
- `timeWait`: 每次攻击完成后下一次攻击的时间间隔

请根据需要修改以上参数，以实现你想要的操作.

## 注意事项

在运行 API 之前，确保具备管理员权限（如果需要模拟键盘或鼠标操作）。

如果你在使用过程中遇到任何问题或有改进建议，请随时联系我们，我们会尽快回复并解决问题。

感谢使用原神角色操作 API，祝你游戏愉快！

## 彩蛋

如果你不会用的话,可以运行一下start.py捏~

- `路径`: .\Genshin\OperationAPI\start.py

## 更新日志

- 2024/2/8 添加了录制鼠标键盘操作的功能,同时支持回放
- 2024/2/8 修复了部分bug
