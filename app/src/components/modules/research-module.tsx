"use client";

import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { Input } from "@/components/ui/input";
import { Button } from "@/components/ui/button";
import { Badge } from "@/components/ui/badge";
import { Skeleton } from "@/components/ui/skeleton";
import { Sparkles, FileText, Download, CheckCircle2, Zap } from "lucide-react";
import { useState } from "react";
import { useMutation } from "@tanstack/react-query";
import { apiClient } from "@/services/api";
import { useAuth } from "@/hooks/useAuth";

export function ResearchModule() {
  const { user } = useAuth();
  const [topicInput, setTopicInput] = useState("");
  const [weakConcepts, setWeakConcepts] = useState("");
  const [research, setResearch] = useState<any>(null);

  const researchMutation = useMutation({
    mutationFn: (data: any) => apiClient.research.createTopic(data),
    onSuccess: (response) => {
      setResearch(response.data);
      setTopicInput("");
      setWeakConcepts("");
    },
    onError: (error: any) => {
      alert("Research failed: " + (error.response?.data?.detail || error.message));
    },
  });

  const handleResearch = () => {
    if (!topicInput.trim() || !user) return;

    researchMutation.mutate({
      user_id: parseInt(user.id, 10) || 1,
      topic: topicInput,
      weak_concepts: weakConcepts
        .split(",")
        .map((c) => c.trim())
        .filter((c) => c),
    });
  };

  const downloadFile = (path: string, filename: string) => {
    const link = document.createElement("a");
    link.href = path;
    link.download = filename;
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
  };

  return (
    <div className="space-y-8">
      {/* Hero Section */}
      <div className="relative">
        <div className="absolute inset-0 bg-gradient-to-r from-blue-500/10 to-violet-500/10 rounded-2xl blur-3xl"></div>
        <div className="relative space-y-2">
          <div className="flex items-center gap-2">
            <Sparkles className="h-6 w-6 text-blue-600" />
            <h1 className="text-4xl font-bold gradient-text">AI-Powered Research</h1>
          </div>
          <p className="text-lg text-slate-600">
            Enter any topic and let AI generate comprehensive research materials with markdown and PDF exports
          </p>
        </div>
      </div>

      {/* Research Form */}
      <Card className="border-2 border-slate-200 shadow-lg hover:shadow-xl transition-shadow">
        <CardHeader>
          <CardTitle className="flex items-center gap-2">
            <Zap className="h-5 w-5 text-amber-500" />
            Create New Research
          </CardTitle>
          <CardDescription>
            Provide a topic and optionally specify weak concepts to focus on
          </CardDescription>
        </CardHeader>
        <CardContent className="space-y-6">
          {/* Topic Input */}
          <div className="space-y-3">
            <label className="text-sm font-semibold text-slate-700">Topic Name *</label>
            <div className="relative">
              <Input
                placeholder="e.g., Machine Learning Basics, React Hooks..."
                value={topicInput}
                onChange={(e) => setTopicInput(e.target.value)}
                className="h-12 text-base pl-4 border-2 border-slate-200 focus:border-blue-500 focus:ring-4 focus:ring-blue-50 rounded-xl transition-all"
              />
            </div>
          </div>

          {/* Weak Concepts Input */}
          <div className="space-y-3">
            <label className="text-sm font-semibold text-slate-700">Weak Concepts (Optional)</label>
            <Input
              placeholder="e.g., neural networks, backpropagation, gradient descent"
              value={weakConcepts}
              onChange={(e) => setWeakConcepts(e.target.value)}
              className="h-12 text-base pl-4 border-2 border-slate-200 focus:border-blue-500 focus:ring-4 focus:ring-blue-50 rounded-xl transition-all"
            />
            <p className="text-xs text-slate-500">Separate multiple concepts with commas</p>
          </div>

          {/* Submit Button */}
          <Button
            onClick={handleResearch}
            disabled={researchMutation.isPending || !topicInput.trim()}
            className="w-full h-12 text-base font-semibold bg-gradient-to-r from-blue-600 to-violet-600 hover:from-blue-700 hover:to-violet-700 text-white rounded-xl transition-all transform hover:scale-105 disabled:opacity-50 disabled:cursor-not-allowed"
          >
            {researchMutation.isPending ? (
              <>
                <span className="animate-spin mr-2">⚡</span>
                Researching...
              </>
            ) : (
              <>
                <Sparkles className="h-5 w-5 mr-2" />
                Start Research
              </>
            )}
          </Button>
        </CardContent>
      </Card>

      {/* Loading State */}
      {researchMutation.isPending && (
        <div className="space-y-4">
          <Skeleton className="h-48 rounded-xl" />
          <div className="flex justify-center">
            <div className="flex gap-1">
              <div className="h-2 w-2 bg-blue-600 rounded-full animate-bounce" style={{ animationDelay: "0s" }}></div>
              <div className="h-2 w-2 bg-blue-600 rounded-full animate-bounce" style={{ animationDelay: "0.2s" }}></div>
              <div className="h-2 w-2 bg-blue-600 rounded-full animate-bounce" style={{ animationDelay: "0.4s" }}></div>
            </div>
          </div>
        </div>
      )}

      {/* Success Result */}
      {research && (
        <div className="space-y-6 animate-in fade-in">
          <div className="relative">
            <div className="absolute inset-0 bg-gradient-to-r from-green-500/10 to-emerald-500/10 rounded-2xl blur-3xl"></div>
            <Card className="relative border-2 border-green-200 bg-gradient-to-br from-green-50 to-emerald-50 shadow-xl">
              <CardHeader>
                <div className="flex items-start justify-between">
                  <div className="flex items-center gap-3">
                    <div className="p-2 bg-green-600 rounded-lg">
                      <CheckCircle2 className="h-6 w-6 text-white" />
                    </div>
                    <div>
                      <CardTitle className="text-green-900">Research Complete! 🎉</CardTitle>
                      <CardDescription className="text-green-700">
                        Your research materials are ready for download
                      </CardDescription>
                    </div>
                  </div>
                </div>
              </CardHeader>
              <CardContent className="space-y-6">
                {/* Info Card */}
                <div className="bg-white rounded-lg p-4 border border-green-100">
                  <div className="grid grid-cols-2 gap-4">
                    <div>
                      <p className="text-xs text-slate-500 font-semibold uppercase">Topic ID</p>
                      <p className="text-lg font-bold text-slate-900 mt-1">{research.topic_id}</p>
                    </div>
                    <div>
                      <p className="text-xs text-slate-500 font-semibold uppercase">Status</p>
                      <Badge className="mt-1 bg-green-600">Ready</Badge>
                    </div>
                  </div>
                </div>

                {/* Download Buttons */}
                <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                  <Button
                    variant="outline"
                    className="h-14 border-2 border-blue-300 bg-white hover:bg-blue-50 text-blue-600 font-semibold rounded-xl transition-all"
                    onClick={() => {
                      if (research.markdown_path) {
                        window.open(research.markdown_path, "_blank");
                      }
                    }}
                  >
                    <FileText className="h-5 w-5 mr-2" />
                    View Markdown
                  </Button>
                  <Button
                    className="h-14 bg-gradient-to-r from-blue-600 to-violet-600 hover:from-blue-700 hover:to-violet-700 text-white font-semibold rounded-xl transition-all"
                    onClick={() => {
                      if (research.pdf_path) {
                        downloadFile(research.pdf_path, `research-${research.topic_id}.pdf`);
                      }
                    }}
                  >
                    <Download className="h-5 w-5 mr-2" />
                    Download PDF
                  </Button>
                </div>

                {/* File Paths Info */}
                <div className="bg-slate-50 rounded-lg p-4 space-y-2">
                  <p className="text-xs font-semibold text-slate-500 uppercase">File Locations</p>
                  <div className="space-y-2 text-xs text-slate-600">
                    <p className="font-mono bg-white p-2 rounded border border-slate-200 break-all">
                      📄 {research.markdown_path}
                    </p>
                    <p className="font-mono bg-white p-2 rounded border border-slate-200 break-all">
                      📕 {research.pdf_path}
                    </p>
                  </div>
                </div>
              </CardContent>
            </Card>
          </div>
        </div>
      )}
    </div>
  );
}
