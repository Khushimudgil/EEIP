import { Link } from "react-router-dom";
import { useState, useEffect } from "react";
import axios from "axios";

import {
  Upload,
  Activity,
  MessageSquare,
  BookOpen,
  Network,
  Database
} from "lucide-react";

import Layout from "../components/Layout";

function Dashboard() {

  const [stats, setStats] = useState({
    repositories: 0,
    files_parsed: 0,
    embeddings: 0,
    ai_queries: 0
  });

  useEffect(() => {
    loadDashboard();
  }, []);

  const loadDashboard = async () => {

    try {

      const response = await axios.get(
        "http://localhost:8001/dashboard-stats"
      );

      setStats(response.data);

    } catch (error) {

      console.log(error);

    }

  };

  const cards = [

    {
      title: "Upload Repository",
      description: "Connect and analyze GitHub repositories.",
      path: "/upload",
      icon: <Upload size={24} />
    },

    {
      title: "Repository Status",
      description: "Monitor indexing progress.",
      path: "/status",
      icon: <Activity size={24} />
    },

    {
      title: "AI Chat",
      description: "Ask questions about repository code.",
      path: "/chat",
      icon: <MessageSquare size={24} />
    },

    {
      title: "Repository Guide",
      description: "Generate complete documentation.",
      path: "/guide",
      icon: <BookOpen size={24} />
    },

    {
      title: "Knowledge Graph",
      description: "Explore repository structure.",
      path: "/knowledge-graph",
      icon: <Network size={24} />
    }

  ];

  return (

    <Layout>

      <div className="max-w-7xl">

        <h1 className="text-5xl font-bold text-amber-50 mb-3">
          EEIP Dashboard
        </h1>

        <p className="text-amber-200/70 mb-10">
          Enterprise Engineering Intelligence Platform
        </p>

        {/* Statistics */}

        <div className="grid md:grid-cols-4 gap-6 mb-10">

          <StatCard
            title="Repositories"
            value={stats.repositories}
          />

          <StatCard
            title="Files Parsed"
            value={stats.files_parsed}
          />

          <StatCard
            title="Embeddings"
            value={stats.embeddings}
          />

          <StatCard
            title="AI Queries"
            value={stats.ai_queries}
          />

        </div>

        {/* Modules */}

        <div className="grid md:grid-cols-2 xl:grid-cols-3 gap-8">

          {cards.map((card) => (

            <Link
              key={card.path}
              to={card.path}
            >

              <div
                className="
                bg-[#2A1E17]
                border
                border-amber-900/40
                rounded-3xl
                p-8
                hover:border-amber-600
                transition-all
                duration-300
                hover:-translate-y-1
                h-full
              "
              >

                <div
                  className="
                  bg-amber-700
                  w-14
                  h-14
                  rounded-2xl
                  flex
                  items-center
                  justify-center
                  mb-6
                "
                >
                  {card.icon}
                </div>

                <h2 className="text-2xl font-semibold text-white mb-3">
                  {card.title}
                </h2>

                <p className="text-amber-200/70">
                  {card.description}
                </p>

              </div>

            </Link>

          ))}

        </div>

      </div>

    </Layout>

  );

}

function StatCard({ title, value }) {

  return (

    <div
      className="
      bg-[#2A1E17]
      border
      border-amber-900/40
      rounded-3xl
      p-6
      shadow-xl
    "
    >

      <div className="flex items-center gap-3 mb-4">

        <Database
          size={24}
          className="text-amber-300"
        />

        <p className="text-amber-300 text-xl">
          {title}
        </p>

      </div>

      <h1 className="text-5xl font-bold text-white">
        {value}
      </h1>

    </div>

  );

}

export default Dashboard;