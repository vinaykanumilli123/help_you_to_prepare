"use client";

import { useRouter } from "next/navigation";
import { useEffect } from "react";
import { useAuth } from "@/hooks/useAuth";
import { QuizModule } from "@/components/modules/quiz-module";
import { Skeleton } from "@/components/ui/skeleton";

export default function QuizzesPage() {
  const router = useRouter();
  const { isAuthenticated, user } = useAuth();

  useEffect(() => {
    if (!isAuthenticated()) {
      router.push("/login");
    }
  }, [isAuthenticated, router]);

  if (!user) {
    return (
      <div className="space-y-4">
        <Skeleton className="h-12 w-64" />
        <div className="grid grid-cols-2 gap-4 mt-8">
          {Array(4)
            .fill(0)
            .map((_, i) => (
              <Skeleton key={i} className="h-32" />
            ))}
        </div>
      </div>
    );
  }

  return <QuizModule />;
}
