import axios, { AxiosInstance } from "axios";
import Cookies from "js-cookie";

const API_URL = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8002";

class APIClient {
  private client: AxiosInstance;

  constructor() {
    this.client = axios.create({
      baseURL: API_URL,
      headers: {
        "Content-Type": "application/json",
      },
    });

    // Add token to requests
    this.client.interceptors.request.use((config) => {
      const token = Cookies.get("auth_token");
      if (token) {
        config.headers.Authorization = `Bearer ${token}`;
      }
      return config;
    });

    // Handle errors
    this.client.interceptors.response.use(
      (response) => response,
      (error) => {
        if (error.response?.status === 401) {
          // Handle unauthorized
          Cookies.remove("auth_token");
          window.location.href = "/login";
        }
        return Promise.reject(error);
      }
    );
  }

  // Auth endpoints
  auth = {
    googleLogin: (token: string) =>
      this.client.post("/api/auth/google", { token }),
    logout: () => this.client.post("/api/auth/logout"),
    me: () => this.client.get("/api/auth/me"),
  };

  // Research endpoints
  research = {
    createTopic: (data: any) => this.client.post("/api/research", data),
  };

  // Quiz endpoints
  quizzes = {
    generate: (data: any) => this.client.post("/api/quiz", data),
  };

  // Evaluation endpoints
  evaluations = {
    evaluate: (data: any) => this.client.post("/api/evaluate", data),
  };
}

export const apiClient = new APIClient();
