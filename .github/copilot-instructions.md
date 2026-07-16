# Study Assistant Frontend Development

## Project Overview

This is a modern React/Next.js frontend for the Study Assistant application, a comprehensive AI-powered learning platform with:

- **Research Module**: AI-powered research assistance
- **Quiz Module**: Interactive quizzes and assessments
- **Evaluation Module**: Progress tracking and performance analytics

## Technology Stack

- **Framework**: Next.js 14 (App Router)
- **Language**: TypeScript
- **Styling**: Tailwind CSS
- **UI Components**: Custom shadcn/ui style components
- **State Management**: Zustand + React Context
- **Data Fetching**: Axios + TanStack Query (React Query)
- **Form Handling**: React Hook Form + Zod

## Project Structure

```
app/
├── src/
│   ├── app/                    # Next.js app directory
│   │   ├── (routes)/          # Page routes
│   │   ├── layout.tsx         # Root layout
│   │   └── providers.tsx      # Context providers
│   ├── components/
│   │   ├── ui/                # Reusable UI components
│   │   ├── layouts/           # Page layouts
│   │   └── modules/           # Feature modules
│   ├── hooks/                 # Custom React hooks
│   ├── services/              # API clients and services
│   ├── stores/                # Zustand stores (state management)
│   ├── types/                 # TypeScript type definitions
│   ├── utils/                 # Utility functions
│   └── styles/                # Global styles
├── package.json               # Dependencies
├── tsconfig.json             # TypeScript config
├── tailwind.config.ts        # Tailwind configuration
├── next.config.js            # Next.js configuration
└── README.md
```

## Getting Started

### Prerequisites

- Node.js 18+
- npm or yarn

### Installation

```bash
cd app
npm install
```

### Development

```bash
npm run dev
```

Open [http://localhost:3000](http://localhost:3000) in your browser.

The app will reload when you make changes.

### Build

```bash
npm run build
npm start
```

### Type Checking

```bash
npm run type-check
```

### Linting

```bash
npm run lint
```

## Environment Variables

Create a `.env.local` file in the `app` directory:

```env
NEXT_PUBLIC_API_URL=http://localhost:8000
```

## Key Features

### Authentication
- Google OAuth integration
- Token-based authentication
- Protected routes with `useRequireAuth` hook
- Persistent session with cookies and Zustand

### API Integration
- Centralized API client with Axios
- Automatic token injection in headers
- Error handling and retry logic
- TanStack Query for caching and synchronization

### UI Components
- Modern, accessible components built with Tailwind CSS
- Variant-based styling with `class-variance-authority`
- Responsive design patterns
- Loading states and skeletons

### State Management
- Auth store with Zustand for user state
- React Query for server state
- Context API for theme and app-level config

## Development Guidelines

### Component Conventions

1. **Use "use client" directive** for interactive components
2. **File naming**: camelCase for files, PascalCase for components
3. **Import paths**: Use `@/` alias for absolute imports
4. **Props**: Define interfaces for all props

```typescript
interface MyComponentProps {
  title: string;
  onAction?: () => void;
}

export function MyComponent({ title, onAction }: MyComponentProps) {
  // ...
}
```

### Style Guidelines

- Use Tailwind utility classes
- Extract repeated patterns into components
- Use CSS variables for theming
- Maintain consistent spacing with Tailwind scale

### API Usage

```typescript
import { apiClient } from "@/services/api";
import { useQuery, useMutation } from "@tanstack/react-query";

// Query example
const { data, isLoading } = useQuery({
  queryKey: ["quizzes"],
  queryFn: () => apiClient.quizzes.getAll(),
});

// Mutation example
const { mutate } = useMutation({
  mutationFn: (data) => apiClient.quizzes.submitAttempt(data),
  onSuccess: () => {
    // Handle success
  },
});
```

## Testing

Tests are set up with Jest. Run tests with:

```bash
npm test
```

## Deployment

The frontend can be deployed to Vercel, Netlify, or any Node.js hosting platform.

### Vercel (Recommended)

```bash
npm install -g vercel
vercel
```

### Docker

A Dockerfile can be added for containerized deployment.

## Scripts

- `npm run dev` - Start development server
- `npm run build` - Build for production
- `npm start` - Start production server
- `npm run lint` - Run ESLint
- `npm run type-check` - Run TypeScript type checking

## Troubleshooting

### API Connection Issues

1. Ensure backend server is running on `http://localhost:8000`
2. Check CORS configuration in backend
3. Verify `NEXT_PUBLIC_API_URL` in `.env.local`

### TypeScript Errors

1. Run `npm run type-check` to identify issues
2. Check `tsconfig.json` path aliases
3. Verify imports use `@/` alias pattern

### Build Failures

1. Clear `.next` folder: `rm -rf .next`
2. Clear node_modules: `rm -rf node_modules && npm install`
3. Check for TypeScript errors: `npm run type-check`

## Contributing

- Follow the file structure conventions
- Write TypeScript for all components
- Use ESLint for code quality
- Keep components small and focused
- Document complex logic with comments

## License

MIT
