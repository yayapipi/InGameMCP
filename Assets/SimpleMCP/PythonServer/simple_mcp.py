#!/usr/bin/env python3
"""
簡單的 MCP 測試客戶端
使用方法: python simple_client.py
"""

import asyncio
import websockets
import json

async def test_mcp():
    uri = "ws://localhost:8765"
    
    try:
        async with websockets.connect(uri) as ws:
            print(f"✓ 已連接到 {uri}\n")
            
            # 1. 獲取玩家位置
            print("1️⃣ 獲取玩家位置...")
            await ws.send(json.dumps({"method": "get_position"}))
            response = await ws.recv()
            print(f"   回應: {response}\n")
            await asyncio.sleep(1)
            
            # 2. 移動玩家到 (5, 0, 5)
            print("2️⃣ 移動玩家到 (5, 0, 5)...")
            await ws.send(json.dumps({
                "method": "move_player",
                "x": 5.0,
                "y": 0.0,
                "z": 5.0
            }))
            response = await ws.recv()
            print(f"   回應: {response}\n")
            await asyncio.sleep(1)
            
            # 3. 再次獲取位置確認
            print("3️⃣ 確認新位置...")
            await ws.send(json.dumps({"method": "get_position"}))
            response = await ws.recv()
            print(f"   回應: {response}\n")
            await asyncio.sleep(1)
            
            # 4. 移動玩家到 (-3, 1, 8)
            print("4️⃣ 移動玩家到 (-3, 1, 8)...")
            await ws.send(json.dumps({
                "method": "move_player",
                "x": -3.0,
                "y": 1.0,
                "z": 8.0
            }))
            response = await ws.recv()
            print(f"   回應: {response}\n")
            
            print("✓ 測試完成！")
            
    except Exception as e:
        print(f"✗ 錯誤: {e}")

async def interactive():
    """互動模式"""
    uri = "ws://localhost:8765"
    
    try:
        async with websockets.connect(uri) as ws:
            print(f"✓ 已連接到 {uri}")
            print("\n指令:")
            print("  pos - 獲取玩家位置")
            print("  move <x> <y> <z> - 移動玩家")
            print("  quit - 退出\n")
            
            while True:
                cmd = input("> ").strip().split()
                if not cmd:
                    continue
                
                if cmd[0] == "quit":
                    break
                elif cmd[0] == "pos":
                    await ws.send(json.dumps({"method": "get_position"}))
                    response = await ws.recv()
                    data = json.loads(response)
                    if "error" in data:
                        print(f"   ✗ {data['error']}")
                    else:
                        print(f"   位置: ({data['x']:.2f}, {data['y']:.2f}, {data['z']:.2f})")
                elif cmd[0] == "move" and len(cmd) == 4:
                    await ws.send(json.dumps({
                        "method": "move_player",
                        "x": float(cmd[1]),
                        "y": float(cmd[2]),
                        "z": float(cmd[3])
                    }))
                    response = await ws.recv()
                    data = json.loads(response)
                    if "error" in data:
                        print(f"   ✗ {data['error']}")
                    else:
                        print(f"   ✓ 已移動到: ({data['x']:.2f}, {data['y']:.2f}, {data['z']:.2f})")
                else:
                    print("   ✗ 未知指令")
                    
    except Exception as e:
        print(f"✗ 錯誤: {e}")

if __name__ == "__main__":
    import sys
    
    print("=" * 50)
    print("Unity MCP 簡單測試客戶端")
    print("=" * 50)
    print()
    
    if len(sys.argv) > 1 and sys.argv[1] == "-i":
        asyncio.run(interactive())
    else:
        print("示範模式（使用 -i 進入互動模式）\n")
        asyncio.run(test_mcp())