# electron-vite-vue

```
Really simple `Electron` + `Vue` + `Vite`
Example is chunk upload
```
## Quick Start

```sh
npm install
npm run dev
```

## Directory

```diff
+ ├─┬ electron
+ │ ├─┬ main
+ │ │ └── index.ts    entry of Electron-Main
+ │ └─┬ preload
+ │   └── index.ts    entry of Preload-Scripts
  ├─┬ src
  │ └── main.ts       entry of Electron-Renderer
  ├── index.html
  ├── package.json
  └── vite.config.ts
```

## Api

```
pip install fastapi, uvicorn
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```