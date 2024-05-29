module.exports = {
    devServer: {
      proxy: {
        '/api': {
          target: 'http://localhost:4000/api/stocks',
          changeOrigin: true,
        },
      },
    },
  };
  