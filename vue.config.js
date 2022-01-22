module.exports = {
    devServer: {

        // localhostでvueからexpressにAPIリクエストを送信する為の設定
        proxy:{
            '^/': {
                target:'http://localhost:5000',
                changeOrigin: true,
            },
        },
        watchOptions: {
            poll: true
          }
    
},
pluginOptions: {
    electronBuilder: {
        builderOptions: {
            "extraResources": [
                "./build/**/*",
            ],
        },
        pluginOptions: {
            nodeIntegration: true
        }
    }
},


}