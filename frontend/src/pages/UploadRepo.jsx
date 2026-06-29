import { useState } from "react";
import { GitBranch, Upload } from "lucide-react";
import Layout from "../components/Layout";
import api from "../services/api";

function UploadRepo() {
  const [repoUrl, setRepoUrl] = useState("");
  const [loading, setLoading] = useState(false);

  const handleUpload = async () => {
    if (!repoUrl) {
      alert("Please enter repository URL");
      return;
    }

    try {
      setLoading(true);

      const response = await api.post("/upload-repository", {
        repo_url: repoUrl,
      });

      console.log(response.data);

      alert(JSON.stringify(response.data));

      setRepoUrl("");
    } catch (error) {
      console.error(error);
      alert("Upload failed");
    } finally {
      setLoading(false);
    }
  };

  return (
    <Layout>
      <div className="max-w-4xl">
        <h1 className="text-5xl font-bold text-amber-50 mb-3">
          Upload Repository
        </h1>

        <p className="text-amber-200/70 mb-10">
          Connect a GitHub repository and start analysis.
        </p>

        <div className="bg-[#2A1E17] border border-amber-900/40 rounded-3xl p-8">
          <div className="flex items-center gap-3 mb-6">
            <GitBranch size={24} />
            <h2 className="text-xl font-semibold">
              GitHub Repository URL
            </h2>
          </div>

          <input
            type="text"
            placeholder="https://github.com/user/repository"
            value={repoUrl}
            onChange={(e) => setRepoUrl(e.target.value)}
            className="
              w-full
              p-4
              rounded-xl
              bg-[#1A120E]
              border
              border-amber-900/40
              text-white
              outline-none
              mb-6
            "
          />

          <button
            onClick={handleUpload}
            disabled={loading}
            className="
              flex
              items-center
              gap-2
              bg-amber-700
              hover:bg-amber-600
              px-6
              py-3
              rounded-xl
              transition
              disabled:opacity-50
            "
          >
            <Upload size={18} />

            {loading
              ? "Uploading..."
              : "Analyze Repository"}
          </button>
        </div>
      </div>
    </Layout>
  );
}

export default UploadRepo;