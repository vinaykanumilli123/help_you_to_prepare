// Auth Types
export interface User {
  id: string;
  email: string;
  name: string;
  picture?: string;
  createdAt: string;
}

export interface AuthState {
  user: User | null;
  token: string | null;
  isLoading: boolean;
  error: string | null;
}

// Research Types
export interface ResearchRequest {
  user_id: number;
  topic: string;
  weak_concepts: string[];
}

export interface ResearchResponse {
  topic_id: number;
  markdown_path: string;
  pdf_path: string;
}

// Quiz Types
export interface QuizRequest {
  user_id: number;
  topic_id: number;
}

export interface QuizQuestion {
  question: string;
  options: string[];
}

export interface QuizResponse {
  quiz_id: number;
  questions: QuizQuestion[];
}

// Evaluation Types
export interface EvaluationRequest {
  user_id: number;
  quiz_id: number;
  answers: string[];
}

export interface EvaluationResponse {
  score: number;
  passed: boolean;
  weak_concepts: string[];
}

// API Response Types
export interface ApiResponse<T> {
  success: boolean;
  data?: T;
  error?: string;
  message?: string;
}

export interface PaginatedResponse<T> {
  items: T[];
  total: number;
  page: number;
  pageSize: number;
  hasMore: boolean;
}
