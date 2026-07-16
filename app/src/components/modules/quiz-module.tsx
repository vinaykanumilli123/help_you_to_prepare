"use client";

import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { Input } from "@/components/ui/input";
import { Button } from "@/components/ui/button";
import { Badge } from "@/components/ui/badge";
import { Skeleton } from "@/components/ui/skeleton";
import { Play, Plus } from "lucide-react";
import { useState } from "react";
import { useMutation } from "@tanstack/react-query";
import { apiClient } from "@/services/api";
import { useAuth } from "@/hooks/useAuth";

export function QuizModule() {
  const { user } = useAuth();
  const [topicIdInput, setTopicIdInput] = useState("");
  const [quizzes, setQuizzes] = useState<any[]>([]);
  const [currentQuiz, setCurrentQuiz] = useState<any>(null);
  const [answers, setAnswers] = useState<string[]>([]);

  const generateQuizMutation = useMutation({
    mutationFn: (data: any) => apiClient.quizzes.generate(data),
    onSuccess: (response) => {
      const quiz = response.data;
      setCurrentQuiz(quiz);
      setQuizzes([...quizzes, quiz]);
      setAnswers(Array(quiz.questions.length).fill(""));
    },
    onError: (error: any) => {
      alert("Quiz generation failed: " + (error.response?.data?.detail || error.message));
    },
  });

  const handleGenerateQuiz = () => {
    if (!topicIdInput.trim() || !user) return;

    generateQuizMutation.mutate({
      user_id: user.id,
      topic_id: topicIdInput,
    });
  };

  const handleAnswerSelect = (questionIndex: number, optionIndex: number) => {
    const newAnswers = [...answers];
    newAnswers[questionIndex] = optionIndex.toString();
    setAnswers(newAnswers);
  };

  const handleSubmitQuiz = () => {
    if (!answers.every((a) => a !== "")) {
      alert("Please answer all questions");
      return;
    }
    // Submit to evaluation - will be handled in next step
    alert("Quiz complete! Answers: " + JSON.stringify(answers));
  };

  return (
    <div className="space-y-6">
      <div>
        <h1 className="text-3xl font-bold">Quiz Module</h1>
        <p className="text-muted-foreground mt-2">
          Test your knowledge with AI-generated quizzes
        </p>
      </div>

      {/* Generate Quiz Form */}
      <Card>
        <CardHeader>
          <CardTitle>Generate Quiz</CardTitle>
          <CardDescription>
            Enter the topic ID from your research to generate a quiz
          </CardDescription>
        </CardHeader>
        <CardContent className="space-y-4">
          <div>
            <label className="text-sm font-medium">Topic ID</label>
            <Input
              placeholder="e.g., topic_123"
              value={topicIdInput}
              onChange={(e) => setTopicIdInput(e.target.value)}
              className="mt-1"
            />
          </div>
          <Button
            onClick={handleGenerateQuiz}
            disabled={generateQuizMutation.isPending || !topicIdInput.trim()}
            className="gap-2"
          >
            <Plus className="h-4 w-4" />
            {generateQuizMutation.isPending ? "Generating..." : "Generate Quiz"}
          </Button>
        </CardContent>
      </Card>

      {/* Quiz Display */}
      {generateQuizMutation.isPending && <Skeleton className="h-96" />}

      {currentQuiz && (
        <Card>
          <CardHeader>
            <CardTitle>Quiz: {currentQuiz.quiz_id}</CardTitle>
            <CardDescription>
              {currentQuiz.questions.length} questions
            </CardDescription>
          </CardHeader>
          <CardContent className="space-y-6">
            {currentQuiz.questions.map((q: any, qIndex: number) => (
              <div key={qIndex} className="border-b pb-6 last:border-b-0">
                <p className="font-semibold mb-3">
                  {qIndex + 1}. {q.question}
                </p>
                <div className="space-y-2">
                  {q.options.map((option: string, oIndex: number) => (
                    <button
                      key={oIndex}
                      onClick={() => handleAnswerSelect(qIndex, oIndex)}
                      className={`w-full text-left p-3 rounded-lg border-2 transition-all ${
                        answers[qIndex] === oIndex.toString()
                          ? "border-primary bg-primary/10"
                          : "border-border hover:border-primary/50"
                      }`}
                    >
                      <span className="font-medium">{String.fromCharCode(65 + oIndex)}.</span>{" "}
                      {option}
                    </button>
                  ))}
                </div>
              </div>
            ))}
            <Button onClick={handleSubmitQuiz} className="w-full" size="lg">
              Submit Quiz
            </Button>
          </CardContent>
        </Card>
      )}

      {/* Previous Quizzes */}
      {quizzes.length > 1 && (
        <div>
          <h3 className="text-lg font-semibold mb-4">Previous Quizzes</h3>
          <div className="grid gap-4">
            {quizzes.slice(0, -1).map((quiz) => (
              <Card key={quiz.quiz_id}>
                <CardHeader>
                  <CardTitle className="text-base">{quiz.quiz_id}</CardTitle>
                </CardHeader>
                <CardContent>
                  <Button variant="outline" className="w-full">
                    <Play className="h-4 w-4 mr-2" />
                    Retake Quiz
                  </Button>
                </CardContent>
              </Card>
            ))}
          </div>
        </div>
      )}
    </div>
  );
}
