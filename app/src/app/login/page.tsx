"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { useAuth } from "@/hooks/useAuth";
import { BookOpen, Sparkles, ArrowRight } from "lucide-react";

export default function LoginPage() {
  const router = useRouter();
  const { login, isAuthenticated } = useAuth();
  const [isLoading, setIsLoading] = useState(false);

  // Redirect if already authenticated
  if (isAuthenticated()) {
    router.push("/");
  }

  const handleGoogleLogin = async () => {
    setIsLoading(true);
    try {
      // In a real app, you would use Google Sign-In SDK
      // For now, this is a placeholder
      const mockUser = {
        id: "user-123",
        email: "user@example.com",
        name: "John Doe",
        picture: "",
        createdAt: new Date().toISOString(),
      };

      login(mockUser, "mock-token");
      router.push("/");
    } catch (error) {
      console.error("Login failed:", error);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-900 via-blue-900 to-slate-900 flex items-center justify-center p-4">
      {/* Animated Background */}
      <div className="absolute inset-0 overflow-hidden">
        <div className="absolute w-96 h-96 bg-blue-500/20 rounded-full blur-3xl -top-20 -left-20 animate-pulse"></div>
        <div className="absolute w-96 h-96 bg-violet-500/20 rounded-full blur-3xl -bottom-20 -right-20 animate-pulse" style={{ animationDelay: "1s" }}></div>
      </div>

      <div className="relative z-10 w-full max-w-md">
        {/* Logo Section */}
        <div className="text-center mb-8">
          <div className="flex justify-center mb-4">
            <div className="p-3 bg-gradient-to-r from-blue-600 to-violet-600 rounded-2xl shadow-2xl">
              <Sparkles className="h-8 w-8 text-white" />
            </div>
          </div>
          <h1 className="text-4xl font-bold text-white mb-2">StudyAI</h1>
          <p className="text-blue-100 text-sm">Your AI-powered study companion</p>
        </div>

        {/* Login Card */}
        <Card className="border-0 shadow-2xl bg-white/95 backdrop-blur">
          <CardHeader className="space-y-4">
            <CardTitle className="text-2xl gradient-text">Welcome Back</CardTitle>
            <CardDescription className="text-base">
              Sign in to access your personalized learning experience
            </CardDescription>
          </CardHeader>
          <CardContent className="space-y-6">
            {/* Google Sign In Button */}
            <Button
              onClick={handleGoogleLogin}
              disabled={isLoading}
              className="w-full h-12 bg-white text-slate-900 border-2 border-slate-200 hover:border-blue-500 hover:shadow-lg transition-all rounded-xl font-semibold flex items-center justify-center gap-3"
            >
              {isLoading ? (
                <>
                  <span className="animate-spin">⚡</span>
                  Signing in...
                </>
              ) : (
                <>
                  <svg className="h-5 w-5" viewBox="0 0 24 24">
                    <path
                      fill="currentColor"
                      d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92c-.26 1.37-1.04 2.53-2.21 3.31v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.09z"
                    />
                    <path
                      fill="currentColor"
                      d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z"
                    />
                    <path
                      fill="currentColor"
                      d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.07H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.93l2.85-2.22.81-.62z"
                    />
                    <path
                      fill="currentColor"
                      d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.07l3.66 2.84c.87-2.6 3.3-4.53 6.16-4.53z"
                    />
                  </svg>
                  Sign in with Google
                </>
              )}
            </Button>

            {/* Divider */}
            <div className="relative">
              <div className="absolute inset-0 flex items-center">
                <div className="w-full border-t border-slate-200"></div>
              </div>
              <div className="relative flex justify-center text-sm">
                <span className="px-2 bg-white text-slate-500">or</span>
              </div>
            </div>

            {/* Demo Access */}
            <Button
              onClick={handleGoogleLogin}
              disabled={isLoading}
              className="w-full h-12 bg-gradient-to-r from-blue-600 to-violet-600 text-white rounded-xl font-semibold hover:shadow-lg transition-all hover:scale-105"
            >
              Try Demo Access
              <ArrowRight className="h-4 w-4 ml-2" />
            </Button>

            {/* Terms */}
            <p className="text-xs text-center text-slate-500">
              By signing in, you agree to our{" "}
              <a href="#" className="text-blue-600 hover:underline">
                Terms of Service
              </a>{" "}
              and{" "}
              <a href="#" className="text-blue-600 hover:underline">
                Privacy Policy
              </a>
            </p>
          </CardContent>
        </Card>

        {/* Features List */}
        <div className="mt-8 space-y-3">
          {[
            "🧠 AI-powered research for any topic",
            "📚 Interactive quizzes and assessments",
            "📊 Track your learning progress",
          ].map((feature, idx) => (
            <div key={idx} className="flex items-center gap-3 text-blue-100 text-sm">
              <div className="h-1.5 w-1.5 rounded-full bg-blue-400"></div>
              {feature}
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}
