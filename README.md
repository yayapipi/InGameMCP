![%E8%9E%A2%E5%B9%95%E6%93%B7%E5%8F%96%E7%95%AB%E9%9D%A2_2025-10-05_172613.png](https://storage.googleapis.com/dashboard-51ba6.appspot.com/0187f40317b38859b4e48fa43bc74ce8.png?GoogleAccessId=firebase-adminsdk-jd298%40dashboard-51ba6.iam.gserviceaccount.com&Expires=16725225600&Signature=QMhLhj4n0ssrNMD%2FmmrXJXx9AuB00W5NwiY5EWU4gp7g2MM%2BTVJkw0ZXhHpyQcl5uzH6paMCJF%2FpwhAj2N8g6w5GtMqQobf%2BFfizPd3ugzSZaPE4nx%2BDj60YGJXXXZKfdZEr72i4%2F%2BZiCvEoZZcL0SB62pBsuBuI81nn9U95frysze9fCbRY6t4zFvX%2BnrzwTUzhV8QMlHiR2wLKs7%2BWCPzJE2fHLWGN72PsbV05XNI7nezEtYiDCGyt%2BDrrYQWVfNw%2FoQpPu%2F2oToLn7s0kv7Y3JnEy52xwRQbC1Jn%2BmioZJIyGWkr6Cg5BHWrjY%2BekMR7ZKEEAqnHaM9lAEFr5rg%3D%3D)

[20251005-1009-47.7816913.mp4](https://prod-files-secure.s3.us-west-2.amazonaws.com/595010d7-414b-4824-894d-bffa456d64a3/39d0964b-8130-456e-96aa-77c8796ddd9a/20251005-1009-47.7816913.mp4?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46627S3WAWU%2F20251005%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251005T103721Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHt4AjWnBCBcPGEy8ehwcg5NFZAuUv8kTZWsDNDE%2BQhpAiBxMyH58kjzcbpScicXW1cwpcV1wwY5H1yKbFNlwVbcbCr%2FAwhvEAAaDDYzNzQyMzE4MzgwNSIMXCl%2FRHBT7BXI6O2sKtwDEP9DOgPo4RuFT5al8hEE0bNmg1RTgykcdxcEFtG%2B%2BWnKti4zeVxQWYuL34j7kXAPEJIhLZnKaqdTVs3Ef44aJYVv7Axh%2FGFv%2FRQsRokT8IlpnEhb3QAdAZDTJRc3Hw42tXtIrvmXwxBAFUwQ3icHAvqbbLZyRkw9IDSMOOhxUu%2FYB6hWAXdpCgUEXMTHo4vq6ze3yMXLiYDhe%2FDdPv5Np4zv%2BOw96ZSq1iQQjZfh1u0dr4Wb6p2yKxVw7wa5rg95nxWJaXK%2BkH6nqPVGZC3DD2tuEyDgKcPkYy0jkkiKQgFhZCJwrj7CFwbTz2dg4qsPX7AgqNeR7qo4ph%2FTkO%2FcMOm0B9SH0dUX87n6CP7QcRQVBP0Iz5fguQ6vD72Ftn1HvxXp88XhmOaxKR6UZKdK%2FE2P9%2FK9IU243HcMFyON67MHKZg05ssXiJfb7UrM2F7wr9uhy5HZvTWHEM9ihP8Zixbpr%2B2J08qfNZPZAWkZW4Gxed57EUOvn5LlmbkGum%2FZQOum2WoWP01vdoj5ilEbQKXmeBsg8pGRFVLmKZ11MZ21lM6Qt9nXjJtjH1oygd3QJMOiNIAvf8yyQo9gavz84dDg%2FuqbY2hgZz2cY7kzggjmwKYPuHDI5uGoYY0wo4OIxwY6pgGKA41zTN2XrOAOGxS9hAt29WlvUJ9PIjxo4DXSvSX0qrk%2BjR93Og1Z9lwahLJazugv30kTVa1qIHYBPqxJqhDU4opvBBt75HlYVprGtrRLunRHh9BwK7V0TOxgh2enDh9VToszw4F1QOviqFtjBJulSOGaS5N6uxCSQgMNHixrxdcdhkwKrgccoz5A2oNjmns%2BeYiw%2F85OhpIMY9QMBDzS9JmoRRtm&X-Amz-Signature=45d7b6f748f99e3f15b236e5885b4f7bfb2e4af4a95ad4a7aa20bc8d40ed8649&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)


# InGameMCP

一個最小可用的 Unity × MCP 範例，透過簡易的 WebSocket 伺服器把 Unity 場景中的玩家位置暴露為工具，讓 IDE（如 Cursor）可以讀取與控制玩家位置。

## 特色
- 內建 `Assets/SimpleMCP/SimpleMCP.cs`，於 Unity 端開啟 WebSocket 伺服器（預設埠 8765）
- 提供方法：取得玩家座標、設定玩家座標、取得玩家資訊
- 搭配 `Assets/SimpleMCP/PythonServer/simple_mcp_bridge.py` 作為 MCP Bridge，讓 Cursor 以 MCP 協定呼叫 Unity 方法

## 環境需求
- Unity 2021+（新版亦可）
- Python 3.9+（用於執行 MCP Bridge）
- 建議使用 Cursor（支援 MCP）

## 快速開始（Unity）
1. 開啟專案後打開場景：`Assets/SimpleMCP/SimpleMCP.unity`
2. 在場景中確認有一個 GameObject 掛載 `SimpleMCP` 組件（範例場景已包含 `SimpleMCPScript`）
3. 在 `SimpleMCP` Inspector 中設定：
   - `Port`: 預設 8765（可改）
   - `Player Transform`: 拖曳你的玩家物件；若留空會自動尋找 Tag 為 `Player` 的物件
4. 進入 Play 模式，Console 會顯示伺服器啟動訊息

## 可用方法（Unity 端）
- `get_position` / `getPosition`：回傳玩家目前位置
- `move_player` / `movePlayer` / `set_position` / `setPosition`：設定玩家位置（x, y, z）
- `get_player_info` / `getPlayerInfo`：回傳玩家 position/rotation/scale/name
- `ping`：健康檢查

## MCP Config（在 Cursor 啟用 MCP）
專案已提供 `.cursor/mcp.json`：

```json
{
  "mcpServers": {
    "unity-game-mcp": {
      "command": "python",
      "args": [
        "Assets/SimpleMCP/PythonServer/simple_mcp_bridge.py"
      ],
      "env": {
        "UNITY_HOST": "localhost",
        "UNITY_PORT": "8765"
      },
      "enabled": true
    }
  }
}
```

- 當在 Cursor 中開啟此專案，MCP 會自動啟動 Python Bridge 並嘗試連線到 Unity。
- 如需修改埠或主機，更新 `env.UNITY_HOST/UNITY_PORT` 或 `SimpleMCP` 組件中的 `Port`。

## Python Bridge（手動啟動）
如未使用 Cursor，也可手動啟動 bridge：

```bash
python Assets/SimpleMCP/PythonServer/simple_mcp_bridge.py
```

啟動後會嘗試以 `ws://localhost:8765` 連線 Unity（可透過環境變數覆寫）：

- Windows PowerShell：
```powershell
$env:UNITY_HOST = "localhost"
$env:UNITY_PORT = "8765"
python Assets/SimpleMCP/PythonServer/simple_mcp_bridge.py
```

- macOS/Linux（bash/zsh）：
```bash
UNITY_HOST=localhost UNITY_PORT=8765 \
python3 Assets/SimpleMCP/PythonServer/simple_mcp_bridge.py
```

Bridge 會將連線與請求記錄在 `Assets/SimpleMCP/PythonServer/unity_mcp_debug.log`。

## 在 IDE/工具端呼叫（範例）
若你的工具能送出 WebSocket 文本訊息給 Unity 伺服器，可直接傳 JSON：

```json
{"method":"get_position"}
```

或設定玩家位置：

```json
{"method":"move_player", "x": 20, "y": 5, "z": 5}
```

## 疑難排解
- 無法連線：
  - 確認 Unity 在 Play 模式且場景中有掛 `SimpleMCP`
  - 確認 Console 出現類似「伺服器已啟動在端口 8765」訊息
  - 檢查防火牆是否允許該埠
  - 檢查 `.cursor/mcp.json` 的 `UNITY_PORT` 與 `SimpleMCP` 組件的 `Port` 是否一致
- 找不到玩家：
  - 在 Inspector 指定 `Player Transform`，或確保玩家物件的 `Tag` 設為 `Player`

## 授權
本專案遵循 `LICENSE` 檔案。
