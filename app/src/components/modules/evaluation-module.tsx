"use client";

import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Badge } from "@/components/ui/badge";
import { BarChart3 } from "lucide-react";
import { useState } from "react";
import { useMutation } from "@tanstack/react-query";
import { apiClient } from "@/services/api";
import { useAuth } from "@/hooks/useAuth";

export function EvaluationModule() {
  const { user } = useAuth();
  const [quizIdInput, setQuizIdInput] = useState("");
  const [answersInput, setAnswersInput] = useState("");
  const [evaluation, setEvaluation] = useState<any>(null);
  const [evaluationHistory, setEvaluationHistory] = useState<any[]>([]);

  const evaluateMutation = useMutation({
    mutationFn: (data: any) => apiClient.evaluations.evaluate(data),
    onSuccess: (response) => {
      const result = response.data;
      setEvaluation(result);
      setEvaluationHistory([...evaluationHistory, result]);
      setQuizIdInput("");
      setAnswersInput("");
    },
    onError: (error: any) => {
      alert("Evaluation failed: " + (error.response?.data?.detail || error.message));
    },
  });

  const handleEvaluate = () => {
    if (!quizIdInput.trim() || !answersInput.trim() || !user) return;

    const answers = answersInput
      .split(",")
      .map((a) => a.trim())
      .filter((a) => a);

    evaluateMutation.mutate({
      user_id: user.id,
      quiz_id: quizIdInput,
      answers: answers,
    });
  };

  const getScoreColor = (score: number) => {
    if (score >= 80) return "text-green-600";
    if (score >= 60) return "text-yellow-600";
    return "text-red-600";
  };

  return (
    <div className="space-y-6">
      <div>
        <h1 className="text-3xl font-bold">Evaluation Module</h1>
        <p className="text-muted-foreground mt-2">
          Evaluate your quiz performance and identify weak concepts
        </p>
      </div>

      {/* Evaluation Form */}
      <Card>
        <CardHeader>
          <CardTitle>Evaluate Quiz</CardTitle>
          <CardDescription>
            Submit your quiz answers for evaluation
          </CardDescription>
        </CardHeader>
        <CardContent className="space-y-4">
          <div>
            <label className="text-sm font-medium">Quiz ID</label>
            <Input
              placeholder="e.g., quiz_123"
              value={quizIdInput}
              onChange={(e) => setQuizIdInput(e.target.value)}
              className="mt-1"
            />
          </div>
          <div>
            <label className="text-sm font-medium">
              Answers (comma-separated indices, e.g., 0,1,2,3)
            </label>
            <Input
              placeholder="e.g., 0,1,2,3,1,0"
              value={answersInput}
              onChange={(e) => setAnswersInput(e.target.value)}
              className="mt-1"
            />
          </div>
          <Button
            onClick={handleEvaluate}
            disabled={
              evaluateMutation.isPending ||
              !quizIdInput.trim() ||
              !answersInput.trim()
            }
          >
            {evaluateMutation.isPending ? "Evaluating..." : "Submit for Evaluation"}
          </Button>
        </CardContent>
      </Card>

      {/* Current Evaluation Result */}
      {evaluation && (
        <Card className={evaluation.passed ? "border-green-200 bg-green-50" : "border-red-200 bg-red-50"}>
          <CardHeader>
            <div className="flex items-center justify-between">
              <CardTitle>Evaluation Result</CardTitle>
              <Badge variant={evaluation.passed ? "default" : "destructive"}>
                {evaluation.passed ? "PASSED ✓" : "NEEDS IMPROVEMENT"}
              </Badge>
            </div>
          </CardHeader>
          <CardContent className="space-y-4">
            <div className="grid grid-cols-2 gap-4">
              <div>
                <p className="text-sm text-muted-foreground">Score</p>
                <p className={`text-3xl font-bold ${getScoreColor(evaluation.score)}`}>
                  {evaluation.score}%
                </p>
              </div>
              <div>
                <p className="text-sm text-muted-foreground">Status</p>
                <p className="text-lg font-semibold">
                  {evaluation.passed ? "✓ Passed" : "✗ Failed"}
                </p>
              </div>
            </div>

            {evaluation.weak_concepts && evaluation.weak_concepts.length > 0 && (
              <div>
                <p className="text-sm font-medium mb-2">Weak Concepts to Review:</p>
                <div className="flex flex-wrap gap-2">
                  {evaluation.weak_concepts.map((concept: string, idx: number) => (
                    <Badge key={idx} variant="outline">
                      {concept}
                    </Badge>
                  ))}
                </div>
              </div>
            )}
          </CardContent>
        </Card>
      )}

      {/* Evaluation History */}
      {evaluationHistory.length > 0 && (
        <div>
          <h3 className="text-lg font-semibold mb-4 flex items-center gap-2">
            <BarChart3 className="h-5 w-5" />
            Evaluation History
          </h3>
          <div className="grid gap-4">
            {evaluationHistory.map((result, idx) => (
              <Card key={idx}>
                <CardHeader>
                  <div className="flex items-center justify-between">
                    <CardTitle className="text-base">
                      Quiz Attempt {evaluationHistory.length - idx}
                    </CardTitle>
                    <p className={`text-xl font-bold ${getScoreColor(result.score)}`}>
                      {result.score}%
                    </p>
                  </div>
                </CardHeader>
                <CardContent>
                  <div className="w-full bg-muted rounded-full h-2">
                    <div
                      className="bg-primary h-2 rounded-full transition-all"
                      style={{ width: `${result.score}%` }}
                    />
                  </div>
                </CardContent>
              </Card>
            ))}
          </div>
        </div>
      )}
    </div>
  );
}
