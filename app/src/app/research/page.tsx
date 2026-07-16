"use client";

import { useRouter } from "next/navigation";
import { useEffect } from "react";
import { useAuth } from "@/hooks/useAuth";
import { ResearchModule } from "@/components/modules/research-module";
import { Skeleton } from "@/components/ui/skeleton";

export default function ResearchPage() {
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
        <Skeleton className="h-10 w-full" />
        {Array(3)
          .fill(0)
          .map((_, i) => (
            <Skeleton key={i} className="h-24" />
          ))}
      </div>
    );
  }

  return <ResearchModule />;
}
