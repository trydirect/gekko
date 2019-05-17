const CONFIG = {
  headless: true,
  api: {
    host: '0.0.0.0',
    port: 3000,
    timeout: 120000 // 2 minutes
  },
  ui: {
    ssl: false,
    host: '0.0.0.0',
    port: 8080,
    path: '/'
  },
  adapter: 'sqlite'
}


if(typeof window === 'undefined')
  module.exports = CONFIG;
else
  window.CONFIG = CONFIG;
