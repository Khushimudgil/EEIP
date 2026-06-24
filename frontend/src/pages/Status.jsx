import { useState } from "react";
import Layout from "../components/Layout";
import api from "../services/api";

function Status() {
  const [repoId, setRepoId] = useState("");
  const [status, setStatus] = useState(null);

  const fetchStatus = async () => {
    try {
      const response = await api.get(
        `/repository/${repoId}/status`
      );

      setStatus(response.data);
    } catch (error) {
      console.error(error);
      alert("Repository not found");
    }
  };

  return (
    <Layout>
      <div className="max-w-4xl">

        <h1 className="text-5xl font-bold text-amber-50 mb-3">
          Repository Status
        </h1>

        <p className="text-amber-200/70 mb-10">
          Check processing status.
        </p>

        <div className="bg-[#2A1E17] p-8 rounded-3xl">

          <input
            type="number"
            placeholder="Repository ID"
            value={repoId}
            onChange={(e) => setRepoId(e.target.value)}
            className="
              w-full
              p-4
              rounded-xl
              bg-[#1A120E]
              border
              border-amber-900/40
              text-white
              mb-5
            "
          />

          <button
            onClick={fetchStatus}
            className="
              bg-amber-700
              hover:bg-amber-600
              px-6
              py-3
              rounded-xl
            "
          >
            Check Status
          </button>

          {status && (
            <div className="mt-8">

              <p>
                <strong>ID:</strong> {status.repo_id}
              </p>

              <p>
                <strong>Status:</strong> {status.status}
              </p>

            </div>
          )}

        </div>

      </div>
    </Layout>
  );
}

export default Status;