"use client";

import { useEffect } from "react";
import { useRouter } from "next/navigation";
import { DashboardOverview } from "@/components/modules/dashboard-overview";
import { useAuth } from "@/hooks/useAuth";
import { Skeleton } from "@/components/ui/skeleton";

export default function Home() {
  const router = useRouter();
  const { user, isAuthenticated } = useAuth();

  useEffect(() => {
    if (!isAuthenticated()) {
      router.push("/login");
    }
  }, [isAuthenticated, router]);

  if (!user) {
    return (
      <div className="space-y-4">
        <Skeleton className="h-12 w-64" />
        <Skeleton className="h-6 w-96" />
        <div className="grid grid-cols-3 gap-6 mt-8">
          {Array(3)
            .fill(0)
            .map((_, i) => (
              <Skeleton key={i} className="h-64" />
            ))}
        </div>
      </div>
    );
  }

  return <DashboardOverview />;
}
