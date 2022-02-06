# battle_ope_recorder
electronアプリ
# 行ったこと
- 接続されているビデオデバイスの名前とIDをPython(flask)上で取得
- デバイス名をセレクトできるようにした
- ~~デバイスIDをPOSTで送れるようにした~~→urlにidを乗せる方式にした
- アプリ上にUVCカメラの映像を表示させる
- アプリ上でデバイス選択をした際ビデオを切り替える機能を実装　動画は無限ループで取り込んでいるので切り替えが起こったことをクラス変数でやり取りしている
- UVCデバイスの一覧を取得し、その中からVideoデバイスを取得し、label(デバイス名)とdeviceIdを取得して選択できるようにした。
- vue上でUVCデバイスから映像を取得してVideoタグで表示させる
- vue上で取得したデバイス画像をflaskにpostする機能を追加
- 画像処理をしてスコアを算出する機能を追加　vueからポストしてflaskで受けとってスコアを返す
- 画像処理のスコア算出方法(マッチした数字の位置と数字の算出)を少し変更 スコアの部分だけ切り取ってテンプレートマッチングすることにより少し処理を軽量化

# 行うこと
- 画像処理実装 (id認識、マッチ種類、ルール、コスト、マップ、参加人数)
- 見栄え
- vue側でocrしてみる

# 気になる点
    ~~デバイス選択切り替えが早すぎると、静止画になってしまう（キャッシュのような感じ）~~
    ~~対策として500 ms空画像を表示させている。映像が送信されたことが判定できるとよい~~
    ↑vue側でビデオを取得するので問題なくなった。
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
