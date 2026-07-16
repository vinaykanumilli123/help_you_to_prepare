import type { Metadata } from "next";
import { Providers } from "./providers";
import { RootLayout } from "@/components/layouts/root-layout";
import "@/styles/globals.css";

export const metadata: Metadata = {
  title: "Study Assistant - AI-Powered Learning",
  description: "Your intelligent study companion powered by AI",
};

export default function Layout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en" suppressHydrationWarning>
      <body>
        <Providers>
          <RootLayout>{children}</RootLayout>
        </Providers>
      </body>
    </html>
  );
}
