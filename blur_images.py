# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

from PIL import Image, ImageFilter
import os

folder = r'C:\Users\tsuku\Documents\Antigravity\test\projects\ゆるふわ\ly-hair-beautysalon\note用画像'
output = os.path.join(folder, 'ぼかし済み')
os.makedirs(output, exist_ok=True)

def blur_regions(filename, regions):
    path = os.path.join(folder, filename)
    if not os.path.exists(path):
        print(f"NOT FOUND: {filename}")
        return
    img = Image.open(path).convert("RGB")
    for (x1, y1, x2, y2) in regions:
        region = img.crop((x1, y1, x2, y2))
        blurred = region.filter(ImageFilter.GaussianBlur(radius=15))
        img.paste(blurred, (x1, y1))
    out_path = os.path.join(output, filename.replace('【ぼかし必要】', '').replace('【アイコンぼかし】', ''))
    img.save(out_path)
    print(f"OK: {filename}")

blur_regions('②_Git_Credential_Manager認証.png', [
    (563, 255, 920, 300),
])

blur_regions('③_GitHubリポジトリ一覧.png', [
    (1490, 0, 1545, 50),
])

blur_regions('④_GitHub_Pages設定画面【ぼかし必要】.png', [
    (0, 0, 420, 55),         # 左上ブレッドクラム
    (490, 240, 830, 270),    # URL内のtsukushihub
    (484, 268, 670, 292),    # Last deployed by tsukushihub
    (1490, 0, 1545, 50),     # 右上アイコン
])

blur_regions('⑦_NetlifyとGitHub連携認証【ぼかし必要】.png', [
    (200, 168, 480, 200),
])

blur_regions('⑧_Confirm_access【ぼかし必要】.png', [
    (28, 60, 80, 118),       # アイコン
    (88, 82, 295, 120),      # @tsukushihub
])

blur_regions('⑨_Netlifyリポジトリ選択【ぼかし必要】.png', [
    (135, 278, 175, 330),
    (175, 285, 355, 325),
])

blur_regions('⑩_デプロイ確認画面【ぼかし必要】.png', [
    (45, 475, 430, 530),
])

blur_regions('⑪_デプロイ完了画面【アイコンぼかし】.png', [
    (20, 800, 75, 857),
])

blur_regions('⑮_Netlifyクレジット【ぼかし必要】.png', [
    (183, 10, 320, 48),
])

blur_regions('㉔_Project_configuration_Change_project_name【ぼかし必要】.png', [
    (835, 318, 910, 348),
    (835, 360, 1160, 395),
])

print("完了！ぼかし済みフォルダに保存されました。")
