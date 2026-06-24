import Layout from "../components/Layout";
import { motion } from "framer-motion";

function Dashboard() {

  const stats = [
    {
      title: "Repositories",
      value: "0"
    },
    {
      title: "Files",
      value: "0"
    },
    {
      title: "Embeddings",
      value: "0"
    },
    {
      title: "Searches",
      value: "0"
    }
  ];

  return (
    <Layout>

      {/* Header */}

      <div className="mb-10">

        <h1 className="text-5xl font-bold text-[#f5e6d3] mb-3">
          Dashboard
        </h1>

        <p className="text-[#b8a08d] text-lg">
          Enterprise Engineering Intelligence Platform
        </p>

      </div>

      {/* Stats */}

      <div className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-4 gap-6">

        {stats.map((item, index) => (

          <motion.div
            key={item.title}
            initial={{
              opacity: 0,
              y: 20
            }}
            animate={{
              opacity: 1,
              y: 0
            }}
            transition={{
              delay: index * 0.1
            }}
            whileHover={{
              scale: 1.03
            }}
            className="
              bg-[#241912]/80
              backdrop-blur-lg
              border
              border-[#3a2b20]
              rounded-2xl
              p-6
              shadow-xl
              hover:border-[#c68b59]
              transition-all
              duration-300
            "
          >

            <h3 className="text-[#b8a08d] text-lg">
              {item.title}
            </h3>

            <p className="text-5xl font-bold text-[#f5e6d3] mt-4">
              {item.value}
            </p>

          </motion.div>

        ))}

      </div>

      {/* Recent Activity */}

      <div className="mt-10">

        <div
          className="
            bg-[#241912]/80
            backdrop-blur-lg
            border
            border-[#3a2b20]
            rounded-2xl
            p-8
            shadow-xl
          "
        >

          <div className="flex items-center justify-between mb-6">

            <h2 className="text-2xl font-semibold text-[#f5e6d3]">
              Recent Activity
            </h2>

            <span
              className="
                px-4
                py-2
                rounded-full
                bg-[#8b5e3c]
                text-sm
                text-white
              "
            >
              No Activity
            </span>

          </div>

          <div className="text-[#b8a08d]">
            No repositories analyzed yet.
          </div>

        </div>

      </div>

      {/* Welcome Card */}

      <div className="mt-10">

        <div
          className="
            rounded-3xl
            p-10
            border
            border-[#3a2b20]
            bg-gradient-to-r
            from-[#3a2415]
            via-[#5a3924]
            to-[#7a4d2e]
            shadow-2xl
          "
        >

          <h2 className="text-3xl font-bold text-white mb-4">
            Welcome to EEIP
          </h2>

          <p className="text-[#f5e6d3] text-lg">
            Upload repositories, generate embeddings,
            perform hybrid search, and chat with your codebase
            using AI-powered repository intelligence.
          </p>

        </div>

      </div>

    </Layout>
  );
}

export default Dashboard;