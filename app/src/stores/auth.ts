import { create } from "zustand";
import { persist } from "zustand/middleware";
import { User, AuthState } from "@/types";
import Cookies from "js-cookie";

interface AuthStore extends AuthState {
  login: (user: User, token: string) => void;
  logout: () => void;
  setUser: (user: User | null) => void;
  setLoading: (loading: boolean) => void;
  setError: (error: string | null) => void;
  isAuthenticated: () => boolean;
}

export const useAuthStore = create<AuthStore>()(
  persist(
    (set, get) => ({
      user: null,
      token: null,
      isLoading: false,
      error: null,

      login: (user: User, token: string) => {
        Cookies.set("auth_token", token, { expires: 7 });
        set({ user, token, error: null });
      },

      logout: () => {
        Cookies.remove("auth_token");
        set({ user: null, token: null, error: null });
      },

      setUser: (user: User | null) => set({ user }),

      setLoading: (isLoading: boolean) => set({ isLoading }),

      setError: (error: string | null) => set({ error }),

      isAuthenticated: () => {
        const { token } = get();
        return !!token;
      },
    }),
    {
      name: "auth-store",
      partialize: (state) => ({ user: state.user, token: state.token }),
    }
  )
);
