# battle_ope_recorder
electronアプリ
# 行ったこと
- デバイス名をセレクトできるようにした
- アプリ上にUVCカメラの映像を表示させる
- vue上でUVCデバイスから映像を取得してVideoタグで表示させる
- vue上で取得したデバイス画像をflaskにpostする機能を追加
- 画像処理をしてスコアを算出する機能を追加　vueからポストしてflaskで受けとってスコアを返す
- 画像処理のスコア算出方法(マッチした数字の位置と数字の算出)を少し変更 スコアの部分だけ切り取ってテンプレートマッチングすることにより少し処理を軽量化

## ocr
- vue側でocrしてみた ユーザーのインストールがいらないからこっちのほうがいいかも
- ocrに結構時間がかかるので1idごとに切り取ってリザルトの時に一回だけocrするのがいいかも

# 行うこと
- 画像処理実装 (id認識、マッチ種類、ルール、コスト、マップ、参加人数)
- 見栄え

## 画像処理
- ブリーフィング、準備完了を常にテンプレートマッチングで認識して、ルールなどの部分を切り取ってフロント側に渡す
- 準備完了を押した後でもルール等が認識できるか確認

# 気になる点
    id認識するためのocr処理が時間かかかりすぎている

# Emoji
 ==================== Emojis ====================  
🌱  :seedling: 初めてのコミット（Initial Commit）  
🔖  :bookmark: バージョンタグ（Version Tag）  
✨  :sparkles: 新機能（New Feature）  
🐛  :bug: バグ修正（Bugfix）  
♻️  :recycle: リファクタリング(Refactoring)  
📚  :books: ドキュメント（Documentation）  
🎨  :art: デザインUI/UX(Accessibility)  
🐎  :horse: パフォーマンス（Performance）  
🔧  :wrench: ツール（Tooling）  
🚨  :rotating_light: テスト（Tests）  
💩  :hankey: 非推奨追加（Deprecation）  
🗑️  :wastebasket: 削除（Removal）  
🚧  :construction: WIP(Work In Progress)  

## Project setup
```
yarn install
```

### Compiles and hot-reloads for development
```
yarn serve
```

### Compiles and minifies for production
```
yarn build
```

### Lints and fixes files
```
yarn lint
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).
