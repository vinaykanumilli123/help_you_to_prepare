# Study Assistant Frontend

## Setup

```bash
cd app
npm install
```

## Development

```bash
npm run dev
```

Open [http://localhost:3000](http://localhost:3000) in your browser.

## Build

```bash
npm run build
npm start
```

## Features

- 🔐 Google Authentication
- 📚 Research Module - AI-powered research assistance
- 🎯 Quiz Module - Interactive quizzes
- 📊 Evaluation Module - Progress tracking and evaluation
- 🎨 Modern UI with Tailwind CSS
- ⚡ Server-side rendering with Next.js
- 🔄 Real-time data fetching with TanStack Query

## Environment Variables

Create a `.env.local` file:

```
NEXT_PUBLIC_API_URL=http://localhost:8000
```

## Project Structure

- `src/app` - Next.js App Router pages
- `src/components` - React components (UI, layouts, modules)
- `src/services` - API service clients
- `src/hooks` - Custom React hooks
- `src/stores` - Zustand state management
- `src/types` - TypeScript type definitions
- `src/utils` - Utility functions
- `src/styles` - Global styles
