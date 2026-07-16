"use client";

import { ReactNode } from "react";
import Link from "next/link";
import { useAuth } from "@/hooks/useAuth";
import { useRouter } from "next/navigation";
import { Button } from "@/components/ui/button";
import { BookOpen, LogOut, Sparkles } from "lucide-react";
import { getInitials } from "@/utils/helpers";

export function RootLayout({ children }: { children: ReactNode }) {
  const { user, logout } = useAuth();
  const router = useRouter();

  const handleLogout = () => {
    logout();
    router.push("/login");
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-50 via-white to-slate-100">
      {/* Navigation */}
      <nav className="sticky top-0 z-50 backdrop-blur-lg bg-white/80 border-b border-slate-200/50 shadow-sm">
        <div className="max-w-7xl mx-auto px-6 py-4 flex items-center justify-between">
          <Link href="/" className="flex items-center gap-3 font-bold text-xl group">
            <div className="relative">
              <div className="absolute inset-0 bg-gradient-to-r from-blue-600 to-violet-600 rounded-lg blur opacity-75 group-hover:opacity-100 transition duration-1000"></div>
              <div className="relative bg-white px-3 py-2 rounded-lg">
                <BookOpen className="h-5 w-5 bg-gradient-to-r from-blue-600 to-violet-600 bg-clip-text text-transparent" />
              </div>
            </div>
            <span className="bg-gradient-to-r from-blue-600 to-violet-600 bg-clip-text text-transparent">StudyAI</span>
          </Link>

          {user && (
            <div className="flex items-center gap-6">
              <div className="flex items-center gap-3 px-4 py-2 rounded-full bg-gradient-to-r from-blue-50 to-violet-50 border border-blue-100">
                <div className="h-8 w-8 rounded-full bg-gradient-to-r from-blue-600 to-violet-600 text-white flex items-center justify-center text-xs font-semibold">
                  {getInitials(user.name)}
                </div>
                <span className="text-sm font-medium text-slate-700">{user.name}</span>
              </div>
              <Button
                variant="ghost"
                size="sm"
                onClick={handleLogout}
                className="gap-2 hover:bg-red-50 text-red-600 hover:text-red-700"
              >
                <LogOut className="h-4 w-4" />
                Logout
              </Button>
            </div>
          )}
        </div>
      </nav>

      {/* Main Content */}
      <main className="max-w-7xl mx-auto px-6 py-12">{children}</main>
    </div>
  );
}
