const MiniCssExtractPlugin = require('mini-css-extract-plugin')
const HtmlWebpackPlugin = require('html-webpack-plugin')
const TerserWebpackPlugin = require('terser-webpack-plugin')
const OptimizeCssAssetsWebpackPlugin = require('optimize-css-assets-webpack-plugin')

module.exports = {
    mode: 'development',
    entry: './src/index.js',
    devtool: 'inline-source-map',
    devServer: {
        static: './dist',
        hot: true,
        open: true,
        port: 3001 
      },
    output: {
       
      filename: 'super.js'
    },
    plugins: [
            new MiniCssExtractPlugin(),
            new HtmlWebpackPlugin({
                template:'src/index.pug',
                title: 'Development',
                filename:'index.html'
            }),
            new TerserWebpackPlugin(),
            new OptimizeCssAssetsWebpackPlugin(),
        ],
        optimization: {
            minimize:true,
            minimizer: [new TerserWebpackPlugin(),  new OptimizeCssAssetsWebpackPlugin()],
          },
    module: {
      rules: [
        { test: /\.css$/,
         use: [
                {
                    loader: MiniCssExtractPlugin.loader,
                    options: {
                    esModule: true,
                    },
                },
                'css-loader',
            ],

         },
         {
            test: /\.pug$/,
            use: 'pug-loader'

         }
      ]
    }
  };