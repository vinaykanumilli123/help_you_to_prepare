"use client";

import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import Link from "next/link";
import { Button } from "@/components/ui/button";
import { BookOpen, Brain, BarChart3, Sparkles, ArrowRight } from "lucide-react";

export function DashboardOverview() {
  const modules = [
    {
      title: "Research",
      description: "AI-powered research materials for any topic",
      icon: Brain,
      href: "/research",
      color: "from-blue-600 to-cyan-600",
      bgColor: "from-blue-50 to-cyan-50",
      borderColor: "border-blue-200",
      badge: "New",
    },
    {
      title: "Quiz",
      description: "Interactive quizzes and assessments",
      icon: BookOpen,
      href: "/quizzes",
      color: "from-violet-600 to-purple-600",
      bgColor: "from-violet-50 to-purple-50",
      borderColor: "border-violet-200",
      badge: "Coming Soon",
    },
    {
      title: "Evaluation",
      description: "Track your progress and performance",
      icon: BarChart3,
      href: "/evaluation",
      color: "from-emerald-600 to-teal-600",
      bgColor: "from-emerald-50 to-teal-50",
      borderColor: "border-emerald-200",
      badge: "Coming Soon",
    },
  ];

  return (
    <div className="space-y-12">
      {/* Hero Section */}
      <div className="relative">
        <div className="absolute inset-0 bg-gradient-to-r from-blue-500/10 via-purple-500/10 to-pink-500/10 rounded-3xl blur-3xl"></div>
        <div className="relative space-y-4">
          <div className="flex items-center gap-3">
            <div className="p-2 bg-gradient-to-r from-blue-600 to-violet-600 rounded-lg">
              <Sparkles className="h-6 w-6 text-white" />
            </div>
            <h1 className="text-5xl font-bold gradient-text">Welcome to StudyAI</h1>
          </div>
          <p className="text-xl text-slate-600 max-w-2xl">
            Your intelligent study companion powered by advanced AI. Explore research, test your knowledge, and track your progress all in one place.
          </p>
        </div>
      </div>

      {/* Quick Stats */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
        {[
          { label: "Topics Researched", value: "0", icon: "📚" },
          { label: "Quizzes Completed", value: "0", icon: "✅" },
          { label: "Average Score", value: "-", icon: "📊" },
        ].map((stat, idx) => (
          <Card key={idx} className="border-2 border-slate-200 hover:border-blue-300 transition-colors">
            <CardContent className="pt-6">
              <div className="flex items-center justify-between">
                <div>
                  <p className="text-sm text-slate-600 font-medium">{stat.label}</p>
                  <p className="text-3xl font-bold text-slate-900 mt-2">{stat.value}</p>
                </div>
                <span className="text-4xl opacity-50">{stat.icon}</span>
              </div>
            </CardContent>
          </Card>
        ))}
      </div>

      {/* Modules Grid */}
      <div>
        <h2 className="text-2xl font-bold mb-6 text-slate-900">Available Modules</h2>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
          {modules.map((module) => {
            const Icon = module.icon;
            return (
              <Link key={module.href} href={module.href}>
                <Card className={`border-2 ${module.borderColor} bg-gradient-to-br ${module.bgColor} hover:shadow-xl transition-all transform hover:scale-105 h-full cursor-pointer group`}>
                  <CardHeader>
                    <div className="flex items-start justify-between mb-4">
                      <div className={`p-3 bg-gradient-to-br ${module.color} rounded-xl shadow-lg group-hover:shadow-xl transition-all`}>
                        <Icon className="h-6 w-6 text-white" />
                      </div>
                      <Badge className="bg-gradient-to-r from-blue-600 to-violet-600 text-white text-xs">
                        {module.badge}
                      </Badge>
                    </div>
                    <CardTitle className="text-xl">{module.title}</CardTitle>
                    <CardDescription className="text-sm">{module.description}</CardDescription>
                  </CardHeader>
                  <CardContent>
                    <Button className={`w-full bg-gradient-to-r ${module.color} text-white hover:opacity-90 rounded-xl font-semibold group-hover:translate-x-1 transition-all`}>
                      Get Started
                      <ArrowRight className="h-4 w-4 ml-2" />
                    </Button>
                  </CardContent>
                </Card>
              </Link>
            );
          })}
        </div>
      </div>

      {/* CTA Section */}
      <div className="relative">
        <div className="absolute inset-0 bg-gradient-to-r from-blue-600/20 to-violet-600/20 rounded-2xl blur-2xl"></div>
        <Card className="relative border-2 border-blue-300 bg-gradient-to-r from-blue-50 to-violet-50">
          <CardContent className="pt-8">
            <div className="flex items-center justify-between">
              <div>
                <h3 className="text-xl font-bold text-slate-900">Ready to boost your learning?</h3>
                <p className="text-slate-600 mt-1">Start with Research to explore new topics today</p>
              </div>
              <Link href="/research">
                <Button className="bg-gradient-to-r from-blue-600 to-violet-600 text-white font-semibold rounded-xl">
                  Start Researching
                  <Sparkles className="h-4 w-4 ml-2" />
                </Button>
              </Link>
            </div>
          </CardContent>
        </Card>
      </div>
    </div>
  );
}
