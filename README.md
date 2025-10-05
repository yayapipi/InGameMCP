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
