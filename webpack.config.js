// https://medium.com/labcodes/configurando-um-projeto-django-com-react-1292abded7a5

const path = require('path');
let CopyWebpackPlugin = require('copy-webpack-plugin');

module.exports = {
    entry: './index.js',
    // output: {
    //     filename: 'main.js',
    //     path: path.resolve(__dirname, 'static/dist')
    // },
    // module: {
    //     rules: [{
    //         test: /\.css$/,
    //         use: ['style-loader', 'css-loader']
    //     }]
    // },
    plugins: [
        new CopyWebpackPlugin([{
            from: './node_modules/admin-lte',
            to: path.resolve(__dirname, 'static/admin-lte')
        }])
    ]
};