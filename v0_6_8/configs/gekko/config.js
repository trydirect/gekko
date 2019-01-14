const CONFIG = {
    headless: true,
    api: {
        host: '127.0.0.1',
        port: 3000,
    },
    ui: {
        ssl: true,
        host: '{{DOMAIN}}',
        port: 443,
        path: '/' // change this if you are serving from something like `example.com/gekko`
    },
    adapter: 'sqlite'
}