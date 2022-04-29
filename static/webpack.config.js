const path=require('path')
const {
  merge
} = require('webpack-merge');
const BundleTracker = require('webpack-bundle-tracker');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');
module.exports ={
    mode:'development',
    entry:
    {
     bundle:   path.resolve(__dirname,'src/assets/js/index.js'),
    },
    output: {
        path: path.resolve(__dirname,'src/assets/dist'),
        filename: '[name].js',
    },
    plugins: [
        new BundleTracker({ filename: './webpack-stats.json' }),
        new MiniCssExtractPlugin({
          filename: '[name]-[chunkhash].css',
          chunkFilename: '[id]-[name]-[chunkhash].css',
        }),
      ],
      module: {
        rules: [{
          test: /\.css$/i,
          use: [MiniCssExtractPlugin.loader, "css-loader"],
        }, {
          test: /\.scss$/,
          use: [MiniCssExtractPlugin.loader, "css-loader", "sass-loader"],
        }, {
          test: /\.(gif|svg|jpg|png)$/,
          loader: "file-loader",
        }]
      },
}