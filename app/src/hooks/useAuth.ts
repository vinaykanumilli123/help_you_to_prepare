import { useAuthStore } from "@/stores/auth";
import { useEffect } from "react";
import { useRouter } from "next/navigation";

export const useAuth = () => {
  return useAuthStore();
};

export const useRequireAuth = () => {
  const router = useRouter();
  const { isAuthenticated, user } = useAuthStore();

  useEffect(() => {
    if (!isAuthenticated()) {
      router.push("/login");
    }
  }, [isAuthenticated, router]);

  return { user, isAuthenticated: isAuthenticated() };
};
